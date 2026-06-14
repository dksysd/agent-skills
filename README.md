# agent-skills

이 repo는 Codex, Claude Code, 기타 AI coding agent가 읽을 수 있는 공용 skill 모음입니다.

## 설치 위치

Codex:
~/.agents/skills/<skill-name>

Claude Code:
~/.claude/skills/<skill-name>

## 설치 방식

원하는 skill 폴더를 위 경로에 복사하거나 symbolic link로 연결하세요.

예:

ln -s /path/to/shared-agent-skills/gb-h100-cloud-workspace ~/.agents/skills/gb-h100-cloud-workspace

ln -s /path/to/shared-agent-skills/gb-h100-cloud-workspace ~/.claude/skills/gb-h100-cloud-workspace
