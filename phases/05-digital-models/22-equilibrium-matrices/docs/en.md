# Lesson 22: Equilibrium matrices

[Course contents](../../../../COURSE.md) · Phase 05: Form-finding and digital models

## Objective

Read how member connectivity becomes a linear equilibrium system.

**Prerequisite:** Lesson 21; or demonstrate its evidence check.

**Planning time:** approximately 300 minutes including practice and recording. Split into short sessions as needed.

## Concept

The force-density matrix A has three rows per node and one column per member. At endpoint a the member column contains x_b−x_a; at b it contains the negative. Thus A q=0 represents free unloaded self-stress. This differs from a unit-direction matrix acting on axial forces F. A nontrivial nullspace may describe balanced internal stress, but admissible signs and stability still matter.

![Supporting diagram for this phase](../../../../assets/prism.svg)

## Worked example

Six nodes give 18 rows and twelve members give 12 columns. Our 30° prism has a one-dimensional self-stress nullspace in the chosen numerical tolerance. Multiplying any basis vector by a scalar retains equilibrium; its signs must match cables and struts.

## Materials and setup

Python, tensegrity/models.py and default prism output.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Read equilibrium_matrix and identify endpoint row indices.
2. Inspect one column and verify that endpoint entries cancel.
3. Run the prism lab and inspect its nullspace basis.
4. Multiply the analytic q by 2 and verify residual scaling remains near zero.
5. State why a solver’s tolerance and unit scaling matter.

## Runnable lab

From the repository root (the folder containing README.md):

```bash
python3 -m tensegrity prism
```

See the [lab guide](../../../../labs/README.md) for expected output and parameter changes. Compare one output with a calculation before interpreting the result. If you cannot run Python, use the worked example and label the task as a manual exercise.

## Expected behavior and interpretation

The independent analytic vector agrees with a numerical nullspace up to scale and sign.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

Do not confuse numerical rank with exact symbolic proof, especially near the special twist angle.

## Teach-back quiz

1. What are A’s dimensions?
2. What multiplies this A: q or F?
3. Can any nullspace vector be used physically?

[Facilitator answer key](../../../../assessments/phase-05-answers.md) — attempt the questions first.

## Evidence to submit

A matrix-column explanation and residual verification.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
