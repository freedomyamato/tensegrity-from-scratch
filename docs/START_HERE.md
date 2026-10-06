# Getting started

## Choose your first session

You need paper, a ruler and a way to save observations. A computer is optional for the beginning. Read [lesson 01](../phases/00-orientation/01-goals-and-placement/docs/en.md), choose a route, then prepare a kit in lesson 02. If no physical kit is available, start with drawings and worked examples and mark physical evidence as pending.

Keep the finished target modest: a labeled tabletop prism you can rebuild, explain and measure. Solar panels and motors come later. A dummy panel made of light card is sufficient for the first application prototype.

## A manageable routine

For each session: five minutes recalling the last result; ten minutes observing the new problem; a short explanation and worked example; making/calculation time; then a teach-back and notebook entry. Split long lessons into multiple sessions. Approximately six hours a week completes the full 180-hour plan in thirty weeks, but this is an estimate and there is no deadline.

Complete a lesson when its evidence exists and each applicable rubric dimension is at least level 2. You can answer through a sketch, demonstration, speech or another suitable form. Do not remove useful support simply to appear independent.

## Computer route

Extract the repository, open a terminal in its root and run:

```bash
python3 --version
python3 -m tensegrity prism
```

Expected result: a JSON geometry with six nodes, twelve members, nullspace dimension one and a tiny equilibrium residual. It also writes `outputs/prism.json`. The output proves mathematical equilibrium for the ideal state; it does not prove the physical model’s capacity.

If Python is unavailable, read the example calculations. On Windows use `py -3` if that is your Python launcher. Do not install unknown packages; this course has no runtime package dependencies.

## Reading on a phone

The Markdown lessons can be read on GitHub after publication. The offline reader can be opened on a computer after extraction. Some mobile file managers do not open local HTML reliably; use the Markdown files or transfer the extracted folder to a computer. Preserve the folder structure so linked diagrams and worksheets remain available.

## First twelve weeks

Weeks 1–2: setup and force intuition. Weeks 3–4: topology, prism making and repeatability. Weeks 5–6: units, diagrams and balance. Weeks 7–8: material and joint behavior. Weeks 9–11: digital geometry, equilibrium and measured comparison. Week 12: a short demonstration and review. Repeat a block when evidence is missing. This covers the beginning of the course, not all 48 lessons.

Next: [Course contents](../COURSE.md) · [Learning paths](../learning-paths/README.md).
