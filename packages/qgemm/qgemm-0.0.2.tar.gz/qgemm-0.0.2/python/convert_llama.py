import os
import json
import math
import yaml
import torch
from dataclasses import dataclass
from typing import Optional, Dict, Any, List, Tuple
from transformers import AutoModelForCausalLM, AutoConfig
from safetensors.torch import save_file
from tqdm import tqdm

from quantize import compute_group_scales, quantize_int4_pack

from quantize import detect_outliers

from quantize import apply_outlier_bypass

@dataclass
class ConvertArgs:
    hf_path: str
    out_path: str
    group_size: int = 64
    pack_axis: str = "K"  
    outlier_pct: float = 0.0
    percentile: float = 99.9
    policy_path: Optional[str] = None
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    dtype: torch.dtype = torch.float16

def load_policy(policy_path: Optional[str]) -> Dict[str, Any]:
    if not policy_path:
        return {}
    with open(policy_path, "r") as f:
        return yaml.safe_load(f) or {}

def iter_llama_linear_layers(model) -> List[Tuple[str, torch.nn.Linear]]:
    """
    Returns list of (layer_name, linear_module) for:
    - Attention: q_proj, k_proj, v_proj, o_proj
    - MLP: up_proj, gate_proj, down_proj
    Adjust for exact HF model class layout if needed.
    """
    layers = []
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            # Heuristic include only target projections
            lname = name.split(".")[-1]
            if lname in {"q_proj", "k_proj", "v_proj", "o_proj", "up_proj", "gate_proj", "down_proj"}:
                layers.append((name, module))
    return layers

def get_layer_policy(global_args: ConvertArgs, per_layer: Dict[str, Any],
layer_name: str) -> Dict[str, Any]:
    conf = {
        "quant_enabled": True,
        "group_size": global_args.group_size,
        "outlier_pct": global_args.outlier_pct,
        "percentile": global_args.percentile,
        "pack_axis": global_args.pack_axis,
        "epilogue_variant": None,
    }
    if per_layer and layer_name in per_layer:
        conf.update(per_layer[layer_name] or {})
    return conf

def convert_linear_layer(
    layer_name: str,
    linear: torch.nn.Linear,
    cfg: Dict[str, Any],
    device: str,
    store_dtype: torch.dtype,
) -> Dict[str, Any]:
    """
    Convert a single Linear layer to INT4 packed format.
    Returns a dict ready to save via safetensors with tensors + metadata.
    """
    W = linear.weight.detach().to(device=device, dtype=store_dtype)  

    bias = linear.bias.detach().to(device=device, dtype=store_dtype) if linear.bias is not None else None
    
    M, K = W.shape

    if cfg["pack_axis"] != "K":
        raise ValueError("Only pack_axis='K' is supported.")

    # outlier detection
    out_idx = torch.empty(0, dtype=torch.long, device=device)
    W_q = W
    outlier_w = None

    if cfg.get("outlier_pct", 0.0) > 0.0:
        out_idx, _ = detect_outliers(W, pct=cfg["outlier_pct"], axis="row",score="l2")
        if out_idx.numel() > 0:
            W_q, outlier_w, meta = apply_outlier_bypass(W, out_idx, axis="row", store_dtype=store_dtype)
        else:
            meta = {"axis": "row", "indices": out_idx, "orig_shape": (M, K)}

    # compute per-group scales on quantizable rows
    scales = compute_group_scales(W_q, group_size=cfg["group_size"], percentile=cfg["percentile"])  # [M, ceil(K/g)]

    # quantize and pack along K
    packed_w = quantize_int4_pack(W_q, scales, group_size=cfg["group_size"], pack_axis="K")  # uint8 [M, ceil(K/2)]

    # build metadata
    metadata = {
        "dtype": "int4",
        "endianness": "little_nibbles", 
        "pack_axis": "K",
        "group_size": int(cfg["group_size"]),
        "scale_layout": "row_major_groups_K",  # [M, ceil(K/group_size)]
        "outlier_pct": float(cfg.get("outlier_pct", 0.0)),
        "percentile": float(cfg.get("percentile", 99.9)),
        "orig_shape": [int(M), int(K)],
        "has_bias": bias is not None,
        "epilogue_variant": cfg.get("epilogue_variant"),
        "layer_name": layer_name,
    }

    # assemble tensors dict for safetensors
    tensors = {
        "packed_w": packed_w,               # uint8
        "scales": scales.to(store_dtype),   # fp16
    }
    if bias is not None:
        tensors["bias"] = bias
    if out_idx.numel() > 0 and outlier_w is not None:
        tensors["outlier_idx"] = out_idx.to(torch.int32)  # smaller type ok
        tensors["outlier_w"] = outlier_w  # fp16
        metadata["outlier_axis"] = "row"
        metadata["outlier_shape"] = list(outlier_w.shape)

    return {"tensors": tensors, "metadata": metadata}

