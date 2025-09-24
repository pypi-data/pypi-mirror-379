import os
from pathlib import Path

import pytest

from mtdump import MTDChecksumError, load_dump, save_dump


@pytest.fixture
def sample_obj():
    return {
        "string": "hello world",
        "integer": 42,
        "float": 3.14159,
        "list": [1, 2, 3, "a", "b", "c"],
        "dict": {"nested_key": "nested_value"},
        "bytes": b"some binary data",
        "none": None,
    }


@pytest.fixture
def tmp_file(tmp_path: Path):
    return tmp_path / "test_dump.mtd"


def test_default_dump_roundtrip(sample_obj, tmp_file):
    result = save_dump(sample_obj, tmp_file)
    loaded = load_dump(tmp_file)
    assert loaded == sample_obj
    assert "checksum" in result


def test_encrypted_roundtrip(sample_obj, tmp_file):
    result = save_dump(sample_obj, tmp_file, passphrase="auto")
    assert "passphrase" in result
    loaded, info = load_dump(
        tmp_file, passphrase=result["passphrase"], return_info=True
    )
    assert loaded == sample_obj
    assert info["dump"]["encrypted"] is True


def test_dill_and_meta_and_env_packages(sample_obj, tmp_file):
    custom_meta = {"experiment_id": "exp_123", "user": "test_user"}
    save_dump(
        sample_obj,
        tmp_file,
        serializer="dill",
        meta=custom_meta,
        env_packages=["numpy", "sklearn"],
    )
    loaded, info = load_dump(tmp_file, return_info=True)
    assert loaded == sample_obj
    assert info["dump"]["serializer"] == "dill"
    assert info["meta"]["experiment_id"] == "exp_123"
    assert "python" in info["environment"]
    # presence regardless of installation state (None if missing)
    assert "numpy" in info["environment"]
    assert "scikit-learn" in info["environment"]  # normalized name


def test_checksum_failure(sample_obj, tmp_file):
    save_dump(sample_obj, tmp_file)
    with pytest.raises(MTDChecksumError):
        load_dump(tmp_file, checksum="incorrect_checksum")


def test_result_passthrough(sample_obj, tmp_file):
    result = save_dump(sample_obj, tmp_file, passphrase="auto")
    loaded = load_dump(**result)
    assert loaded == sample_obj
