"""Independent mathematical checks and invalid-input tests for teaching labs."""
import math
import unittest
from tensegrity.models import (prism,lengths,equilibrium_matrix,nullspace,
                               analytic_self_stress,max_residual,cable_force,
                               euler_load,oscillator,integrate_power,controller_step)


class PrismTests(unittest.TestCase):
    def test_geometry_against_independent_closed_forms(self):
        R,h=.08,.14
        n,m=prism(R,h); L=lengths(n,m)
        self.assertEqual(len(n),6);self.assertEqual(len(m),12)
        for l in L[:6]: self.assertAlmostEqual(l,math.sqrt(3)*R)
        for l in L[6:9]: self.assertAlmostEqual(l,math.sqrt(h*h+(2-math.sqrt(3))*R*R))
        for l in L[9:]: self.assertAlmostEqual(l,math.sqrt(h*h+(2+math.sqrt(3))*R*R))

    def test_balanced_admissible_self_stress_for_multiple_sizes(self):
        for R,h in [(.08,.14),(.02,.1),(.2,.03)]:
            n,m=prism(R,h);A=equilibrium_matrix(n,m);q=analytic_self_stress()
            self.assertLess(max_residual(A,q),1e-12)
            self.assertTrue(all(x>0 for x in q[:9]));self.assertTrue(all(x<0 for x in q[9:]))
            b=nullspace(A);self.assertEqual(len(b),1)
            normalized=[v/b[0][6] for v in b[0]]
            for a,c in zip(normalized,q):self.assertAlmostEqual(a,c,places=9)

    def test_force_density_is_not_axial_force(self):
        n,m=prism();L=lengths(n,m);q=analytic_self_stress()
        self.assertAlmostEqual(q[0]*L[0],.08)
        self.assertNotAlmostEqual(q[0],q[0]*L[0])

    def test_translation_and_rotation_do_not_break_equilibrium(self):
        n,m=prism();transformed=[(-y+.9,x-.2,z+.3) for x,y,z in n]
        self.assertLess(max_residual(equilibrium_matrix(transformed,m),analytic_self_stress()),1e-12)

    def test_arbitrary_twist_is_not_the_same_equilibrium(self):
        n,m=prism(twist_degrees=45);A=equilibrium_matrix(n,m)
        self.assertEqual(len(nullspace(A)),0)
        self.assertGreater(max_residual(A,analytic_self_stress()),.001)

    def test_damaged_topology_loses_this_self_stress(self):
        n,m=prism();damaged=[x for x in m if x.name!='C0']
        self.assertEqual(len(nullspace(equilibrium_matrix(n,damaged))),0)

    def test_bad_dimensions(self):
        for kwargs in [{'radius':0},{'height':-1},{'radius':float('nan')},{'twist_degrees':float('inf')}]:
            with self.assertRaises(ValueError):prism(**kwargs)


class LinearAlgebraTests(unittest.TestCase):
    def test_known_nullspace_and_scale_invariance(self):
        for scale in [1,1e-12,1e12]:
            matrix=[[scale,2*scale,3*scale],[2*scale,4*scale,6*scale]]
            basis=nullspace(matrix);self.assertEqual(len(basis),2)
            for v in basis:self.assertLess(max_residual(matrix,v)/(abs(scale)),1e-10)

    def test_full_rank_and_zero_matrix(self):
        self.assertEqual(nullspace([[1,0],[0,1]]),[])
        self.assertEqual(nullspace([[0,0],[0,0]]),[[1.,0.],[0.,1.]])

    def test_invalid_matrix(self):
        for a in [[],[[1],[1,2]],[[math.nan]]]:
            with self.assertRaises(ValueError):nullspace(a)


class MaterialTests(unittest.TestCase):
    def test_tension_only_spring(self):
        self.assertAlmostEqual(cable_force(100,.15,.14),1)
        self.assertEqual(cable_force(100,.13,.14),0)

    def test_euler_scaling(self):
        P=euler_load(2e9,1e-10,.2)
        self.assertAlmostEqual(P,49.34802200544678)
        self.assertAlmostEqual(euler_load(2e9,1e-10,.4),P/4)
        self.assertAlmostEqual(euler_load(2e9,1e-10,.2,2),P/4)

    def test_invalid_material_parameters(self):
        with self.assertRaises(ValueError):cable_force(-1,.15,.14)
        with self.assertRaises(ValueError):euler_load(1,0,.2)


class DynamicsTests(unittest.TestCase):
    def test_undamped_solution_against_cosine(self):
        rows=oscillator(damping=0,duration=2,dt=.01)
        for r in rows:
            self.assertAlmostEqual(r['displacement_m'],.01*math.cos(2*r['time_s']),places=9)
            self.assertAlmostEqual(r['energy_J'],.0002,places=10)

    def test_damped_energy_decreases(self):
        rows=oscillator();energies=[r['energy_J'] for r in rows]
        self.assertTrue(all(b<=a+1e-12 for a,b in zip(energies,energies[1:])))
        self.assertLess(energies[-1],energies[0])

    def test_bad_time_step(self):
        with self.assertRaises(ValueError):oscillator(dt=1)


class SolarTests(unittest.TestCase):
    def test_constant_power_known_energy(self):
        rows=[dict(time_s=0,voltage_V=5,current_A=.2),dict(time_s=3600,voltage_V=5,current_A=.2)]
        self.assertAlmostEqual(integrate_power(rows),1)

    def test_linear_ramp(self):
        rows=[dict(time_s=0,voltage_V=5,current_A=0),dict(time_s=3600,voltage_V=5,current_A=.4)]
        self.assertAlmostEqual(integrate_power(rows),1)

    def test_invalid_or_duplicate_readings(self):
        good=dict(time_s=0,voltage_V=5,current_A=.1)
        for rows in [[good],[good,good],[good,dict(time_s=1,voltage_V=-5,current_A=.1)],
                     [good,dict(time_s=1,voltage_V=5,current_A=math.nan)]]:
            with self.assertRaises(ValueError):integrate_power(rows)


class ControllerTests(unittest.TestCase):
    def test_step_and_bounds(self):
        self.assertAlmostEqual(controller_step(.15,.16,.15),.151)
        self.assertEqual(controller_step(.18,1,0),.18)
        self.assertEqual(controller_step(.12,0,1),.12)

    def test_invalid_reading(self):
        with self.assertRaises(ValueError):controller_step(.15,.16,math.nan)


if __name__=='__main__':unittest.main()
