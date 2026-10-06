# Lesson 16: Nodal equilibrium and self-stress

[Course contents](../../../../COURSE.md) · Phase 03: Statics and useful mathematics

## Objective

Verify a nonzero balanced internal force-density state in the ideal prism.

**Prerequisite:** Lesson 15; or demonstrate its evidence check.

**Planning time:** approximately 270 minutes including practice and recording. Split into short sessions as needed.

## Concept

For member i, force density q_i=F_i/L_i. At a node, sum q_i(x_other−x_node)=0 in the unloaded free case. At 30° twist our analytic state uses ring densities 1/√3 N/m, cross densities 1 N/m and strut densities −1 N/m. The scale can vary; real material and stability limits remain separate.

![Supporting diagram for this phase](../../../../assets/prism.svg)

## Worked example

A ring length 0.13856 m with q=1/√3 N/m carries approximately 0.08 N tension. A 0.14600 m cross cable with q=1 N/m carries approximately 0.14600 N. These forces differ despite symmetric families. The code evaluates residuals at all six nodes.

## Materials and setup

Calculator or Python and the prism output.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Run the prism lab at its default geometry.
2. Find example_force_density and example_member_force_N in the output.
3. Check one F=qL multiplication by hand.
4. Explain why the negative entries correspond to the intended struts.
5. Inspect the maximum residual and describe what its small value does and does not show.

## Runnable lab

From the repository root (the folder containing README.md):

```bash
python3 -m tensegrity prism
```

See the [lab guide](../../../../labs/README.md) for expected output and parameter changes. Compare one output with a calculation before interpreting the result. If you cannot run Python, use the worked example and label the task as a manual exercise.

## Expected behavior and interpretation

The ideal analytic state balances to floating-point precision and has cable-positive/strut-negative signs.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

q is N/m, not N. A small residual is an equilibrium check, not proof of prestress stability.

## Teach-back quiz

1. How is force density defined?
2. Why is a strut density negative?
3. What remains after checking equilibrium?

[Facilitator answer key](../../../../assessments/phase-03-answers.md) — attempt the questions first.

## Evidence to submit

A hand calculation, solver output and limitations statement.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
