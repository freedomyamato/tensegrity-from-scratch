# Lesson 23: Constrained form-finding

[Course contents](../../../../COURSE.md) · Phase 05: Form-finding and digital models

## Objective

Explore a constrained geometry search and identify feasible equilibrium.

**Prerequisite:** Lesson 22; or demonstrate its evidence check.

**Planning time:** approximately 300 minutes including practice and recording. Split into short sessions as needed.

## Concept

Form-finding seeks geometry compatible with chosen connectivity and force/material constraints. Our introductory lab restricts radius and height and varies only twist; it is not a general nonlinear design optimizer. The reference analytic q balances at 30° for this topology. Away from that angle, residual grows and the numerical nullspace usually becomes trivial.

![Supporting diagram for this phase](../../../../assets/prism.svg)

## Worked example

At 30°, y components from corresponding cable and offset strut cancel because sin30°=sin150°. Their x components balance the two ring cables when qring=qcross/√3. This explains the special geometry rather than merely selecting the prettiest rendering.

## Materials and setup

Python or calculator; no physical high-tension geometry search.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Run the sweep lab for the supplied nine twist angles.
2. Locate the angle with a nonzero nullspace and a near-zero reference residual.
3. Explain the y-component cancellation at 30°.
4. Name constraints missing from the sweep: material rest lengths, external loads and stability.
5. Describe what evidence a general solver would need before acceptance.

## Runnable lab

From the repository root (the folder containing README.md):

```bash
python3 -m tensegrity sweep
```

See the [lab guide](../../../../labs/README.md) for expected output and parameter changes. Compare one output with a calculation before interpreting the result. If you cannot run Python, use the worked example and label the task as a manual exercise.

## Expected behavior and interpretation

The constrained scan reveals a special equilibrium and separates it from arbitrary geometric variants.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

A small sample scan does not prove that no other equilibrium geometry exists outside its range or topology.

## Teach-back quiz

1. Which variable is searched?
2. Does the lab optimize every node?
3. What must be checked beyond residual?

[Facilitator answer key](../../../../assessments/phase-05-answers.md) — attempt the questions first.

## Evidence to submit

A twist-sweep table with a feasibility interpretation.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
