# Lesson 25: Vibration and damping

[Course contents](../../../../COURSE.md) · Phase 06: Dynamics and resilience

## Objective

Distinguish stiffness, inertia and damping through a one-degree-of-freedom example.

**Prerequisite:** Lesson 24; or demonstrate its evidence check.

**Planning time:** approximately 240 minutes including practice and recording. Split into short sessions as needed.

## Concept

A simple oscillator follows m ẍ+c ẋ+k x=0. Mass stores kinetic energy, stiffness stores elastic energy and damping dissipates energy. Its undamped natural angular frequency is sqrt(k/m). This model teaches dynamics but does not represent every node or mode of a tensegrity structure.

![Supporting diagram for this phase](../../../../assets/learning-loop.svg)

## Worked example

For m=1 kg and k=4 N/m, natural angular frequency is 2 rad/s, about 0.318 Hz. With c=0, ideal total energy stays constant; with c=0.4 N·s/m, it decays. The supplied RK4 integrator checks numerical behavior over small time steps.

## Materials and setup

Python or supplied example oscillator table; optional ruler and video of a gently disturbed tabletop model.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Calculate the example natural frequency.
2. Run the oscillator with damping 0 and 0.4, saving to different files.
3. Compare displacement peaks and energy columns.
4. If observing a model, gently disturb it without adding loads; record motion without claiming a fitted full model.
5. Explain one reason measured oscillation differs from the one-DOF idealization.

## Runnable lab

From the repository root (the folder containing README.md):

```bash
python3 -m tensegrity oscillator
```

See the [lab guide](../../../../labs/README.md) for expected output and parameter changes. Compare one output with a calculation before interpreting the result. If you cannot run Python, use the worked example and label the task as a manual exercise.

## Expected behavior and interpretation

Undamped energy varies only by small numerical error; positive damping reduces energy.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

Numerical time-step error can resemble damping. Multiple structural modes cannot be inferred from one trace alone.

## Teach-back quiz

1. What does damping do to energy?
2. What is sqrt(k/m)?
3. Is this a full tensegrity dynamic solver?

[Facilitator answer key](../../../../assessments/phase-06-answers.md) — attempt the questions first.

## Evidence to submit

Two oscillator traces and a model-scope explanation.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