def save_layer_safetensors(out_dir: str, layer_name: str, payload: Dict[str,Any]) -> str:
    os.makedirs(out_dir, exist_ok=True)
    fname = layer_name.replace(".", "_") + ".safetensors"
    fpath = os.path.join(out_dir, fname)
    meta = {k: json.dumps(v) if isinstance(v, (dict, list)) else str(v) for k, v in payload["metadata"].items()}
    save_file(payload["tensors"], fpath, metadata=meta)
    return fpath

def convert_model_to_int4_safetensors(
    hf_path: str,
    out_path: str,
    group_size: int = 64,
    pack_axis: str = "K",
    outlier_pct: float = 0.0,
    policy_path: Optional[str] = None,
    percentile: float = 99.9,
    device: Optional[str] = None,
    dtype: torch.dtype = torch.float16,
):
    device = device or ("cuda" if torch.cuda.is_available() else "cpu")
    args = ConvertArgs(
        hf_path=hf_path,
        out_path=out_path,
        group_size=group_size,
        pack_axis=pack_axis,
        outlier_pct=outlier_pct,
        percentile=percentile,
        policy_path=policy_path,
        device=device,
        dtype=dtype,
    )
    os.makedirs(out_path, exist_ok=True)

    # load model from HF
    config = AutoConfig.from_pretrained(hf_path)
    model = AutoModelForCausalLM.from_pretrained(hf_path, torch_dtype=dtype,device_map="auto")
    model.eval()

    # load optional per-layer policy
    per_layer_policy = load_policy(args.policy_path)

    # collect target linear layers
    layers = iter_llama_linear_layers(model)

    index = {
        "hf_path": hf_path,
        "model_type": config.model_type,
        "pack_axis": args.pack_axis,
        "default_group_size": args.group_size,
        "layers": {},
    }

    for layer_name, linear in tqdm(layers, desc="Converting layers"):
        lcfg = get_layer_policy(args, per_layer_policy, layer_name)
        if not lcfg.get("quant_enabled", True):
            continue

        payload = convert_linear_layer(layer_name, linear, lcfg, device=args.device, store_dtype=args.dtype)
        fpath = save_layer_safetensors(out_path, layer_name, payload)

        # record entry in index
        entry = {
            "file": os.path.basename(fpath),
            "metadata": payload["metadata"],
            "tensors": list(payload["tensors"].keys()),
        }
        index["layers"][layer_name] = entry

    # save index json
    with open(os.path.join(out_path, "index.json"), "w") as f:
        json.dump(index, f, indent=2)

    return index

# loader helper for a single layer file
  
def load_int4_safetensors(layer_path: str):
    """Load a single layer file with tensors and metadata.
    Returns: packed_w, scales, bias, metadata, (out_idx, outlier_w)
    """
    from safetensors import safe_open

    metadata: Dict[str, Any] = {}
    tensors: Dict[str, torch.Tensor] = {}
    with safe_open(layer_path, framework="pt", device="cpu") as f:
        # metadata is a dict[str, str]
        meta_raw = f.metadata() or {}
        for k, v in meta_raw.items():
            try:
                metadata[k] = json.loads(v)
            except Exception:
                metadata[k] = v
        for name in f.keys():
            tensors[name] = f.get_tensor(name)

    packed_w = tensors.get("packed_w")
    scales = tensors.get("scales")
    bias = tensors.get("bias") if "bias" in tensors else None
    out_idx = tensors.get("outlier_idx") if "outlier_idx" in tensors else None
    outlier_w = tensors.get("outlier_w") if "outlier_w" in tensors else None

    return packed_w, scales, bias, metadata, (out_idx, outlier_w)
