# Lesson 17: Cable stiffness and stretch

[Course contents](../../../../COURSE.md) · Phase 04: Materials and failure

## Objective

Estimate a local stiffness from a small force–extension record.

**Prerequisite:** Lesson 16; or demonstrate its evidence check.

**Planning time:** approximately 240 minutes including practice and recording. Split into short sessions as needed.

## Concept

For a locally linear axial member, stiffness k≈ΔF/ΔL in N/m. For a homogeneous ideal member k=EA/L, where E is elastic modulus, A is area and L is reference length. Real cord, knots and elastic bands may show nonlinear response and hysteresis. Distinguish stiffness from strength and from prestress.

![Supporting diagram for this phase](../../../../assets/prism.svg)

## Worked example

An illustrative sample extends 2 mm at 0.2 N and 4 mm at 0.4 N. The slope over that interval is (0.4−0.2)/(0.004−0.002)=100 N/m. This is a local estimate, not a breaking-load rating.

## Materials and setup

Illustrative dataset examples/cable_extension.csv; optional small supervised test with a low-force spring scale and contained tray.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Plot force against extension from the sample dataset.
2. Calculate the slope over two intervals.
3. Predict force at 3 mm extension under the local linear assumption.
4. If testing a real sample, use small increments and stop on slip or damage.
5. Record loading and unloading separately and compare with the ideal law.

## Runnable lab

From the repository root (the folder containing README.md):

```bash
python3 -m tensegrity spring
```

See the [lab guide](../../../../labs/README.md) for expected output and parameter changes. Compare one output with a calculation before interpreting the result. If you cannot run Python, use the worked example and label the task as a manual exercise.

## Expected behavior and interpretation

The synthetic linear data yields 100 N/m; real samples may show differing slopes and hysteresis.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

Do not extrapolate a low-load slope to failure or substitute knot movement for material extension.

## Teach-back quiz

1. What are stiffness units?
2. Is stiffness the same as strength?
3. What force is predicted at 3 mm?

[Facilitator answer key](../../../../assessments/phase-04-answers.md) — attempt the questions first.

## Evidence to submit

A force–extension plot/table and scope of the stiffness estimate.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
