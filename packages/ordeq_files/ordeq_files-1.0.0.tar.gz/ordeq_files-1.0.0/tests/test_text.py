from ordeq_files import Text


def test_text(tmp_path):
    dataset = Text(path=tmp_path / "hello.txt")
    dataset.save("hello")

    assert (tmp_path / "hello.txt").read_text() == "hello"

    (tmp_path / "world.txt").write_text("world")
    dataset = Text(path=tmp_path / "world.txt")
    assert dataset.load() == "world"
