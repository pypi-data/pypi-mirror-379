"""Package CLI for the organizer."""
from pathlib import Path
import argparse
import json
from typing import Dict

from .core import organize, DEFAULT_GROUPS

try:
    import tomllib  # Python 3.11+
except Exception:
    try:
        import tomli as tomllib  # fallback for older Pythons (tomli provides same API)
    except Exception:
        tomllib = None


def build_parser():
    p = argparse.ArgumentParser(prog="file-organizer")
    p.add_argument("target", nargs="?", default='.', help="Target directory to organize")
    p.add_argument("--dry-run", action="store_true", help="Show actions without performing them")
    p.add_argument("--copy", action="store_true", help="Copy files instead of moving")
    p.add_argument("--overwrite", action="store_true", help="Overwrite existing files in destination")
    p.add_argument("--recursive", action="store_true", help="Operate recursively on subdirectories")
    p.add_argument("--config", type=str, help="Path to JSON or TOML file that defines groups mapping")
    p.add_argument("--verbose", action="store_true", help="Show more verbose output and a summary")
    p.add_argument("--pattern", type=str, help="Only process files matching this glob pattern (e.g. '*.txt')")
    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    target = Path(args.target).resolve()

    groups = DEFAULT_GROUPS
    if args.config:
        cfg_path = Path(args.config)
        if not cfg_path.exists():
            raise FileNotFoundError(cfg_path)
        if cfg_path.suffix.lower() in (".toml",) and tomllib is None:
            raise RuntimeError("TOML config requires Python >=3.11 or tomllib support")

        with cfg_path.open("rb") as fh:
            if cfg_path.suffix.lower() in (".toml",):
                groups = tomllib.load(fh)
            else:
                # treat as JSON/text
                groups = json.load(fh)

    # normalize group mappings: values -> set of lowercased extension names without dot
    def normalize(groups_obj) -> Dict[str, set]:
        out = {}
        for k, v in groups_obj.items():
            if isinstance(v, str):
                exts = [v]
            else:
                exts = list(v)
            out[k] = set(e.lower().lstrip('.') for e in exts)
        return out

    groups = normalize(groups)

    actions = organize(
        target,
        groups=groups,
        dry_run=args.dry_run,
        move=not args.copy,
        overwrite=args.overwrite,
        recursive=args.recursive,
        pattern=args.pattern,
    )

    counts = {"move": 0, "copy": 0, "skip": 0}
    for src, dst, action in actions:
        print(f"{action.upper():6} {src.name} -> {dst.relative_to(target)}")
        counts[action] = counts.get(action, 0) + 1

    if args.verbose:
        total = sum(counts.values())
        print()
        print(f"Processed: {total} files")
        for k, v in counts.items():
            print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
