#!/usr/bin/env python3
"""Scaffold a GB H100 cloud farm project layout."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import sys
from textwrap import dedent


def valid_project_name(value: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,62}", value):
        raise argparse.ArgumentTypeError(
            "use 1-63 letters, digits, dots, underscores, or hyphens; start with a letter or digit"
        )
    if value in {".", ".."}:
        raise argparse.ArgumentTypeError("invalid project name")
    return value


def write_text(path: Path, content: str, dry_run: bool) -> None:
    if path.exists():
        return
    print(f"create file {path}")
    if not dry_run:
        path.write_text(content, encoding="utf-8")


def mkdir(path: Path, dry_run: bool) -> None:
    print(f"mkdir -p {path}")
    if not dry_run:
        path.mkdir(parents=True, exist_ok=True)


def symlink(target: Path, link: Path, force: bool, dry_run: bool) -> None:
    if link.is_symlink():
        current = Path(os.readlink(link))
        if current == target:
            print(f"keep symlink {link} -> {target}")
            return
        if not force:
            raise SystemExit(f"{link} already points to {current}; rerun with --force to replace it")
        print(f"replace symlink {link} -> {target}")
        if not dry_run:
            link.unlink()
    elif link.exists():
        if not force:
            raise SystemExit(f"{link} already exists and is not a symlink; rerun with --force only if safe")
        print(f"remove existing path {link}")
        if not dry_run:
            if link.is_dir():
                raise SystemExit(f"refusing to remove directory {link}; move it manually")
            link.unlink()
    else:
        print(f"create symlink {link} -> {target}")

    if not dry_run:
        link.symlink_to(target, target_is_directory=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_name", type=valid_project_name)
    parser.add_argument("--local-root", default="/root", type=Path)
    parser.add_argument("--nfs-root", default="/root/project", type=Path)
    parser.add_argument("--force", action="store_true", help="replace existing symlinks")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    project = args.project_name
    workspace = args.local_root / f"{project}-workspace"
    storage = args.nfs_root / "storage" / project
    checkpoints = args.nfs_root / "checkpoints" / project
    dataset = args.nfs_root / "dataset"

    for path in [
        workspace / "src",
        workspace / "configs",
        workspace / "scripts",
        workspace / "tmp",
        workspace / "cache",
        workspace / "work_outputs",
        storage / "docs",
        storage / "reports",
        storage / "logs",
        storage / "manifests",
        storage / "outputs",
        checkpoints,
        dataset,
    ]:
        mkdir(path, args.dry_run)

    symlink(storage / "outputs", workspace / "outputs", args.force, args.dry_run)
    symlink(checkpoints, workspace / "checkpoints", args.force, args.dry_run)
    symlink(dataset, workspace / "dataset", args.force, args.dry_run)

    write_text(
        storage / "README.md",
        dedent(
            f"""\
            # {project}

            Purpose: durable storage for reports, logs, manifests, and final outputs for `{project}`.

            ## Structure

            - `docs/`: durable documentation.
            - `reports/`: final reports and summaries.
            - `logs/`: logs worth preserving.
            - `manifests/`: project-level and multi-run reproducibility records.
            - `outputs/`: final or selected outputs.

            ## Notes

            Active development, dependency installs, caches, and builds should stay in `{workspace}`.
            """
        ),
        args.dry_run,
    )

    write_text(
        storage / "manifests" / "project.manifest.yaml",
        dedent(
            f"""\
            project: "{project}"
            created_at: ""
            workspace: "{workspace}"
            durable_storage: "{storage}"
            checkpoints: "{checkpoints}"
            dataset_root: "{dataset}"
            notes: "Fill in inputs, commands, code state, outputs, logs, and reproduction steps per run."
            """
        ),
        args.dry_run,
    )

    print("\nworkspace:", workspace)
    print("durable storage:", storage)
    print("checkpoints:", checkpoints)
    print("dataset root:", dataset)
    return 0


if __name__ == "__main__":
    sys.exit(main())
