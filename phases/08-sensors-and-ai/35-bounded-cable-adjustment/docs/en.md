# Lesson 35: Bounded cable adjustment

[Course contents](../../../../COURSE.md) · Phase 08: Sensors, controls and AI

## Objective

Inspect a simulated feedback rule before considering hardware.

**Prerequisite:** Lesson 34; or demonstrate its evidence check.

**Planning time:** approximately 240 minutes including practice and recording. Split into short sessions as needed.

## Concept

A feedback rule changes a command based on error. Our mock controller limits the command change and clamps the commanded cable length between bounds. The mock reading equals command length, so this is a toy plant, not a prism controller. Real hardware also needs force limits, sensor validation, emergency stop and review of failure modes.

![Supporting diagram for this phase](../../../../assets/learning-loop.svg)

## Worked example

At current length 0.150 m, target 0.160 m and gain 0.2, raw change is 0.002 m. With maximum step 0.001 m, next command is 0.151 m. A command beyond the upper bound is clamped; this software bound does not physically prevent excess tension.

## Materials and setup

Python and the controller lab; no motors or hardware connected.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Calculate the first bounded step by hand.
2. Run the controller lab and compare its first row.
3. Use the API to test current length at the upper bound.
4. List consequences of a stuck sensor and a wrong sign of feedback.
5. Draft hardware-review conditions without implementing a physical actuator.

## Runnable lab

From the repository root (the folder containing README.md):

```bash
python3 -m tensegrity controller
```

See the [lab guide](../../../../labs/README.md) for expected output and parameter changes. Compare one output with a calculation before interpreting the result. If you cannot run Python, use the worked example and label the task as a manual exercise.

## Expected behavior and interpretation

The simulated command approaches the target within stated bounds and has limited step size.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

Do not use the toy controller on hardware. Length bounds alone do not bound cable force.

## Teach-back quiz

1. What is the first next command?
2. Is the mock sensor realistic?
3. Do command bounds guarantee safe force?

[Facilitator answer key](../../../../assessments/phase-08-answers.md) — attempt the questions first.

## Evidence to submit

A hand-checked controller trace and failure-case list.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
