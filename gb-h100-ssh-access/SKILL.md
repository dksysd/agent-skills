---
name: gb-h100-ssh-access
description: Prepare SSH access for the Gyeongbuk super-scale AI cloud farm H100 environment. Use when a user asks how to connect by SSH, configure VSCode or another IDE over SSH, use a4ai.pem, set ProxyCommand, connect through 210.91.154.131:20080, or troubleshoot the "경북 초거대 AI 클라우드 팜" remote access command.
---

# GB H100 SSH Access

## Required Values

Collect or identify these values before producing a final command:

- `a4ai.pem` absolute path: downloaded SSH permission key.
- Development environment IP address: shown in the cloud dashboard.
- Bastion endpoint: `a4ai@210.91.154.131` on port `20080`.
- Target user: `root`.

SSH means Secure Shell, a secure terminal connection protocol. `ProxyCommand` tells SSH to reach the target environment through the bastion endpoint.

## Direct SSH

Use this command shape:

```bash
ssh -o ProxyCommand="ssh -i {absolute-path-to-a4ai.pem} -p 20080 -W %h:%p a4ai@210.91.154.131" root@{development-environment-ip}
```

Replace both placeholders. The key path must be absolute.

## IDE SSH Config

For VSCode or another IDE, add this to the user's SSH config file. On Windows the usual path is `C:\Users\<username>\.ssh\config`; on Linux or macOS it is usually `~/.ssh/config`.

```text
Host {development-environment-ip}
    HostName {development-environment-ip}
    ProxyCommand ssh -i {absolute-path-to-a4ai.pem} -p 20080 -W %h:%p a4ai@210.91.154.131
    User root
```

Then connect with:

```bash
ssh root@{development-environment-ip}
```

Read `references/ssh-access.md` when preparing user-facing setup instructions or troubleshooting common SSH failures.
