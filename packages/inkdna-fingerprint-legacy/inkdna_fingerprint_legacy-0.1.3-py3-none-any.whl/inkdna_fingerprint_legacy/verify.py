from __future__ import annotations
from pathlib import Path
from typing import Optional, Any, Dict
import json, zlib, hashlib
import pikepdf
from .utils import MARKER

def _pdf_extract_payload(pdf: pikepdf.Pdf) -> Optional[dict]:
    for page in pdf.pages:
        raw = page.Contents
        if raw is None:
            refs = []
        elif isinstance(raw, pikepdf.Array):
            refs = list(raw)
        else:
            refs = [raw]
        for ref in refs:
            try:
                obj = ref if hasattr(ref, "read_bytes") else pdf.open_object(ref)
                data = obj.read_bytes()
            except Exception:
                continue
            if MARKER in data:
                try:
                    _, blob = data.split(MARKER + b"\n", 1)
                    payload = json.loads(zlib.decompress(blob).decode("utf-8"))
                    if isinstance(payload, dict) and payload.get("type") == "pdf":
                        return payload
                except Exception:
                    continue
    return None

def _pdf_canon_sha(pdf: pikepdf.Pdf):
    h = hashlib.sha256()
    page_info = []
    for idx, page in enumerate(pdf.pages, start=1):
        raw = page.Contents
        if raw is None:
            refs = []
        elif isinstance(raw, pikepdf.Array):
            refs = list(raw)
        else:
            refs = [raw]
        stream_sizes = []
        for ref in refs:
            try:
                obj = ref if hasattr(ref, "read_bytes") else pdf.open_object(ref)
                data = obj.read_bytes()
            except Exception:
                continue
            stream_sizes.append(len(data))
            if MARKER in data:
                continue
            h.update(data)
        page_info.append({"page": idx, "stream_count": len(stream_sizes), "stream_sizes": stream_sizes})
    return h.hexdigest(), page_info

def verify_pdf(path: Path, *, sidecar: Optional[Path] = None) -> dict:
    path = Path(path)
    detail: Dict[str, Any] = {"type": "pdf", "file": str(path)}
    with pikepdf.open(str(path)) as pdf:
        embedded = _pdf_extract_payload(pdf)
        canon, page_info = _pdf_canon_sha(pdf)

    detail["embedded"] = embedded or {}
    detail["recomputed_canon_sha256"] = canon
    detail["page_count"] = len(page_info)
    detail["page_streams"] = page_info
    detail["ok"] = bool(embedded and embedded.get("canon_sha256") == canon)

    if sidecar:
        try:
            sc = json.loads(Path(sidecar).read_text(encoding="utf-8"))
            scp = sc.get("payload", sc)
            detail["sidecar_load"] = "ok"
            detail["sidecar_payload"] = scp
            mismatches = {}
            if embedded and isinstance(scp, dict):
                for k in ("canon_sha256", "code", "type"):
                    if k in embedded and k in scp and embedded[k] != scp[k]:
                        mismatches[k] = {"embedded": embedded[k], "sidecar": scp[k]}
            detail["sidecar_mismatches"] = mismatches
        except Exception as e:
            detail["sidecar_load"] = f"error: {e}"

    return detail
