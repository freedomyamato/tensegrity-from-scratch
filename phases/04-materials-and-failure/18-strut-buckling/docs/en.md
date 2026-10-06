# Lesson 18: Strut buckling

[Course contents](../../../../COURSE.md) · Phase 04: Materials and failure

## Objective

Use an ideal buckling equation to explore length sensitivity.

**Prerequisite:** Lesson 17; or demonstrate its evidence check.

**Planning time:** approximately 240 minutes including practice and recording. Split into short sessions as needed.

## Concept

Euler’s ideal elastic column model gives Pcr=π²EI/(KL)². E is modulus in Pa, I the cross-section second moment in m⁴, L the length in m and K an effective-length factor. It assumes a slender, straight column with idealized end conditions. Actual failure may occur earlier because of imperfections, joints or material limits.

![Supporting diagram for this phase](../../../../assets/prism.svg)

## Worked example

Using hypothetical E=2×10⁹ Pa, I=10⁻¹⁰ m⁴, L=0.20 m and K=1 gives approximately 49.35 N. Doubling L gives about 12.34 N, one quarter. These inputs are illustrative, not properties or a rating for your craft sticks.

## Materials and setup

Calculator or Python; no physical failure test required.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Run the default buckling lab and reproduce the value by hand.
2. Run it at length 0.4 m; calculate the ratio.
3. Change K to 2 and explain the result.
4. List three reasons a physical strut may fail below the ideal value.
5. Label your table “hypothetical ideal column,” not “safe load.”

## Runnable lab

From the repository root (the folder containing README.md):

```bash
python3 -m tensegrity buckling
```

See the [lab guide](../../../../labs/README.md) for expected output and parameter changes. Compare one output with a calculation before interpreting the result. If you cannot run Python, use the worked example and label the task as a manual exercise.

## Expected behavior and interpretation

Longer effective length sharply reduces the ideal buckling load.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

Do not use the result as a allowable load or deliberately load a classroom strut to collapse.

## Teach-back quiz

1. What happens when length doubles?
2. What does I measure?
3. Is Pcr a complete safe-load calculation?

[Facilitator answer key](../../../../assessments/phase-04-answers.md) — attempt the questions first.

## Evidence to submit

A parameter table and three model limitations.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
