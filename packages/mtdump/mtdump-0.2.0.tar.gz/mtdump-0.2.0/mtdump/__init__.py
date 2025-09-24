"""
Python object serialization to `.mtd` with compression, encryption, and
environment diagnostics metadata for compatibility and debugging.
"""

from ._v1 import load_dump, save_dump
from .common import MTDChecksumError, MTDDecryptionError, MTDFormatError

__all__ = [
    "save_dump",
    "load_dump",
    "MTDChecksumError",
    "MTDDecryptionError",
    "MTDFormatError",
]
