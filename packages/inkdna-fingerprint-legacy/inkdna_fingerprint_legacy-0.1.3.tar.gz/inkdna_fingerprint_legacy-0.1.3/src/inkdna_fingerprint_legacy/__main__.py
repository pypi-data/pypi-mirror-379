from __future__ import annotations
import argparse, sys, json
from pathlib import Path

def main():
    ap = argparse.ArgumentParser(
        prog="inkdna",
        description="Stamp & verify PDFs with sidecars (execution-only)."
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    ap_s = sub.add_parser("stamp", help="Stamp a PDF and emit a sidecar")
    ap_s.add_argument("input", type=Path, help="Input PDF")
    ap_s.add_argument("-o", "--output", type=Path, help="Output PDF path")
    ap_s.add_argument("--code", type=str, default="", help="Optional attribution code (e.g., order/customer id)")

    ap_v = sub.add_parser("verify", help="Verify a stamped PDF; sidecar optional")
    ap_v.add_argument("input", type=Path, help="Stamped PDF")
    ap_v.add_argument("--sidecar", type=Path, help="Optional sidecar JSON to cross-check")

    args = ap.parse_args()

    if args.cmd == "stamp":
        inp = args.input
        if not inp.exists():
            print(f"[!] Input not found: {inp}", file=sys.stderr)
            sys.exit(2)
        if inp.suffix.lower() != ".pdf":
            print("[!] Only .pdf is supported", file=sys.stderr)
            sys.exit(2)
        from .stamp_pdf import stamp_pdf  # lazy import
        out = stamp_pdf(inp, args.output, code=args.code)
        print(str(out))
        return

    if args.cmd == "verify":
        if args.input.suffix.lower() != ".pdf":
            print("[!] Only .pdf is supported", file=sys.stderr)
            sys.exit(2)
        from .verify import verify_pdf  # lazy import
        detail = verify_pdf(args.input, sidecar=args.sidecar)
        print(json.dumps(detail, indent=2))
        sys.exit(0 if detail.get("ok") else 1)

if __name__ == "__main__":
    main()