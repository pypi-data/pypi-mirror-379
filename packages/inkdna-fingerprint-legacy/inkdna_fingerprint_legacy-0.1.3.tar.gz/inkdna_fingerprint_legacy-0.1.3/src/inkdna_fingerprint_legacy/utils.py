from __future__ import annotations
import json, base64, hashlib, time
from pathlib import Path

TOOL = "inkdna-cli"
VERSION = "0.1.3"
MARKER = b"INKDNA_PAYLOAD_V1"  # stream marker inside PDFs

def now_ts() -> int:
    return int(time.time())

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def write_sidecar(output_path: Path, payload: dict) -> Path:
    base = output_path.with_suffix("")
    sidecar = base.with_name(f"{base.name}_inkdna_signature.json")
    sidecar.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return sidecar

def b64e(b: bytes) -> str:
    import base64
    return base64.b64encode(b).decode("ascii")

def b64d(s: str) -> bytes:
    import base64
    return base64.b64decode(s.encode("ascii"))
