# Tensegrity Teaching Assistant v0.1

An original teaching plugin inspired by the organization of Anthropic's knowledge-work-plugins. No Anthropic plugin content is copied and this is not an Anthropic-endorsed product.

## Install in Claude Code
After this branch is merged into main:
```bash
claude plugin marketplace add freedomyamato/tensegrity-from-scratch
claude plugin install tensegrity-teaching@tensegrity-learning-plugins
```
Before merge, download or check out this branch and run from the repository root:
```bash
claude --plugin-dir ./plugins/tensegrity-teaching
```
Use the local-plugin route only in a Claude Code installation supporting that option. In Cowork, custom-plugin availability depends on the installed product and workspace configuration; this package has not been installed there during development.

## Commands
- `/tensegrity-teaching:lesson-plan beginner tension and compression, 60 minutes, English`
- `/tensegrity-teaching:build-coach tabletop prism, beginner, pre-cut materials`
- `/tensegrity-teaching:quiz phase 01, five questions, Chinese, live mode`
- `/tensegrity-teaching:progress-review L01 identified cables correctly with visual prompts; no assembly evidence`
- `/tensegrity-teaching:adapt-lesson quiet environment, large-print task cards, no forced touch`
- `/tensegrity-teaching:experiment-plan compare joint drift over ten minutes, no added load`

The reusable skill has also been prepared for ChatGPT Skills. In ChatGPT, use natural language; Claude slash commands are specific to the Claude plugin.

## Scope
Works with host-model capabilities and supplied evidence. No external accounts, API keys or MCP servers are required by this plugin. No connectors, student database, autonomous messaging, structural certification or mobile-app AI backend are included. Progress tracking is manual unless a separately authorized integration is supplied. The existing mobile course is not changed by this addition.

## Customize
Edit the teaching-playbook to match instructor formats, course-map to match curriculum changes, and glossary to match language preferences. Keep public examples anonymous. Run `python3 plugins/tensegrity-teaching/scripts/validate_plugin.py` from the repository root before distributing edits.

See `examples/beginner-lesson.md` for a ready-to-use session and `examples/quiz-and-progress.md` for grading examples. Validation here checks files and teaching examples; live Claude/Cowork behavior still needs a user pilot.
