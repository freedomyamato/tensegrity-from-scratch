# Lesson 09: Nodes and connectivity

[Course contents](../../../../COURSE.md) · Phase 02: Geometry and making

## Objective

Translate the prism into a node and member schedule.

**Prerequisite:** Lesson 08; or demonstrate its evidence check.

**Planning time:** approximately 270 minutes including practice and recording. Split into short sessions as needed.

## Concept

Topology says which nodes are connected; geometry says where they are. Our prism uses bottom nodes 0,1,2 and top nodes 3,4,5. B and T are triangle-edge cables; C joins corresponding bottom/top nodes; S joins bottom i to top (i+1) modulo 3. The six nodes and twelve members must be labeled consistently across drawings and code.

![Supporting diagram for this phase](../../../../assets/prism.svg)

## Worked example

C0 connects 0–3. S0 connects 0–4, S1 connects 1–5 and S2 connects 2–3. At node 0, B0, B2, C0 and S0 meet. A missing C0 changes topology even if the model still looks similar.

## Materials and setup

Printed assets/prism.svg, member table in builds/three-strut-prism.md, label stickers.

Use a private copy of the [experiment record](../../../../templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.

## Predict and practice

Before acting, write the result you expect and one observation that could disagree with it.

1. Label all six nodes on a drawing.
2. Copy all twelve member endpoint pairs.
3. List the four members meeting node 0.
4. Count how many times each member endpoint appears across nodes.
5. Match the drawing labels to the supplied digital prism output.

## Expected behavior and interpretation

There are nine cables and three struts; each node has degree four.

If your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.

## Troubleshooting and limits

Mixing top-node order changes the geometry and may create intersecting or unbalanced members.

## Teach-back quiz

1. How many cables are in this topology?
2. What does S2 connect?
3. What is the difference between topology and geometry?

[Facilitator answer key](../../../../assessments/phase-02-answers.md) — attempt the questions first.

## Evidence to submit

A complete labeled node/member schedule.

Include your prediction, setup, results with units or criteria, and one limitation. Use the [rubric](../../../../assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.

## Facilitator adaptation

Offer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.

## Reading and provenance

See [source notes](../../../../references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.
