---
name: experiment-log-docs
description: Create, review, or restructure reproducible experiment summary documents in Markdown. Use when the user asks to document an experiment, validation run, model evaluation, Git state audit, benchmark, failure analysis, or work summary using a consistent structure with purpose, baseline state, method, results, judgment, and next actions.
---

# Experiment Log Docs

## Overview

Use this skill to turn rough notes, command outputs, logs, or existing Markdown into a reproducible experiment record. Keep the record useful for both non-developers who need the conclusion and developers who need exact paths, commands, versions, and evidence.

## Core Structure

Prefer this structure unless the repository already has a stronger local convention:

1. Summary
2. Purpose
3. Baseline State
4. Method
5. Results
6. Judgment
7. Next Actions

Do not include a "Who" section unless the user explicitly requests ownership tracking and there is evidence for it. File state, logs, and Git metadata usually prove what happened, not who did it.

## Field Guidance

- Summary: state the one-line conclusion, status, core result, and next decision.
- Purpose: state why the experiment was run, the hypothesis, and the success criteria.
- Baseline State: capture date, repository, branch, commit, environment, input data, model or checkpoint, and comparison baseline.
- Method: include exact commands, parameters, changed settings, evaluation method, repetitions, and seed when relevant.
- Results: record observed facts, metrics, generated artifacts, log paths, failures, warnings, and anomalies.
- Judgment: separate interpretation from facts. Include what can be claimed, what cannot yet be claimed, and risks.
- Next Actions: list follow-up experiments, code or data fixes, and artifacts to preserve, delete, or clean up.

## Writing Rules

- Define abbreviations, uncommon terms, difficult concepts, and newly introduced concepts on first use.
- Keep exact technical evidence intact: paths, commands, commits, branch names, model names, metric values, filenames, and timestamps.
- Explain metric direction in plain language when using metrics. Say whether higher or lower is better.
- Use "not applicable" instead of deleting important fields when a field does not apply.
- Mark uncertain claims explicitly. Do not turn missing evidence into a conclusion.
- Prefer tables for comparing multiple runs or repositories.
- Keep "Results" factual and "Judgment" interpretive.

## Template

Use `assets/experiment-template.md` when creating a new document from scratch. Use `assets/example-experiment.md` as a style example for Git state audits or similar validation summaries.

```md
# 실험 정리: <실험명>

## 1. 요약
- 한 줄 결론:
- 상태: 성공 / 실패 / 보류 / 재실험 필요
- 핵심 결과:
- 다음 결정:

## 2. 목적
- 왜 이 실험을 했는가:
- 확인하려는 가설:
- 성공 기준:

## 3. 기준 상태
- 날짜:
- 저장소:
- 브랜치:
- 커밋:
- 실행 환경:
- 데이터셋 / 입력 경로:
- 모델 / 체크포인트:
- 비교 기준선:

## 4. 방법
- 실행 명령:
- 주요 파라미터:
- 변경한 설정:
- 평가 방식:
- 반복 횟수 / seed:

## 5. 결과
- 주요 지표:
- 생성 산출물:
- 로그 위치:
- 실패 / 경고 / 이상 징후:

## 6. 판단
- 결과 해석:
- 주장 가능한 것:
- 아직 주장하면 안 되는 것:
- 리스크:

## 7. 후속 작업
- 다음 실험:
- 보완할 데이터 / 코드:
- 정리 / 삭제 / 보존할 산출물:
```
