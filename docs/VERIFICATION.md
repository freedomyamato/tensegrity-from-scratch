# Release verification — 1.0.0

Local verification performed on 6 October 2026 with Python 3.12.14.

## Numerical tests

**21 tests passed.** Coverage includes independent closed-form prism lengths; admissible analytic self-stress at several dimensions; translation/rotation invariance; nullspace agreement and scale invariance; a deliberately altered twist and damaged topology; invalid dimensions; unilateral cable behavior; Euler length/end-condition scaling; undamped cosine and energy checks; damped energy decay; known solar-energy integrals; bad/duplicate readings; and controller step/boundary/nonfinite checks.

Command: `python3 -m unittest discover -s tests -v`.

## Course and command checks

All 48 lesson documents and worksheets, twelve phase guides and 24 assessment documents pass the content/link checker. The machine-readable routes, SVG assets, reader IDs and local reader links are checked. All seven lab commands ran successfully, including a slack-cable case. The local progress helper accepted an existing artifact as **recorded, not graded**. Reader JavaScript passed Node syntax checking.

The course generator rebuilds committed course documents and the reader deterministically. The release ZIP is checked for integrity and excludes generated output, private learner records, caches and local Git history.

## What was not verified

No physical prism was assembled for this release. No material properties, load capacity, stability proof, full-scale roof or floating system, electrical installation, actuator hardware, classroom timings, learner outcomes or accessibility effectiveness were validated. The offline reader was checked structurally and its script syntax checked, but was not interactively tested in a real browser during this release.

The GitHub Actions workflow is included. See the repository's Actions tab for hosted-run results; the local checks described above remain distinct from that status. Source repository: https://github.com/freedomyamato/tensegrity-from-scratch.

These distinctions are intentional: software verification is useful evidence and does not substitute for physical or classroom validation.
