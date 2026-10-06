# Geometry and model derivations

## Our topology

Bottom nodes i=0,1,2 have coordinates (R cosθi,R sinθi,0), where θi=2πi/3. Top nodes i+3 have coordinates (R cos(θi+α),R sin(θi+α),h). Ring cables form each triangle. Cross cables connect i to i+3. Struts connect i to ((i+1) mod 3)+3.

This fixes both topology and rotation convention. “Three-strut prism” alone is insufficient because changing endpoint ordering changes the equilibrium problem.

## Member lengths

Two points on a radius-R circle separated by angle β have squared planar distance 2R²(1−cosβ).

- Ring edge: Lr=√3R.
- Cross cable: Lc=√[h²+2R²(1−cosα)].
- Strut: Ls=√[h²+2R²(1−cos(α+120°))].

At α=30°, the squared planar terms become (2−√3)R² for cross cables and (2+√3)R² for struts. These closed forms provide independent tests of the coordinate-based code.

## Analytic self-stress

Use force density q=F/L, positive in tension. At bottom node 0, the two ring directions sum to (−3R,0,0). The cross and offset-strut vectors are respectively:

```text
cross: (R cosα−R, R sinα, h)
strut: (R cos(α+120°)−R, R sin(α+120°), h)
```

Set qstrut=−qcross to cancel the vertical components. At α=30°, sin30°=sin150°, so y also cancels. The remaining x contribution is √3R qcross. Balance requires −3R qring+√3R qcross=0, hence qring=qcross/√3. Rotational symmetry gives the other bottom nodes; the matching top equilibrium follows by the same geometry. The code independently checks all 18 nodal components.

Choosing qcross=1 N/m produces positive cable densities and negative strut densities. Multiplying all q by a common positive factor retains ideal unloaded equilibrium. This does not establish which scale a real material/joint can sustain.

## Numerical nullspace

Each member column in A contains its coordinate difference at one endpoint and the opposite at the other. A has units m; q has N/m; A q has N. RREF normalizes the matrix by its largest absolute element before using a relative pivot tolerance. Its basis may have reversed overall sign; normalize and check physical signs before interpreting it.

Near singular geometry, numerical rank depends on tolerance. A rank count alone is not a symbolic proof or a full elastic stability analysis. The tests check known independent geometry, analytic equilibrium, rigid transformations, scale invariance and deliberately changed topology/twist.

## Other educational models

Cable spring: F=k max(0,L−L0). Euler column: Pcr=π²EI/(KL)² for a slender ideal column. Oscillator: m ẍ+c ẋ+kx=0, integrated with RK4. Solar record: EWh=Σ(Δt)(Pa+Pb)/2/3600 with P=VI. Controller: a clipped proportional length step, applied to a mock plant only.

None of these models computes a loaded, elastic, supported three-dimensional tensegrity structure with real joints. Use them to understand individual assumptions and measurements, then identify what a more complete analysis would require.
