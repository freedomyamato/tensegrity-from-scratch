# Lesson 34: Data quality and calibration

[Course contents](../../../../COURSE.md) · Phase 08: Sensors, controls and AI

## Objective

Fit and independently check a simple calibration.

**Prerequisite:** Lesson 33; or demonstrate its evidence check.

**Planning time:** approximately 240 minutes including practice and recording. Split into short sessions as needed.

## Concept

Calibration relates a reading to known reference values over a stated range. A two-point line can estimate offset and slope; extra independent points test its adequacy. Keep raw readings, units, timestamp and calibration version. Missing data is not zero and should not be silently replaced by a plausible value.

![Supporting diagram for this phase](../../../../assets/learning-loop.svg)

## Worked example

A hypothetical gauge gives 10 counts at 0 N and 210 counts at 1 N. F=(counts−10)/200 N. An independent 0.5 N check should read 110 counts ideally. If it reads 118, the prediction is 0.54 N, an error of 0.04 N.

## Materials and setup

Paper calibration data or an appropriate low-force sensor and reference; no unverified force application needed.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Calculate the slope and offset from the two reference points.
2. Predict the third point before revealing its example reading.
3. Compute the independent check error.
4. Set a course-specific acceptable error based on the intended measurement, not a universal threshold.
5. Log calibration range, version and missing-data handling.

## Expected behavior and interpretation

The record distinguishes fitted points from independent checks.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

A high-precision fit to two points says nothing about hysteresis, drift or nonlinear behavior outside that range.

## Teach-back quiz

1. What is the example slope in counts/N?
2. Is a fitted point an independent check?
3. What should missing data become?

[Facilitator answer key](../../../../assessments/phase-08-answers.md) — attempt the questions first.

## Evidence to submit

Calibration equation, independent error and metadata record.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
