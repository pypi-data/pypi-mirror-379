from __future__ import annotations
from pathlib import Path
from typing import Optional, Tuple
import io, json, zlib
import pikepdf
from .utils import now_ts, sha256_bytes, write_sidecar, MARKER, TOOL, VERSION

def _collect_canonical_hash(pdf: pikepdf.Pdf) -> Tuple[str, int, list]:
    import hashlib
    h = hashlib.sha256()
    page_info = []
    total_streams = 0
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
            total_streams += 1
            stream_sizes.append(len(data))
            if MARKER in data:
                # skip our own payload streams
                continue
            h.update(data)
        page_info.append({"page": idx, "stream_count": len(stream_sizes), "stream_sizes": stream_sizes})
    return h.hexdigest(), total_streams, page_info

def stamp_pdf(input_path: Path, output_path: Optional[Path] = None, *, code: str = "") -> Path:
    input_path = Path(input_path)
    if output_path is None:
        output_path = input_path.with_name(input_path.stem + "_inkdna.pdf")

    with pikepdf.open(str(input_path)) as pdf:
        canon_hash, total_streams, page_info = _collect_canonical_hash(pdf)

        # Prepare payload to embed
        payload = {
            "issuer": "inkdna",
            "tool": TOOL,
            "version": VERSION,
            "ts": now_ts(),
            "type": "pdf",
            "code": code or "",
            "canon_sha256": canon_hash,
            "page_count": len(pdf.pages),
        }
        raw = json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        comp = zlib.compress(raw, level=9)
        stm = MARKER + b"\n" + comp

        # Append one small stream per file (so we can skip it when hashing)
        for page in pdf.pages[:1]:  # embed once (first page) to keep file small
            existing = page.Contents
            if existing is None:
                arr = []
            elif isinstance(existing, pikepdf.Array):
                arr = list(existing)
            else:
                arr = [existing]
            new_stream = pdf.make_stream(stm)
            arr.append(new_stream)
            page.Contents = pdf.make_indirect(pikepdf.Array(arr))

        pdf.save(str(output_path))

    # Sidecar mirrors payload + raw bytes for future auditing
    sidecar = {
        "payload": payload,
    }
    write_sidecar(output_path, sidecar)
    return output_path
