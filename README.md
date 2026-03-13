# Build bsp_test wheel with Docker

Build a Pyodide/WebAssembly wheel from `bsp_test.py` using Docker.

## Prerequisites

- Docker
- Project files: `bsp_test.py`, `setup.py`, `pyproject.toml`

## Build

From the project directory:

Windows:

```powershell
docker run --rm -v "${PWD}:/src" -w /src ghcr.io/pyodide/pyodide-env:20251004-chrome140-firefox140-py313 bash -c "pip install --upgrade pip pyodide-build && pyodide build"
```

## Output

The wheel is written to `dist/`:

- `dist/bsp_test-1.0.0-cp313-cp313-pyodide_2025_0_wasm32.whl`

## Running

Just serve the index.html, tests should pass.