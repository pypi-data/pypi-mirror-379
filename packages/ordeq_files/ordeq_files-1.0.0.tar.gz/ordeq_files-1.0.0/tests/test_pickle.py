import pickle
from collections.abc import Callable
from pathlib import Path

import pytest
from cloudpathlib import CloudPath
from minio.helpers import ObjectWriteResult
from ordeq_files import Pickle
from urllib3 import BaseHTTPResponse


class TestPickleLocal:
    def test_it_loads(self, tmp_path: Path):
        data = "some_data_to_load"
        path = tmp_path / "test_it_loads.pkl"
        with path.open(mode="wb") as fh:
            # noinspection PyTypeChecker
            pickle.dump(data, fh)
        assert Pickle(path=path).load() == data

    def test_it_saves(self, tmp_path: Path):
        data = "some_data_to_save"
        path = tmp_path / "test_it_saves.pkl"
        Pickle(path=path).save(data)
        with path.open(mode="br") as fh:
            assert pickle.load(fh) == data


class TestPickleMinio:
    @pytest.mark.docker
    def test_it_loads(
        self,
        minio_put_object: Callable[[str, bytes], ObjectWriteResult],
        minio_cloudpath: Callable[[str], CloudPath],
    ):
        key = "TestPickleMinio/test_it_loads.pkl"
        data = {"someKey": "someValue"}
        minio_put_object(key, pickle.dumps(data))
        assert Pickle(path=minio_cloudpath(key)).load() == data

    @pytest.mark.docker
    def test_it_saves(
        self,
        minio_cloudpath: Callable[[str], CloudPath],
        minio_get_object: Callable[[str], BaseHTTPResponse],
    ):
        key = "TestPickleMinio/test_it_saves.pkl"
        data = {"someKey": "someValue"}
        Pickle(path=minio_cloudpath(key)).save(data)
        assert pickle.loads(minio_get_object(key).read()) == data
