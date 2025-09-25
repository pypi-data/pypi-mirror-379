from ordeq_files import Glob


def test_glob_dataset(tmp_path):
    files = ["hello.txt", "world.txt", "foobar.parquet"]
    for file_name in files:
        (tmp_path / file_name).touch()

    dataset = Glob(path=tmp_path, pattern="*.txt")
    assert {path.name for path in dataset.load()} == {"hello.txt", "world.txt"}
