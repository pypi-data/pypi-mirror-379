import base64
import datetime
import hashlib
import importlib
import importlib.metadata
import io
import json
import os
import pickle
import struct
import sys
from pathlib import Path
from typing import Any, Dict, Literal, Optional, Union
from urllib.request import Request, urlopen

from .common import (
    MTDChecksumError,
    MTDDecryptionError,
    MTDFormatError,
    _get_environment_info,
    _get_loaded_modules_info,
)

try:
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

    CRYPTOGRAPHY_AVAILABLE = True
except ImportError:
    CRYPTOGRAPHY_AVAILABLE = False

try:
    import zstandard as zstd

    ZSTANDARD_AVAILABLE = True
except ImportError:
    ZSTANDARD_AVAILABLE = False

try:
    import dill

    DILL_AVAILABLE = True
except ImportError:
    DILL_AVAILABLE = False


# --- Constants ---
MAGIC_NUMBER = b"MTD1"
INFO_LEN_FORMAT = "<Q"  # 8-byte unsigned long long, little-endian
PAYLOAD_LEN_FORMAT = "<Q"  # 8-byte unsigned long long, little-endian
AES_KEY_SIZE = 32  # bytes for AES-256
IV_SIZE = 16  # bytes for AES-CBC


# --- Low-level Helper Functions ---
def _generate_key() -> bytes:
    """
    Generates a secure 32-byte key for AES-256.

    Returns:
        A 32-byte key.
    """
    return os.urandom(AES_KEY_SIZE)


def _prepare_key(passphrase: Union[None, str, bytes]) -> Optional[bytes]:
    """
    Validates and prepares the encryption key from a passphrase.

    Args:
        passphrase: The passphrase to prepare.
            - None: Returns None.
            - bytes: Must be 32 bytes long.
            - str: Must be a base64-encoded string that decodes to 32 bytes.

    Returns:
        A 32-byte key, or None if the input passphrase is None.

    Raises:
        ValueError: If the key is invalid (e.g., wrong length).
    """
    if passphrase is None:
        return None

    if isinstance(passphrase, str):
        try:
            key = base64.b64decode(passphrase)
        except (ValueError, TypeError):
            raise ValueError("Invalid base64-encoded string for passphrase.")
    elif isinstance(passphrase, bytes):
        key = passphrase
    else:
        raise TypeError("Passphrase must be None, str, or bytes.")

    if len(key) != AES_KEY_SIZE:
        raise ValueError(f"Encryption key must be {AES_KEY_SIZE} bytes long.")

    return key


def _encrypt_data(data: bytes, key: bytes) -> bytes:
    """
    Encrypts data using AES-256 in CBC mode with a random IV.

    The IV is prepended to the ciphertext.

    Args:
        data: The plaintext data to encrypt.
        key: A 32-byte encryption key.

    Returns:
        The encrypted data, with the IV prepended.
    """
    if not CRYPTOGRAPHY_AVAILABLE:
        raise ImportError(
            "cryptography is not installed. Please install it with 'pip install cryptography'"
        )

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    iv = os.urandom(IV_SIZE)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ct


