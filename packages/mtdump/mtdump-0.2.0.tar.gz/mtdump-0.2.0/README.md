## mtdump

Robust Python object serialization to a single `.mtd` file with optional compression, encryption, checksum validation, and rich environment diagnostics metadata for compatibility and debugging.

### Intro

`mtdump` provides two simple functions — `save_dump` and `load_dump` — to persist arbitrary Python objects safely. Dumps can be compressed, encrypted with a key, validated with checksum, and include environment diagnostics metadata (Python, optionally specified packages, and versions of currently imported modules) to aid debugging and compatibility when loading across environments.

Key features:

- Compression via Zstandard
- Encryption via AES-256-CBC
- Integrity verification via SHA-256 checksum
- Environment diagnostics, versions of currently imported modules, and custom metadata embedded alongside the payload

### Installation

- From PyPI (once published): `pip install mtdump`
- From source: `pip install -e .`
- Optional dill support: `pip install mtdump[dill]` (or `pip install dill`)

### Examples

Basic use:

```python
from mtdump import save_dump, load_dump

obj = {"a": 1, "b": [1, 2, 3]}
result = save_dump(obj, "data.mtd")
restored = load_dump("data.mtd")
assert restored == obj
```

Enable encryption with checksum validation (auto-generate a secure key):

```python
result = save_dump(obj, "secret.mtd", passphrase="auto")
restored = load_dump("secret.mtd", passphrase=result["passphrase"], checksum=result["checksum"])  # base64 key; validates SHA-256
```

Use dill instead of pickle (for broader object support):

```python
# pip install mtdump[dill]  or  pip install dill
save_dump(obj, "data.mtd", serializer="dill")
```

Attach custom metadata and read it back:

```python
meta = {"experiment_id": "exp_123", "user": "alice"}
save_dump(obj, "meta.mtd", meta=meta)
restored, info = load_dump("meta.mtd", return_info=True)
assert info["meta"]["experiment_id"] == "exp_123"
```

Verify integrity with a known checksum:

```python
result = save_dump(obj, "chk.mtd")
restored = load_dump("chk.mtd", checksum=result["checksum"])  # raises if mismatch
```

Load from URL with headers (e.g., auth):

```python
obj = load_dump(
    "https://example.com/path/to/file.mtd",
    storage_options={"Authorization": "Bearer <token>"},
)
```

Record versions for specific packages in the environment diagnostics metadata:

```python
save_dump(obj, "env.mtd", env_packages=["numpy"])
```

### Documentation

API:

```python
def save_dump(
    obj,
    path,
    compression: "zstd | None" = "zstd",
    protocol: int = 5,
    serializer: "pickle | dill" = "pickle",
    passphrase: None | bytes | str | "auto" = None,
    meta: dict | None = None,
    env_packages: list[str] | None = None,
) -> dict

def load_dump(
    path: str | pathlib.Path,
    passphrase: None | bytes | str = None,
    checksum: str | None = None,
    return_info: bool = False,
    storage_options: dict[str, str] | None = None,
) -> object | tuple[object, dict]
```

Notes:

- **Compression**: `compression="zstd"` (default) or `None`.
- **Encryption**: AES-256-CBC with random IV and PKCS#7. Provide a 32‑byte key (as bytes) or a base64 string; `passphrase="auto"` generates a secure key and returns its base64 string in the result.
- **Integrity**: SHA-256 checksum is computed pre-compression and verified on load. Supply `checksum=` to enforce a specific expected digest.
- **Serializer**: `pickle` (default) or `dill` (optional dependency) for more complex objects.
- **Metadata**: The `info` JSON includes the Python version and, if provided via `env_packages`, versions for those packages (e.g., `"numpy"`, `"scikit-learn"`). It also includes a mapping of all currently loaded installed top-level modules with versions, dump settings, and your `meta` dict — useful for diagnosing loading issues and confirming environment compatibility.
- **File format**: `MTD1` magic header; 8‑byte little-endian lengths for the `info` JSON and payload; payload is optionally encrypted and/or compressed bytes.

License: MIT
