# Lesson 24: Sensitivity and physical validation

[Course contents](../../../../COURSE.md) · Phase 05: Form-finding and digital models

## Objective

Compare measured geometry with predictions and diagnose discrepancies.

**Prerequisite:** Lesson 23; or demonstrate its evidence check.

**Planning time:** approximately 300 minutes including practice and recording. Split into short sessions as needed.

## Concept

Sensitivity asks how much an output changes when an input changes. Validation compares a model with independent physical observations; verification checks correct implementation of its equations. A code test can verify ring length, but it does not validate a real joint. Separate numerical tolerances from instrument uncertainty.

![Supporting diagram for this phase](../../../../assets/prism.svg)

## Worked example

An ideal ring span is 138.56 mm; a measured one is 141 mm. Absolute difference is 2.44 mm and relative difference is about 1.76%. A knot-center definition, stretching or radius mismatch may explain it. A small force residual does not remove these differences.

## Materials and setup

Default digital geometry, physical model or provided illustrative measurement table, ruler.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Change radius by +1% and predict ring length change.
2. Run the geometry and verify that proportional change.
3. Measure three spans of a physical model, or explicitly use synthetic values.
4. Compute absolute and relative differences from prediction.
5. Choose one plausible cause and a measurement that could discriminate it.

## Expected behavior and interpretation

The geometry response is predictable; physical agreement depends on actual dimensions and assumptions.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

Never label synthetic comparison data as experimental validation. Do not tune all inputs until agreement and then call it independent validation.

## Teach-back quiz

1. What is verification?
2. What is validation?
3. What is the example relative difference?

[Facilitator answer key](../../../../assessments/phase-05-answers.md) — attempt the questions first.

## Evidence to submit

Sensitivity result and measured/predicted error table.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
