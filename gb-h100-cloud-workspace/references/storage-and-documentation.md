# H100 Storage And Documentation Reference

## Environment Facts

- vCPU: 19 logical CPUs.
- RAM: 210 GB.
- GPU: H100 NVL.
- VRAM: 94 GB.
- Local storage: dashboard allocation is 1 TB; inside the container `df` may show about 833 GiB.
- NFS storage: dashboard allocation is 2 TB at `/root/project`.

Kubernetes Pod means the running container unit. Files outside NFS can disappear when the Pod stops, the tool is disabled, or local storage pressure occurs.

## Recommended Layout

```text
/root/<project-name>-workspace/
    src/
    .venv/
    cache/
    work_outputs/
    scripts/
    configs/
    outputs -> /root/project/storage/<project-name>/outputs
    checkpoints -> /root/project/checkpoints/<project-name>
    dataset -> /root/project/dataset
```

```text
/root/project/storage/<project-name>/
    docs/
    reports/
    logs/
    manifests/
    outputs/
    README.md
```

```text
/root/project/dataset/<dataset-name>/
    README.md
    manifest.yaml
    files.sha256.txt
```

```text
/root/project/checkpoints/<project-name>/<run-name>/
    README.md
    manifest.yaml
    files.sha256.txt
```

## README Checklist

For durable folders, include:

- Purpose of the folder.
- Important subfolders and files.
- Creation or latest update time.
- Related project, experiment, run, dataset, or checkpoint name.
- What is final, temporary, or safe to delete.

For datasets, also include:

- Source and version.
- Preprocessing status.
- Sample count when known.
- File format.
- License or usage restrictions.
- Preprocessing script and configuration paths.

For checkpoints, also include:

- Model name.
- Training data.
- Training configuration.
- Save time or step.
- Evaluation result summary when available.
- Resume command or manifest path.

For experiment results, also include:

- Execution command.
- Configuration file.
- Input data.
- Output description.
- Log location.
- Reproduction steps.

## Manifest Template

Use project-specific fields when useful, but keep enough information to reproduce or audit the artifact.

```yaml
project: "<project-name>"
artifact: "<dataset|checkpoint|experiment-output|report>"
created_at: "<YYYY-MM-DD HH:MM UTC>"
created_by: "<user-or-agent>"
code:
  workspace: "/root/<project-name>-workspace"
  commit: "<git commit or unknown>"
  diff_status: "<clean|dirty|not-a-git-repo|unknown>"
inputs:
  - path: "/root/project/dataset/<dataset-name>"
    description: "<input description>"
configuration:
  files:
    - "/root/<project-name>-workspace/configs/<config>.yaml"
  notes: "<important settings>"
command: |
  <exact command used>
outputs:
  - path: "/root/project/storage/<project-name>/outputs/<run>"
    description: "<output description>"
logs:
  - "/root/project/storage/<project-name>/logs/<run>.log"
environment:
  gpu: "H100 NVL"
  vram: "94GB"
  notes: "<package versions, container notes, or unknown>"
reproduce:
  steps:
    - "<step 1>"
    - "<step 2>"
```

Store project-level or multi-experiment manifests at `/root/project/storage/<project-name>/manifests`. Store artifact-specific manifests inside that artifact's durable folder.

## files.sha256.txt

Use this format for large file inventories:

```text
<sha256-hex>  <relative-or-absolute-path>
```

Generate only when integrity matters or when listing files in README would be noisy. It can be omitted for temporary or low-value outputs.

## Dataset Shape

Prefer WebDataset-style tar shards for large sample collections when practical. WebDataset means storing many samples inside `.tar` shards, which reduces small-file pressure on NFS.
