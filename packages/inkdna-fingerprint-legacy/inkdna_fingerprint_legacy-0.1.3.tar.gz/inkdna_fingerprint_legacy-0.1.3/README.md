# InkDNA Fingerprint (Simple CLI — PDF only)

A lean, Windows-friendly CLI to **stamp** and **verify** PDFs.

## What it does

* **stamp**: embeds a compact InkDNA payload **inside the PDF** and writes a **sidecar JSON** next to the output (`*_inkdna_signature.json`).
* **verify**: reads the embedded payload and **recomputes a canonical hash** of the page content streams (ignoring our own payload).
  Optionally, pass a sidecar to **cross-check**. Prints **full forensic details** every time.

> No activation, no licensing, no remote calls. Execution-only.

---

## Install (from PyPI)

```bat
py -m pip install --upgrade pip
py -m pip install --upgrade inkdna-fingerprint-legacy
```

This installs the `inkdna` command.

### (Optional) Install from source (developers)

```bat
:: from the project root containing pyproject.toml
py -m pip install --upgrade pip
py -m pip install .
```

---

## Usage

### Stamp

```bat
inkdna stamp "C:\\path\\input.pdf" -o "C:\\path\\output.pdf" --code "ORDER-123"
```

* Always writes a sidecar: `output_inkdna_signature.json`

### Verify (sidecar optional)

```bat
inkdna verify "C:\\path\\output.pdf"
inkdna verify "C:\\path\\output.pdf" --sidecar "C:\\path\\output_inkdna_signature.json"
```

### Output (forensic JSON)

* `ok`: `true` if the canonical hash matches.
* `embedded`: payload embedded in the PDF (issuer, version, timestamp, code, file type, canonical hash, page count).
* `recomputed_canon_sha256`: hash recomputed from page content streams (our own tiny marker stream is ignored).
* `page_streams`: per-page stream counts and sizes.
* `sidecar_payload` and `sidecar_mismatches` when a sidecar is supplied.

**Note:** The canonical hash is derived from page content streams only and **does not include** the `code` or timestamp. Stamping the *same* PDF multiple times yields the **same** canonical hash. Any real change to page content will change the hash.

### Exit codes

* `0` — verification passed (`ok: true`)
* `1` — verification failed
* `2` — input/usage error

### Sidecar naming rule

`<output_basename>_inkdna_signature.json`
Example: `Resume_inkdna.pdf` → `Resume_inkdna_inkdna_signature.json`.

---

## License

MIT

## Version

`0.1.3`
