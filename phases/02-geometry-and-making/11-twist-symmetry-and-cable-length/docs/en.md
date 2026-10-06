# Lesson 11: Twist, symmetry and cable length

[Course contents](../../../../COURSE.md) · Phase 02: Geometry and making

## Objective

Relate rotation to member lengths without assuming all twists are equilibria.

**Prerequisite:** Lesson 10; or demonstrate its evidence check.

**Planning time:** approximately 270 minutes including practice and recording. Split into short sessions as needed.

## Concept

At fixed radius R and height h, the corresponding-node cable length is sqrt(h²+2R²(1−cos α)). Our offset strut length is sqrt(h²+2R²(1−cos(α+120°))). Symmetry makes each family equal in length. Changing α changes geometry; it need not preserve an admissible self-stress for the same connectivity.

![Supporting diagram for this phase](../../../../assets/prism.svg)

## Worked example

For R=0.08 m and h=0.14 m, at α=0° each corresponding-node cable is 0.14 m. At α=30° it is approximately 0.14600 m. The 30° example has a valid analytic self-stress; the twist sweep checks other angles separately.

## Materials and setup

Calculator or Python, member table; no physical retensioning is required.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Calculate the cable length at 0° and 30°.
2. Predict whether increasing h changes all member families.
3. Generate prism outputs at 30° and 45° using different output filenames.
4. Compare member lengths and nullspace dimensions.
5. Separate geometric feasibility from force-equilibrium feasibility in your notes.

## Runnable lab

From the repository root (the folder containing README.md):

```bash
python3 -m tensegrity prism
```

See the [lab guide](../../../../labs/README.md) for expected output and parameter changes. Compare one output with a calculation before interpreting the result. If you cannot run Python, use the worked example and label the task as a manual exercise.

## Expected behavior and interpretation

Triangle edges depend on radius only; cross and strut spans depend on height and twist.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

A visually attractive twist may have no nonzero self-stress in this ideal free framework.

## Teach-back quiz

1. Do triangle edges depend on height?
2. What is C0’s span at zero twist?
3. Does a new geometry automatically balance?

[Facilitator answer key](../../../../assessments/phase-02-answers.md) — attempt the questions first.

## Evidence to submit

Two geometry tables with an equilibrium distinction.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
