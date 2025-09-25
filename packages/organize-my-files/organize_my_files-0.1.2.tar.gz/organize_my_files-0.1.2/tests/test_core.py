import tempfile
from pathlib import Path
from organizer.core import organize, DEFAULT_GROUPS


def touch(p: Path, content: bytes = b"x"):
    p.write_bytes(content)
    return p


def test_organize_moves_files(tmp_path):
    # create files with various extensions
    f1 = touch(tmp_path / "a.jpg")
    f2 = touch(tmp_path / "b.pdf")
    f3 = touch(tmp_path / "c")  # no extension

    actions = organize(tmp_path, dry_run=True)
    # dry run should list 3 actions
    assert len(actions) == 3

    # now actually run move
    actions = organize(tmp_path, dry_run=False, move=True, overwrite=True)

    # ensure files moved into expected dirs
    assert not (tmp_path / "a.jpg").exists()
    assert (tmp_path / "Images" / "a.jpg").exists()
    assert (tmp_path / "Documents" / "b.pdf").exists()
    assert (tmp_path / "NoExt" / "c").exists()
