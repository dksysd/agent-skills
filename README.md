# agent-skills

이 repo는 Codex, Claude Code, 기타 AI coding agent가 읽을 수 있는 공용 skill 모음입니다.

각 skill은 폴더 하나로 구성되며, 핵심 지침은 `SKILL.md`에 담겨 있습니다. agent는 사용자의 요청 맥락이 skill의 `description`과 맞을 때 해당 skill을 자동으로 불러와 그 지침에 따라 동작합니다.

## 스킬 목록

| 스킬 | 한 줄 요약 |
| --- | --- |
| [`audience-aware-docs`](#audience-aware-docs) | 개발자·비개발자가 함께 읽는 문서를 쉽게 쓰고 다듬기 |
| [`experiment-log-docs`](#experiment-log-docs) | 재현 가능한 실험 기록 문서를 일관된 구조로 작성 |
| [`gb-h100-cloud-workspace`](#gb-h100-cloud-workspace) | 경북 초거대 AI 클라우드 팜(H100)에서 프로젝트·저장소 안전 운영 |
| [`gb-h100-ssh-access`](#gb-h100-ssh-access) | 경북 H100 환경 SSH 접속·IDE 원격 연결 설정 |
| [`shared-skill-management`](#shared-skill-management) | Codex와 Claude Code가 공유하는 skill 관리·검증 |

---

### audience-aware-docs

**무엇을 하나** — 개발자와 비개발자가 동시에 읽을 수 있는 Markdown 문서(보고서, 런북, README, 실험 요약, 인수인계 문서 등)를 작성·편집·재구성합니다. 약어는 처음 나올 때 풀어서 설명하고, 어려운 개념은 "무엇인지 / 왜 중요한지 / 사용자가 할 일"을 함께 적어 누구나 이해할 수 있게 만듭니다.

**언제 쓰나** — 문서를 새로 쓰거나, 표현을 더 명확하게 다듬거나, 보고서를 비전문가도 읽을 수 있게 만들고 싶을 때.

---

### experiment-log-docs

**무엇을 하나** — 재현 가능한 실험 요약 문서를 일관된 구조(목적 → 기준 상태(baseline) → 방법 → 결과 → 판단 → 다음 행동)로 작성·검토·재구성합니다. 모델 평가, 검증 실행, 벤치마크, 실패 분석, Git 상태 점검 등을 나중에 누구든 똑같이 따라 할 수 있는 형태로 남깁니다.

**언제 쓰나** — 실험·검증 결과를 기록하거나, 작업 요약을 표준 양식으로 정리하고 싶을 때.

**포함 파일** — `assets/experiment-template.md`(빈 템플릿), `assets/example-experiment.md`(작성 예시).

---

### gb-h100-cloud-workspace

**무엇을 하나** — 경북 초거대 AI 클라우드 팜의 H100 환경에서 프로젝트를 안전하게 만들고 운영하기 위한 규칙을 적용합니다. 핵심은 저장소 선택입니다 — 활성 소스 코드·가상환경·빌드처럼 작은 파일이 많은 작업은 `/root/<project>` 로컬 저장소에, 데이터셋·체크포인트·최종 산출물 같은 영구 보존물은 `/root/project`(NFS, 네트워크 마운트 저장소)에 둡니다. Pod의 로컬 저장소는 휘발성이라 잘못 두면 데이터가 사라질 수 있어 이 구분이 중요합니다.

**언제 쓰나** — 이 환경에서 프로젝트를 생성·복제·빌드·학습·평가·정리할 때, 또는 로컬과 NFS 중 어디에 둘지 판단할 때.

**포함 파일** — `references/storage-and-documentation.md`(저장 규칙·문서화 상세), `scripts/init_h100_project.py`(프로젝트 초기화 스크립트).

---

### gb-h100-ssh-access

**무엇을 하나** — 경북 H100 환경에 SSH로 접속하기 위한 설정을 준비합니다. `a4ai.pem` 키 사용, 게이트웨이(`210.91.154.131:20080`)를 거치는 `ProxyCommand` 구성, VSCode 등 IDE의 원격 연결 설정, 접속 오류 진단을 다룹니다.

**언제 쓰나** — SSH 접속 방법을 묻거나, IDE 원격 개발 환경을 세팅하거나, 접속이 안 될 때 원인을 찾고 싶을 때.

**포함 파일** — `references/ssh-access.md`(접속 설정·문제 해결 상세).

---

### shared-skill-management

**무엇을 하나** — Codex와 Claude Code가 하나의 `SKILL.md`를 공유하도록 skill을 만들고, 연결하고, 검증하고, 문제를 해결합니다. skill이 어디에 위치해야 하는지, symbolic link로 공유하는 방법, agent가 skill을 자동으로 불러오는지 확인하는 방법 등을 다룹니다.

**언제 쓰나** — 공용 skill을 새로 만들거나 수정할 때, 두 도구 간 공유 구조를 잡거나 자동 호출이 되는지 점검할 때.

---

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
