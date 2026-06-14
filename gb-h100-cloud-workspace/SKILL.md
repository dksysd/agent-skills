---
name: gb-h100-cloud-workspace
description: Operate safely in the Gyeongbuk super-scale AI cloud farm H100 environment. Use when creating, cloning, building, training, evaluating, or organizing projects on this machine; when choosing between /root local storage and /root/project NFS; when handling datasets, checkpoints, experiment outputs, caches, virtual environments, node_modules, README files, manifest.yaml files, or files.sha256.txt; and when asked about "경북 초거대 AI 클라우드 팜", H100, NFS, project workspace layout, durable experiment evidence, or storage rules.
---

# GB H100 Cloud Workspace

## Core Rule

Treat `/root` as fast but temporary local storage and `/root/project` as durable NFS-backed storage. NFS means Network File System: it persists across Pod restarts but is slow for metadata-heavy work such as dependency installs, Git scans, builds, package extraction, or many small file operations.

Use this default split:

- Active source, Git working trees, virtual environments, dependency installs, caches, build outputs, and temporary work: `/root/<project-name>-workspace`.
- Durable reports, logs, final artifacts, manifests, and recovery evidence: `/root/project/storage/<project-name>`.
- Datasets: `/root/project/dataset`.
- Model checkpoints: `/root/project/checkpoints/<project-name>`.

Before creating, extracting, cloning, or generating large files on `/root`, estimate size and decide what must be synced back to NFS. Local non-NFS storage is ephemeral and the Kubernetes Pod can be terminated if local usage exceeds the allocation.

## Standard Workflow

1. Choose a short project name and create `/root/<project-name>-workspace`.
2. Put code and metadata-heavy work inside the local workspace, not under `/root/project`.
3. Create durable NFS folders under `/root/project/storage/<project-name>` and `/root/project/checkpoints/<project-name>`.
4. Link durable folders into the workspace only for convenience:
   - `outputs -> /root/project/storage/<project-name>/outputs`
   - `checkpoints -> /root/project/checkpoints/<project-name>`
   - `dataset -> /root/project/dataset`
5. Remember that writes through a symlink land at the target. Do not write high-churn temporary files, frequent training scratch files, or large numbers of small files through an NFS symlink.
6. Keep enough information on NFS to recover: README files, manifests, final reports, logs, checkpoint metadata, and selected final outputs.
7. Periodically remove local caches, build products, package extraction folders, `__pycache__`, `.venv` copies that are no longer needed, and local temporary data subsets.

## Automation

For a new project, prefer the bundled scaffold script:

```bash
python /root/shared-agent-skills/gb-h100-cloud-workspace/scripts/init_h100_project.py <project-name>
```

Use `--dry-run` before changing the filesystem, and `--force` only when replacing existing symlinks is intentional.

## Documentation

When creating or moving durable artifacts, update documentation at the same time.

- Write a `README.md` for durable project, dataset, checkpoint, and experiment result folders.
- Write `manifest.yaml` when an artifact must be reproducible. Include input data, code location, configuration, command, created time, output paths, and environment notes.
- Use `files.sha256.txt` for large file inventories and integrity checks instead of listing every file in README. SHA-256 is a content hash used to verify whether files changed.
- If moving or deleting files, update related README and manifest files in the same change.

Read `references/storage-and-documentation.md` before creating durable project layouts, dataset folders, checkpoint folders, manifests, or file inventories.

## Avoid

- Do not create `.venv`, `node_modules`, `__pycache__`, build directories, cloned dependency trees, or package extraction trees under `/root/project`.
- Do not keep original datasets, final checkpoints, or final reports only on local `/root`.
- Do not repeatedly run broad `find`, `du`, Git scans, or extraction jobs over NFS unless the task genuinely requires it.
- Do not assume local files survive tool shutdown, Pod restart, or local storage pressure.
