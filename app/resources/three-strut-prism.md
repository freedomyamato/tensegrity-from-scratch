# Three-strut tabletop prism

## Nominal geometry and status

Radius 80 mm, height 140 mm, top triangle rotated +30° counterclockwise when viewed from above in the x–y convention. Six point nodes, nine cables and three struts. This **ideal geometry and its self-stress are numerically verified**. The following physical procedure has not been tested in a real workshop; treat it as a pilot build and record deviations.

![Node and member labels](../assets/prism.svg)

| Family | Members/endpoints | Nominal node-to-node span |
|---|---|---:|
| Bottom ring | B0 0–1; B1 1–2; B2 2–0 | 138.564 mm |
| Top ring | T0 3–4; T1 4–5; T2 5–3 | 138.564 mm |
| Cross cables | C0 0–3; C1 1–4; C2 2–5 | 145.996 mm |
| Struts | S0 0–4; S1 1–5; S2 2–3 | 208.531 mm |

Use [node coordinates](../assets/node-coordinates.csv) and [member schedule](../assets/member-schedule.csv) for the precise ideal values. These are spans between defined nodes, not universal cut lengths. If your strut node spans differ, choose a consistent scaled geometry; do not force 208.531 mm onto unsuitable sticks.

## Materials

Three blunt lightweight craft struts with secure soft attachment loops; nine cord segments with adjustable loops; removable tape; labels; ruler; tray; cardboard supports/jig. Pre-cut and preassembled options are useful. Elastic can be used only as a documented low-tension teaching substitution; it changes constitutive behavior. No load rating is supplied for these materials.

## Joint trial before assembly

Make one sample attachment. Mark where the loop sits and gently snug it without high tension. Reject any joint that slips suddenly, exposes sharp edges or damages the cord. Define a node consistently—e.g., the center of the attachment loop. Measure knot/loop allowance separately. Do not rely on an adhesive bond for an unreviewed structural capacity claim.

## Positioning jig

Print [bottom](../assets/jig-bottom.svg) and [top](../assets/jig-top.svg) node patterns at actual size. Verify the 50 mm check line with a ruler; if it is wrong, use the coordinate table or rescale. The jigs show plan positions only. Cardboard spacers can temporarily hold the top pattern 140 mm above the bottom; they support the model during assembly and are not part of the final topology. Do not use them to infer load capacity.

## Assembly

1. Mark all six nodes and identify all twelve members. Check the endpoint schedule aloud or visually.
2. Support the top and bottom node positions using a jig or an assistant. Place S0 along 0–4, S1 along 1–5 and S2 along 2–3. The rods must not be connected to one another along their lengths.
3. Attach the bottom triangle B0,B1,B2 loosely. Check every endpoint.
4. Attach the top triangle T0,T1,T2 loosely. Confirm the top labeling follows the +30° plan pattern.
5. Attach C0,C1,C2. All cables start adjustable; do not pull one cable hard to force the entire shape.
6. Snug connections in small alternating increments, maintaining roughly symmetric family spans. Reinspect for slip, overlap or rod contact. Never place your face near stretched components.
7. Gradually reduce jig support only when joints stay secured and the model can be controlled. If it collapses or releases, support it again and diagnose. No person or object should be under a suspended model.
8. Record measured spans, node heights, joint details and which ideal assumptions differ. Photograph labels, not just the finished silhouette.

## Troubleshooting

| Observation | Check first | Next action |
|---|---|---|
| Model collapses as jig is removed | Missing C cable, wrong top-node order, slip | Resupport, release gently, verify topology |
| One strut contacts another | Topology/twist and real joint offsets | Correct labels and geometry; do not force separation |
| Cable stays slack | Rest length, knot take-up and geometry | Adjust gently with model supported |
| Shape drifts over minutes | Witness marks, creep and measurement method | Record time-series, inspect joint and material |
| Large deviation from ideal spans | Actual strut node length and scaling | Recalculate consistent geometry or retain documented deviation |

Stop on fraying, damaged struts, sudden slip or uncontrolled motion. Do not add a panel or extra load during the first build. The next milestone is repeatable assembly and an honest comparison with the ideal model.
