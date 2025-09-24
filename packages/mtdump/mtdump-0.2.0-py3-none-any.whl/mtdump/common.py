import importlib
import importlib.metadata
import sys
from typing import Dict, Optional


class MTDError(Exception):
    """Base exception for all mtdump errors."""

    pass


class MTDFormatError(MTDError):
    """Raised for errors related to the .mtd file format."""

    pass


class MTDChecksumError(MTDError):
    """Raised when a checksum verification fails."""

    pass


class MTDDecryptionError(MTDError):
    """Raised when decryption fails, possibly due to an incorrect key."""

    pass


def _get_environment_info(
    packages: Optional[list[str]] = None,
) -> Dict[str, Optional[str]]:
    """
    Collects versions for Python and optionally specified packages.

    Args:
        packages: Optional list of package import names to include. If None,
                  only the Python version is recorded.

    Returns:
        A mapping from name to version string, or None if not installed.
        Intended for environment diagnostics to help debug loading issues and
        verify compatibility.
    """
    requested = packages or []
    env_info = {"python": sys.version}

    for pkg in requested:
        try:
            lib = importlib.import_module(pkg)
            version = getattr(lib, "__version__", None)
            if pkg == "sklearn":
                env_info["scikit-learn"] = version
            else:
                env_info[pkg] = version
        except ImportError:
            if pkg == "sklearn":
                env_info["scikit-learn"] = None
            else:
                env_info[pkg] = None

    return env_info


def _get_loaded_modules_info() -> Dict[str, Optional[str]]:
    """
    Gathers versions of all currently imported, non-internal, top-level modules.
    This provides a snapshot of the runtime environment for diagnostics,
    excluding Python's built-in and standard library modules.
    """
    top_level_modules = sorted(
        list(set(m.split(".")[0] for m in sys.modules if not m.startswith("_")))
    )

    versions = {}
    for module_name in top_level_modules:
        try:
            # This will succeed for installed packages and raise PackageNotFoundError
            # for standard library or built-in modules, effectively filtering them.
            version = importlib.metadata.version(module_name)
            versions[module_name] = version
        except importlib.metadata.PackageNotFoundError:
            # This module is not an installed package, so we skip it.
            continue
    return versions
