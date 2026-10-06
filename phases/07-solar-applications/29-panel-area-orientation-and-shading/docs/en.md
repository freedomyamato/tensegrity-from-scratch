# Lesson 29: Panel area, orientation and shading

[Course contents](../../../../COURSE.md) · Phase 07: Solar and Singapore applications

## Objective

Separate solar conversion efficiency from energy yield and support geometry.

**Prerequisite:** Lesson 28; or demonstrate its evidence check.

**Planning time:** approximately 270 minutes including practice and recording. Split into short sessions as needed.

## Concept

A support can change orientation, shading and operating conditions without changing the cell technology. Power P=VI requires simultaneous voltage/current at the same loaded operating point. Conversion efficiency relates electrical power to incident solar power over area; yield is integrated energy over time. This course tests support tradeoffs rather than assuming tensegrity increases efficiency.

![Supporting diagram for this phase](../../../../assets/solar-measurement.svg)

## Worked example

At a loaded 5 V and 0.1 A, power is 0.5 W. Over two minutes of constant output this is 0.01667 Wh. Our sample fluctuating record gives approximately 0.01833 Wh by trapezoidal integration. Open-circuit V and short-circuit I must not be multiplied together as operating power.

## Materials and setup

Paper dummy panel, angle ruler; optional small educational low-voltage panel, suitable load and meters used according to instructions.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Measure dummy-panel area and choose a repeatable angle reference.
2. Calculate the constant-power example.
3. Run the solar lab on the synthetic readings.
4. Draw possible shadows from struts and cables at two orientations.
5. Write which measurements would separate orientation benefits from actual conversion efficiency.

## Runnable lab

From the repository root (the folder containing README.md):

```bash
python3 -m tensegrity solar examples/solar_readings.csv
```

See the [lab guide](../../../../labs/README.md) for expected output and parameter changes. Compare one output with a calculation before interpreting the result. If you cannot run Python, use the worked example and label the task as a manual exercise.

## Expected behavior and interpretation

The learner reports energy over a defined interval and identifies shading as a measurable mechanism.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

Do not connect to household electricity or improvise grid wiring. Synthetic readings do not establish real solar performance.

## Teach-back quiz

1. What readings are required for operating power?
2. Does structure shape inherently change cell efficiency?
3. What are energy units here?

[Facilitator answer key](../../../../assessments/phase-07-answers.md) — attempt the questions first.

## Evidence to submit

Panel/shadow sketch and a checked power–energy calculation.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
