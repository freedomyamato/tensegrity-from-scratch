# Lesson 21: Coordinates and member lengths

[Course contents](../../../../COURSE.md) · Phase 05: Form-finding and digital models

## Objective

Generate geometry and independently check its dimensions.

**Prerequisite:** Lesson 20; or demonstrate its evidence check.

**Planning time:** approximately 300 minutes including practice and recording. Split into short sessions as needed.

## Concept

Coordinates give a precise geometric model. Our bottom triangle lies at z=0; the top at z=h, rotated by α. Node radii are measured from the central axis, not between adjacent nodes. Member length is Euclidean distance between its endpoint coordinates. The drawing uses projection, so visual lengths are not measurement values.

![Supporting diagram for this phase](../../../../assets/prism.svg)

## Worked example

A triangle on a circle of radius R has side √3R. At R=0.08 m the edge is 0.138564 m. Both bottom and top rings share this value. Setting h=0.16 m changes cross/strut lengths while leaving ring edges unchanged.

## Materials and setup

Python 3.10+, calculator and prism drawing; manual calculation alternative permitted.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Generate the default prism JSON.
2. Calculate the bottom ring length from √3R.
3. Check node z coordinates and radial distances.
4. Generate a second geometry with --height 0.16 and a separate output path.
5. Compare each member family and note projection versus true length.

## Runnable lab

From the repository root (the folder containing README.md):

```bash
python3 -m tensegrity prism
```

See the [lab guide](../../../../labs/README.md) for expected output and parameter changes. Compare one output with a calculation before interpreting the result. If you cannot run Python, use the worked example and label the task as a manual exercise.

## Expected behavior and interpretation

All equivalent members agree and independently checked distances match the code.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

Geometry output is a mathematical model, not a fabrication certificate. Units and node definitions must travel with it.

## Teach-back quiz

1. What does radius mean here?
2. How long is a triangle edge?
3. Why not measure the projected diagram?

[Facilitator answer key](../../../../assessments/phase-05-answers.md) — attempt the questions first.

## Evidence to submit

Two saved geometries and independent distance checks.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
