# Lesson 07: Prestress and slack

[Course contents](../../../../COURSE.md) · Phase 01: Structural intuition

## Objective

Explain internal force before external loading and detect slack.

**Prerequisite:** Lesson 06; or demonstrate its evidence check.

**Planning time:** approximately 180 minutes including practice and recording. Split into short sessions as needed.

## Concept

Prestress is an initial internal force state. In a free ideal tensegrity, self-stress can balance at every node without external loading. Cables must remain tensile in the intended state. Prestress may alter stiffness, but increasing it also raises joint demand and strut compression. Equilibrium, stability and material capacity are different checks.

![Supporting diagram for this phase](../../../../assets/prism.svg)

## Worked example

For a unilateral spring with stiffness 100 N/m, rest length 0.14 m and current length 0.15 m, tension is 1 N. At 0.13 m the model returns 0 N, not −1 N, because a cable does not carry compression.

## Materials and setup

Cord or low-tension elastic sample, ruler; optional Python 3.10 or newer.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Observe a cord at three gentle extensions without releasing it suddenly.
2. Record when it is slack and when it is taut.
3. Calculate the two example spring forces.
4. If using Python, run the spring lab at lengths 0.15 and 0.13 m.
5. Explain why a spring estimate is not proof of prism stability.

## Runnable lab

From the repository root (the folder containing README.md):

```bash
python3 -m tensegrity spring
```

See the [lab guide](../../../../labs/README.md) for expected output and parameter changes. Compare one output with a calculation before interpreting the result. If you cannot run Python, use the worked example and label the task as a manual exercise.

## Expected behavior and interpretation

The calculation clips compressive cable force to zero; physical response depends on the actual material.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

Do not infer cable force from appearance alone. Stronger tightening can cause joint failure or buckling.

## Teach-back quiz

1. What is self-stress?
2. What force is predicted below rest length?
3. Does extra prestress always help?

[Facilitator answer key](../../../../assessments/phase-01-answers.md) — attempt the questions first.

## Evidence to submit

A slack/taut observation table and two checked calculations.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
