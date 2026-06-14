---
name: audience-aware-docs
description: Use when creating, editing, summarizing, reviewing, or restructuring Markdown, reports, runbooks, README files, experiment summaries, project notes, handoff docs, or any other documentation that may be read by both non-developers and developers. Apply when the user asks to write a document, improve clarity, explain difficult terms, make a report accessible, or prepare docs for mixed technical audiences.
---

# Audience-Aware Documentation

## Core Rule

Write every document so a non-developer can understand the purpose, conclusion, and practical meaning, while a developer can still find the exact technical details needed to reproduce, verify, or extend the work.

Do not remove technical precision to make text easier. Add orientation, definitions, and structure around the technical content.

## Default Structure

For new documents, prefer this order unless the existing document has a strong local pattern:

1. Title
2. One-paragraph plain-language summary
3. Key conclusions or decisions
4. Terms and abbreviations, if the document contains specialist vocabulary
5. Main body
6. Evidence, paths, commands, metrics, versions, or implementation details
7. Caveats, assumptions, and next steps

For existing documents, preserve the original facts, numbers, file paths, command names, and technical claims. Improve readability by adding explanations and section framing rather than rewriting away useful detail.

## Mixed-Audience Writing Rules

- Start with what the reader should know or decide, not with raw logs or tool output.
- Define difficult terms the first time they appear, or add a short "Terms" section near the top.
- Keep acronyms, but expand them once: `ASR (automatic speech recognition)`.
- Explain metrics in operational language: say whether higher or lower is better, what a positive or negative delta means, and how to interpret common ranges.
- Keep expert-facing fields such as file paths, model names, run IDs, JSON keys, command names, and exact numeric values intact.
- When a table has technical column names, add one sentence before or after the table explaining how to read it.
- Separate conclusion from evidence. Non-developers should be able to stop after the summary; developers should be able to continue into details.
- Prefer short paragraphs and direct sentences. Avoid unexplained jargon, unexplained abbreviations, and dense noun strings.
- If a document is generated from local files or experiment outputs, state the snapshot date and source paths.
- If a claim depends on incomplete evidence, say so explicitly.

## Terms Section Guidance

Add a terms section when a document includes three or more specialist terms, acronyms, internal labels, or metric names.

Use a simple two-column table:

```markdown
|Term|Plain-language meaning|
|-|-|
|WER|Word Error Rate. A word-level error rate for speech recognition; lower is better.|
```

Include internal experiment labels when they are important for reading tables. If the full meaning is not known from the document, say that it is an internal run label and explain how the reader should treat it.

## Review Checklist

Before finishing a documentation task, check:

- A non-developer can answer: What is this document about? What changed? Is the result good, bad, or inconclusive?
- A developer can answer: Where did the data come from? What exact commands, paths, files, metrics, or versions matter?
- Important acronyms and metrics are expanded or explained.
- Tables and charts have enough context to interpret directionality and meaning.
- No source facts, paths, or numeric results were changed merely for readability.

## Skill Maintenance

This skill is shared between Codex and Claude Code through symbolic links. For creating, linking, validating, or troubleshooting shared skills, use `shared-skill-management`.
