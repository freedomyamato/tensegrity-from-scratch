# Lesson 28: Damaged-member scenarios

[Course contents](../../../../COURSE.md) · Phase 06: Dynamics and resilience

## Objective

Assess topology changes without deliberately causing an energetic failure.

**Prerequisite:** Lesson 27; or demonstrate its evidence check.

**Planning time:** approximately 240 minutes including practice and recording. Split into short sessions as needed.

## Concept

Removing a member changes the force-equilibrium system and possible mechanisms. A prior self-stress vector cannot simply be reused. Redundancy means a system can retain required function after a defined failure, not merely that it has many components. Review damage in the digital model before considering physical handling.

![Supporting diagram for this phase](../../../../assets/learning-loop.svg)

## Worked example

Delete C0 from the 30° prism member list, rebuild A and compute its nullspace. In this ideal example the original nonzero self-stress is lost. That finding concerns this topology and unloaded idealization; it is not a general result for every tensegrity.

## Materials and setup

Python console, models.py and node/member schedule; physical model observation is optional.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Copy the short damaged-member example in labs/README.md.
2. Inspect the original matrix and self-stress dimension.
3. Remove C0 and repeat the calculation.
4. Explain why unchanged appearance would not prove retained capability.
5. Write a detect–isolate–repair–recheck procedure for a frayed C0.

## Expected behavior and interpretation

The numerical result illustrates how one missing member changes the equilibrium problem.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

Do not cut a loaded cable. Physical removal occurs only after all tension is safely released.

## Teach-back quiz

1. Can you reuse the original force vector?
2. What does redundancy require?
3. When may a damaged cable be removed physically?

[Facilitator answer key](../../../../assessments/phase-06-answers.md) — attempt the questions first.

## Evidence to submit

Original/damaged comparison and a repair procedure.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
