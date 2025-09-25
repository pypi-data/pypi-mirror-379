from pathlib import Path

from ordeq_files import Bytes


def test_it_loads(tmp_path: Path):
    path = tmp_path / "test_it_loads"
    data = b"somethingToLoad"
    with path.open(mode="wb") as fh:
        fh.write(data)
    assert Bytes(path=path).load() == data


def test_it_saves(tmp_path: Path):
    path = tmp_path / "test_it_saves"
    data = b"somethingToSave"
    Bytes(path=path).save(data)
    with path.open(mode="rb") as fh:
        assert fh.read() == data
