# H100 SSH Access Reference

## Key Download

1. Open the cloud dashboard profile menu in the upper-right corner.
2. Choose `SSH Key 다운로드`.
3. Save the downloaded `a4ai.pem` file.

Use an absolute path to `a4ai.pem` in all commands. If SSH rejects the key on Linux or macOS, set restrictive permissions:

```bash
chmod 600 /absolute/path/to/a4ai.pem
```

## Direct SSH Template

```bash
ssh -o ProxyCommand="ssh -i {absolute-path-to-a4ai.pem} -p 20080 -W %h:%p a4ai@210.91.154.131" root@{development-environment-ip}
```

## SSH Config Template

```text
Host {development-environment-ip}
    HostName {development-environment-ip}
    ProxyCommand ssh -i {absolute-path-to-a4ai.pem} -p 20080 -W %h:%p a4ai@210.91.154.131
    User root
```

## Troubleshooting

- If `Permission denied (publickey)` appears, verify the key path, key permissions, and that `a4ai.pem` is the downloaded cloud key.
- If the target cannot be reached, verify the development environment IP in the dashboard.
- If Windows paths contain spaces, quote the key path in `ProxyCommand`.
- If using VSCode Remote SSH, edit the same SSH config file VSCode reads and then reconnect.
