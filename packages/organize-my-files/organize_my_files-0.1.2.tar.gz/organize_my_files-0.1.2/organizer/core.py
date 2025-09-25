"""Core logic for organizing files by extension."""
from pathlib import Path
from typing import Dict, Iterable, Optional
import shutil

# Default groups: mapping folder name -> set of extensions (lowercase, without dot)
DEFAULT_GROUPS: Dict[str, set] = {
    "Images": {"jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg"},
    "Documents": {"pdf", "doc", "docx", "txt", "odt", "rtf", "md"},
    "Archives": {"zip", "tar", "gz", "bz2", "7z", "rar"},
    "Audio": {"mp3", "wav", "aac", "flac", "ogg", "m4a"},
    "Video": {"mp4", "mkv", "avi", "mov", "wmv", "flv"},
    "Code": {"py", "js", "ts", "java", "c", "cpp", "cs", "go", "rb", "rs"},
}


def _ext_of(path: Path) -> Optional[str]:
    if not path.is_file():
        return None
    suf = path.suffix.lower()
    if not suf:
        return ""
    return suf.lstrip('.')


def classify_extension(ext: str, groups: Dict[str, Iterable[str]]) -> Optional[str]:
    """Return group name for an extension or None for no match.

    ext may be empty string to indicate files without extension.
    """
    for group, exts in groups.items():
        if ext in exts:
            return group
    return None


def organize(
    target: Path,
    groups: Optional[Dict[str, Iterable[str]]] = None,
    dry_run: bool = False,
    move: bool = True,
    overwrite: bool = False,
    recursive: bool = False,
    pattern: Optional[str] = None,
):
    """Organize files in `target` into subfolders by extension groups.

    Args:
      target: directory to organize (non-recursive).
      groups: mapping folder name -> iterable of extensions (lowercase, no dot).
      dry_run: if True, don't perform filesystem writes; only return planned moves.
      move: if True move files; otherwise copy files.
      overwrite: if True overwrite destination if exists.

    Returns:
      A list of tuples (src: Path, dst: Path, action: 'move'|'copy'|'skip').
    """
    if groups is None:
        groups = DEFAULT_GROUPS

    if not target.exists():
        raise FileNotFoundError(target)
    if not target.is_dir():
        raise NotADirectoryError(target)

    results = []
    # Build set of top-level folder names to skip when recursing (avoid re-processing grouped folders)
    group_names = set(groups.keys()) if groups is not None else set(DEFAULT_GROUPS.keys())
    # Also include all configured extension names as possible folder names, and the NoExt fallback
    all_exts = set()
    for exts in (groups or DEFAULT_GROUPS).values():
        all_exts.update(exts)
    group_names.update(all_exts)
    group_names.add("NoExt")

    if recursive:
        iterator = (p for p in target.rglob("*") if p.is_file())
    else:
        iterator = (p for p in target.iterdir() if p.is_file())

    if pattern:
        # convert a glob-like pattern into a filter
        def match_pattern(p: Path) -> bool:
            return p.match(pattern)
        iterator = (p for p in iterator if match_pattern(p))

    for child in iterator:
        # skip files already inside a top-level group folder
        try:
            rel = child.relative_to(target)
            if rel.parts:
                first = rel.parts[0]
                # only skip if the first part is an actual directory inside target
                if (target / first).is_dir() and first in group_names:
                    continue
        except Exception:
            # if relative_to fails for any reason, just continue processing
            pass
        ext = _ext_of(child)
        if ext is None:
            continue
        group = classify_extension(ext, groups)
        if group is None:
            # fallback to extension-named folder, or a 'NoExt' folder
            group = ext if ext else "NoExt"

        dest_dir = target / group
        dest_dir_exists = dest_dir.exists()
        dest = dest_dir / child.name

        if not dry_run:
            if not dest_dir_exists:
                dest_dir.mkdir(parents=True, exist_ok=True)

        if dest.exists():
            if overwrite:
                action = "move" if move else "copy"
            else:
                results.append((child, dest, "skip"))
                continue
        else:
            action = "move" if move else "copy"

        results.append((child, dest, action))

        if not dry_run:
            if action == "move":
                if overwrite and dest.exists():
                    dest.unlink()
                shutil.move(str(child), str(dest))
            elif action == "copy":
                if overwrite and dest.exists():
                    dest.unlink()
                shutil.copy2(str(child), str(dest))

    return results
