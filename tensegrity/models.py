"""Transparent educational mechanics. Length m, force N, time s.

The prism is a pin-jointed idealization. Force densities q=F/L use positive
tension, negative compression. Elastic stability is not computed here.
"""
from dataclasses import dataclass
import math


def positive(value, name):
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f'{name} must be finite and positive')
    return value


@dataclass(frozen=True)
class Member:
    name: str
    a: int
    b: int
    kind: str


def prism(radius=.08, height=.14, twist_degrees=30.):
    positive(radius, 'radius'); positive(height, 'height')
    if not math.isfinite(twist_degrees):
        raise ValueError('twist must be finite')
    angle = math.radians(twist_degrees)
    nodes = [(radius*math.cos(2*math.pi*i/3 + (angle if i >= 3 else 0)),
              radius*math.sin(2*math.pi*i/3 + (angle if i >= 3 else 0)),
              height if i >= 3 else 0.) for i in range(6)]
    members = [Member(f'B{i}', i, (i+1)%3, 'cable') for i in range(3)]
    members += [Member(f'T{i}', i+3, (i+1)%3+3, 'cable') for i in range(3)]
    members += [Member(f'C{i}', i, i+3, 'cable') for i in range(3)]
    members += [Member(f'S{i}', i, (i+1)%3+3, 'strut') for i in range(3)]
    return nodes, members


def lengths(nodes, members):
    return [math.dist(nodes[m.a], nodes[m.b]) for m in members]


def equilibrium_matrix(nodes, members):
    """18 by 12 force-density matrix for the free six-node prism.

    At node a the column is x_b-x_a; at b its negative. A q = 0 describes
    unloaded self-stress. This is not the unit-direction force matrix.
    """
    matrix = [[0.]*len(members) for _ in range(3*len(nodes))]
    for j, m in enumerate(members):
        for k in range(3):
            d = nodes[m.b][k]-nodes[m.a][k]
            matrix[3*m.a+k][j] = d
            matrix[3*m.b+k][j] = -d
    return matrix


def nullspace(matrix, relative_tolerance=1e-10):
    """RREF basis; intended for tiny instructional systems, not large solvers."""
    if not matrix or not matrix[0] or any(len(r) != len(matrix[0]) for r in matrix):
        raise ValueError('matrix must be nonempty and rectangular')
    if any(not math.isfinite(x) for row in matrix for x in row):
        raise ValueError('matrix contains nonfinite values')
    positive(relative_tolerance, 'relative tolerance')
    a = [list(map(float, r)) for r in matrix]
    scale = max(abs(x) for row in a for x in row)
    if scale == 0:
        return [[float(i == j) for i in range(len(a[0]))] for j in range(len(a[0]))]
    a = [[x/scale for x in row] for row in a]
    nr, nc = len(a), len(a[0]); pivots = []; row = 0
    for col in range(nc):
        if row >= nr: break
        p = max(range(row, nr), key=lambda r: abs(a[r][col]))
        if abs(a[p][col]) <= relative_tolerance: continue
        a[row], a[p] = a[p], a[row]
        pivot = a[row][col]
        a[row] = [x/pivot for x in a[row]]
        for r in range(nr):
            if r != row:
                c = a[r][col]
                a[r] = [x-c*y for x, y in zip(a[r], a[row])]
        pivots.append(col); row += 1
    basis = []
    for f in range(nc):
        if f in pivots: continue
        v = [0.]*nc; v[f] = 1.
        for r, p in enumerate(pivots): v[p] = -a[r][f]
        basis.append(v)
    return basis


def analytic_self_stress(cross_density=1.):
    """Only valid for our topology at a 30-degree twist; N/m."""
    positive(cross_density, 'cross force density')
    return [cross_density/math.sqrt(3)]*6 + [cross_density]*3 + [-cross_density]*3


def residual(matrix, vector):
    if not matrix or any(len(r) != len(vector) for r in matrix):
        raise ValueError('incompatible dimensions')
    return [sum(x*y for x, y in zip(row, vector)) for row in matrix]


def max_residual(matrix, vector):
    return max(abs(x) for x in residual(matrix, vector))


def cable_force(stiffness, length, rest_length):
    """Unilateral linear spring: zero force when shorter than rest length."""
    positive(stiffness, 'stiffness'); positive(length, 'length'); positive(rest_length, 'rest length')
    return stiffness*max(0., length-rest_length)


def euler_load(modulus, second_moment, length, effective_length_factor=1.):
    """Ideal Euler buckling load; not a material or joint failure calculation."""
    for x, name in [(modulus,'E'), (second_moment,'I'), (length,'L'), (effective_length_factor,'K')]:
        positive(x, name)
    return math.pi**2*modulus*second_moment/(effective_length_factor*length)**2


def oscillator(mass=1., stiffness=4., damping=.4, x0=.01, v0=0., duration=5., dt=.01):
    """RK4 integration of m*x''+c*x'+k*x=0; one DOF, not a tensegrity solver."""
    positive(mass,'mass'); positive(stiffness,'stiffness'); positive(duration,'duration'); positive(dt,'dt')
    if not math.isfinite(damping) or damping < 0 or not all(math.isfinite(x) for x in [x0,v0]):
        raise ValueError('invalid damping or initial state')
    if dt*math.sqrt(stiffness/mass) > .2:
        raise ValueError('dt too large for this educational oscillator')
    if duration/dt > 1_000_000:
        raise ValueError('too many time steps')
    def f(x,v): return v, -(damping*v+stiffness*x)/mass
    t=0.; x=x0; v=v0; result=[]
    def record(): result.append({'time_s':t,'displacement_m':x,'velocity_m_s':v,'energy_J':.5*mass*v*v+.5*stiffness*x*x})
    record()
    while t < duration-1e-12:
        h=min(dt,duration-t)
        a,b=f(x,v); c,d=f(x+h*a/2,v+h*b/2); e,g=f(x+h*c/2,v+h*d/2); p,q=f(x+h*e,v+h*g)
        x += h*(a+2*c+2*e+p)/6; v += h*(b+2*d+2*g+q)/6; t += h; record()
    return result


def integrate_power(rows):
    """Trapezoidal energy Wh from simultaneous loaded V,I readings and seconds.

    Caller verifies readings describe the same circuit operating point.
    """
    if len(rows) < 2: raise ValueError('at least two readings required')
    cleaned=[]
    for r in rows:
        t,v,i = (float(r[k]) for k in ['time_s','voltage_V','current_A'])
        if not all(math.isfinite(x) for x in [t,v,i]) or t < 0 or v < 0 or i < 0:
            raise ValueError('nonfinite or negative PV reading')
        if cleaned and t <= cleaned[-1][0]: raise ValueError('time must strictly increase')
        cleaned.append((t,v*i))
    return sum((b[0]-a[0])*(a[1]+b[1])/2 for a,b in zip(cleaned,cleaned[1:]))/3600


def controller_step(current, target, reading, gain=.2, max_step=.001, lower=.12, upper=.18):
    """Bounded simulated length adjustment. Hardware limits are not implemented."""
    if not all(math.isfinite(x) for x in [current,target,reading,gain,max_step,lower,upper]):
        raise ValueError('controller inputs must be finite')
    positive(gain,'gain'); positive(max_step,'max step')
    if lower >= upper or not lower <= current <= upper: raise ValueError('invalid length bounds')
    delta = max(-max_step, min(max_step, gain*(target-reading)))
    return max(lower,min(upper,current+delta))
