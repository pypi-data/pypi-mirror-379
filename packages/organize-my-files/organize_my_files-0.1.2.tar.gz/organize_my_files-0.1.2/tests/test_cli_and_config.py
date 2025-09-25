import json
from pathlib import Path
from organizer.core import organize


def touch(p: Path, content: bytes = b"x"):
    p.write_bytes(content)
    return p


def test_recursive_and_pattern(tmp_path):
    # create nested files
    (tmp_path / "a.txt").write_text("hello")
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "b.txt").write_text("b")
    (sub / "c.jpg").write_text("c")

    # pattern to only match txt files
    actions = organize(tmp_path, dry_run=True, recursive=True, pattern="*.txt")
    # should match a.txt and sub/b.txt -> 2 actions
    assert len(actions) == 2


def test_config_loading_json(tmp_path):
    # create files and a small JSON config mapping .xyz to Custom
    (tmp_path / "file.xyz").write_text("x")
    cfg = {"Custom": ["xyz"]}
    # place config outside the target folder so it won't be processed
    cfg_path = tmp_path.parent / "groups.json"
    cfg_path.write_text(json.dumps(cfg))

    actions = organize(tmp_path, groups={k: set(v) for k, v in cfg.items()}, dry_run=True)
    assert len(actions) == 1
    src, dst, action = actions[0]
    assert dst.parts[-2] == "Custom"