def _decrypt_data(data: bytes, key: bytes) -> bytes:
    """
    Decrypts data using AES-256 in CBC mode.

    Assumes the IV is prepended to the ciphertext.

    Args:
        data: The encrypted data (IV + ciphertext).
        key: A 32-byte decryption key.

    Returns:
        The decrypted plaintext data.
    """
    if not CRYPTOGRAPHY_AVAILABLE:
        raise ImportError(
            "cryptography is not installed. Please install it with 'pip install cryptography'"
        )

    if len(data) < IV_SIZE:
        raise MTDFormatError("Invalid encrypted data length.")

    iv = data[:IV_SIZE]
    ct = data[IV_SIZE:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    try:
        padded_decrypted_data = decryptor.update(ct) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted_data = unpadder.update(padded_decrypted_data) + unpadder.finalize()
    except ValueError:
        raise MTDDecryptionError(
            "Decryption failed. The key may be incorrect or the data may be corrupt."
        )
    return decrypted_data


def _compress_data(data: bytes, compression: Optional[str]) -> bytes:
    """
    Compresses data using the specified algorithm.

    Args:
        data: The data to compress.
        compression: The compression algorithm ('zstd') or None.

    Returns:
        The compressed data.
    """
    if compression is None:
        return data
    if compression == "zstd":
        if not ZSTANDARD_AVAILABLE:
            raise ImportError(
                "zstandard is not installed. Please install it with 'pip install zstandard'"
            )
        return zstd.compress(data)
    else:
        raise ValueError(f"Unknown compression algorithm: {compression}")


def _decompress_data(data: bytes, compression: Optional[str]) -> bytes:
    """
    Decompresses data using the specified algorithm.

    Args:
        data: The compressed data.
        compression: The compression algorithm ('zstd') or None.

    Returns:
        The decompressed data.
    """
    if compression is None:
        return data
    if compression == "zstd":
        if not ZSTANDARD_AVAILABLE:
            raise ImportError(
                "zstandard is not installed. Please install it with 'pip install zstandard'"
            )
        return zstd.decompress(data)
    else:
        raise ValueError(f"Unknown compression algorithm: {compression}")


def _serialize_obj(
    obj: Any, serializer: Literal["pickle", "dill"], protocol: int
) -> bytes:
    """
    Serializes a Python object into bytes.

    Args:
        obj: The object to serialize.
        serializer: The serializer to use ('pickle' or 'dill').
        protocol: The pickle protocol version.

    Returns:
        The serialized object as bytes.
    """
    if serializer == "pickle":
        return pickle.dumps(obj, protocol=protocol)
    elif serializer == "dill":
        if not DILL_AVAILABLE:
            raise ImportError(
                "dill is not installed. Please install it with 'pip install dill'"
            )
        return dill.dumps(obj, protocol=protocol)
    else:
        raise ValueError(f"Unknown serializer: {serializer}")


def _deserialize_obj(data: bytes, serializer: Literal["pickle", "dill"]) -> Any:
    """
    Deserializes bytes into a Python object.

    Args:
        data: The bytes to deserialize.
        serializer: The serializer to use ('pickle' or 'dill').

    Returns:
        The deserialized Python object.
    """
    if serializer == "pickle":
        return pickle.loads(data)
    elif serializer == "dill":
        if not DILL_AVAILABLE:
            raise ImportError(
                "dill is not installed. Please install it with 'pip install dill'"
            )
        return dill.loads(data)
    else:
        raise ValueError(f"Unknown serializer: {serializer}")


def _calculate_checksum(data: bytes) -> str:
    """
    Calculates the SHA256 checksum of the data.

    Args:
        data: The data to hash.

    Returns:
        The hex digest of the SHA256 checksum.
    """
    return hashlib.sha256(data).hexdigest()


# --- High-level API Functions ---


def save_dump(
    obj: Any,
    path: Union[str, Path],
    compression: Optional[Literal["zstd"]] = "zstd",
    protocol: int = 5,
    serializer: Literal["pickle", "dill"] = "pickle",
    passphrase: Union[None, str, bytes, Literal["auto"]] = None,
    meta: Optional[Dict[str, Any]] = None,
    env_packages: Optional[list[str]] = None,
) -> Dict[str, Union[str, Path]]:
    """
    Saves a Python object to a .mtd file with specified options.

    The dump pipeline is:
    obj -> pickle/dill -> checksum -> compress -> encrypt -> write to file

    Args:
        obj: The Python object to save.
        path: File path to save the dump to.
        compression: Compression algorithm. 'zstd' or None. Defaults to 'zstd'.
        protocol: The pickle protocol version to use. Defaults to 5.
        serializer: The serializer to use. 'pickle' or 'dill'. Defaults to 'pickle'.
        passphrase: The passphrase for encryption.
            - None: No encryption.
            - bytes: A 32-byte key for AES-256.
            - str: A base64-encoded 32-byte key.
            - 'auto': Automatically generate a secure key.
        meta: Optional dictionary of custom metadata to save in the info JSON.
        env_packages: Optional list of package import names to record in the
            environment diagnostics metadata. If None, only the Python version is
            recorded.

    Returns:
        A dictionary containing the path, checksum, and base64-encoded passphrase
        (if encryption was used) which can be used with `load_dump`.
    """
    # 1. Handle passphrase
    if passphrase == "auto":
        key = _generate_key()
        passphrase_b64 = base64.b64encode(key).decode("ascii")
    else:
        key = _prepare_key(passphrase)
        if key:
            passphrase_b64 = base64.b64encode(key).decode("ascii")
        else:
            passphrase_b64 = None

    # 2. Serialize the object
    serialized_data = _serialize_obj(obj, serializer, protocol)

    # 3. Calculate checksum
    checksum = _calculate_checksum(serialized_data)

    # 4. Compress
    compressed_data = _compress_data(serialized_data, compression)

    # 5. Encrypt
    if key:
        encrypted_data = _encrypt_data(compressed_data, key)
        is_encrypted = True
    else:
        encrypted_data = compressed_data
        is_encrypted = False

    # 6. Prepare info JSON
    info = {
        "version": 1,
        "environment": _get_environment_info(env_packages),
        "modules": _get_loaded_modules_info(),
        "dump": {
            "checksum": checksum,
            "compression": compression,
            "encrypted": is_encrypted,
            "serializer": serializer,
            "created_on": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        },
        "meta": meta or {},
    }
    info_json_bytes = json.dumps(info, indent=2).encode("utf-8")

    # 7. Write to file
    with open(path, "wb") as f:
        f.write(MAGIC_NUMBER)
        f.write(struct.pack(INFO_LEN_FORMAT, len(info_json_bytes)))
        f.write(info_json_bytes)
        f.write(struct.pack(PAYLOAD_LEN_FORMAT, len(encrypted_data)))
        f.write(encrypted_data)

    # 8. Return result dict
    result = {"path": path, "checksum": checksum}
    if passphrase_b64:
        result["passphrase"] = passphrase_b64
    return result


def load_dump(
    path: Union[str, Path],
    passphrase: Union[None, str, bytes] = None,
    checksum: Optional[str] = None,
    return_info: bool = False,
    storage_options: Optional[Dict[str, str]] = None,
) -> Union[Any, tuple[Any, dict]]:
    """
    Loads a Python object from a .mtd file.

    The load pipeline is:
    read from file -> decrypt -> decompress -> verify checksum -> unpickle/undill -> obj

    Args:
        path: File path or URL to load the dump from.
        passphrase: The passphrase for decryption. Should match the one used
                    for saving. Can be None, bytes (32-byte key), or str
                    (base64-encoded key).
        checksum: Optional SHA256 checksum (hex digest) to verify the integrity
                  of the data. If not provided, the checksum from the info
                  will be used. If provided, it overrides the one in the info.
        return_info: If True, returns a tuple of (object, info).
                     Otherwise, returns only the object.
        storage_options: A dictionary of options to use when loading from a URL.
                         These are passed as headers to the request.

    Returns:
        The loaded Python object, or a tuple of (object, info) if
        `return_info` is True. The `info` includes environment diagnostics
        (Python version, versions for requested packages, and versions of
        currently imported installed modules).
    """
    # 1. Read the raw data from path or URL
    if isinstance(path, str) and (
        path.startswith("http://") or path.startswith("https://")
    ):
        req = Request(path, headers=storage_options or {})
        with urlopen(req) as response:
            f = io.BytesIO(response.read())
    else:
        f = open(path, "rb")

    with f:
        # 2. Parse the header
        magic = f.read(len(MAGIC_NUMBER))
        if magic != MAGIC_NUMBER:
            raise MTDFormatError("Not a valid .mtd file.")

        info_len_bytes = f.read(struct.calcsize(INFO_LEN_FORMAT))
        info_len = struct.unpack(INFO_LEN_FORMAT, info_len_bytes)[0]
        info_json_bytes = f.read(info_len)
        info = json.loads(info_json_bytes.decode("utf-8"))

        payload_len_bytes = f.read(struct.calcsize(PAYLOAD_LEN_FORMAT))
        payload_len = struct.unpack(PAYLOAD_LEN_FORMAT, payload_len_bytes)[0]
        encrypted_data = f.read(payload_len)

    # 3. Prepare for decryption
    dump_info = info["dump"]
    is_encrypted = dump_info["encrypted"]
    key = _prepare_key(passphrase)

    if is_encrypted and not key:
        raise MTDDecryptionError("File is encrypted, but no passphrase was provided.")
    if not is_encrypted and key:
        # For now, just a note. Could be a warning later.
        pass

    # 4. Decrypt
    if is_encrypted:
        compressed_data = _decrypt_data(encrypted_data, key)
    else:
        compressed_data = encrypted_data

    # 5. Decompress
    compression = dump_info["compression"]
    serialized_data = _decompress_data(compressed_data, compression)

    # 6. Verify checksum
    checksum_to_verify = checksum or dump_info["checksum"]
    actual_checksum = _calculate_checksum(serialized_data)
    if actual_checksum != checksum_to_verify:
        raise MTDChecksumError(
            f"Checksum mismatch: expected {checksum_to_verify}, got {actual_checksum}"
        )

    # 7. Deserialize
    serializer = dump_info["serializer"]
    obj = _deserialize_obj(serialized_data, serializer)

    if return_info:
        return obj, info
    else:
        return obj
