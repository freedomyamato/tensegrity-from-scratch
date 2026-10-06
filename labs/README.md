# Computational labs

Python 3.10+; standard library only. Run from the root directory. Each command prints its result or output filename. Generated files under `outputs/` are ignored by Git. Example data are explicitly synthetic.

## 1. Prism geometry and self-stress

```bash
python3 -m tensegrity prism
python3 -m tensegrity prism --height 0.16 --output outputs/taller-prism.json
```

Defaults: R=0.08 m, h=0.14 m, twist=30°. Output has six nodes, twelve members and a one-dimensional nullspace. Ring, cross and strut lengths are approximately 0.138564,0.145996,0.208531 m. Analytic q is +1/√3 for rings, +1 for cross cables and −1 for struts, in N/m. The maximum nodal residual should be below 10⁻¹² N on typical floating-point implementations. It verifies equilibrium, not stability.

## 2. Constrained twist sweep

```bash
python3 -m tensegrity sweep
```

Output `outputs/twist-sweep.csv` compares nine angles. The reference self-stress balances at 30°; other sampled angles have nonzero residual and normally a trivial nullspace for this topology. RREF rank uses an explicit relative tolerance. The scan is not a general form-finding or stability solver.

## 3. Unilateral spring

```bash
python3 -m tensegrity spring --stiffness 100 --length 0.15 --rest-length 0.14
python3 -m tensegrity spring --length 0.13
```

Expected forces: 1 N and 0 N. Model: F=k max(0,L−L0). It does not model hysteresis or the full structure. Compare with the illustrative data in [cable_extension.csv](../examples/cable_extension.csv).

## 4. Ideal Euler column

```bash
python3 -m tensegrity buckling
python3 -m tensegrity buckling --length 0.4
```

Hypothetical E=2×10⁹ Pa, I=10⁻¹⁰ m⁴, L=0.2 m, K=1 gives about 49.348 N. Doubling length gives 12.337 N. These are not material properties or safe-load ratings for your kit.

## 5. Oscillator

```bash
python3 -m tensegrity oscillator --damping 0 --output outputs/undamped.csv
python3 -m tensegrity oscillator --damping 0.4 --output outputs/damped.csv
```

Defaults m=1 kg, k=4 N/m, x0=0.01 m and v0=0. Time step 0.01 s, duration 5 s. Total initial energy is 0.0002 J. Undamped energy stays approximately constant; damping causes decay. This is a single oscillator, not a multi-node tensegrity solver. The code guards oversized time steps for the teaching range.

## 6. Solar energy integration

```bash
python3 -m tensegrity solar examples/solar_readings.csv
```

Expected energy 0.018333333 Wh over the two-minute synthetic record. Each row has time in seconds, loaded voltage in V and current in A at the same operating point. Energy uses trapezoidal integration of P=VI divided by 3600. Times must strictly increase; negative/nonfinite values are rejected. The integrator does not infer conversion efficiency or compare weather conditions for you.

## 7. Bounded mock controller

```bash
python3 -m tensegrity controller
```

First row: mock reading 0.150 m and next command 0.151 m. A proportional rule clips step size to 0.001 m and command length to [0.12,0.18] m. The mock plant reports command length directly. No hardware driver or physical force limit exists; do not connect this toy model to actuators.

## Damaged-member API exercise

Create a short local script or paste this into a Python console opened at the root:

```python
from tensegrity.models import prism, equilibrium_matrix, nullspace
nodes, members = prism()
print(len(nullspace(equilibrium_matrix(nodes, members))))  # 1
damaged = [m for m in members if m.name != "C0"]
print(len(nullspace(equilibrium_matrix(nodes, damaged))))  # 0
```

Removing a member changes this ideal self-stress problem. This does not alone characterize every failure response of a physical model. Never cut a tensioned member for this exercise.

## Interpret and record

Keep the command, parameters, meaningful output and one independent calculation. Identify whether evidence is computational, synthetic or physical. A passing software test does not fill the physical validation field in your notebook.
