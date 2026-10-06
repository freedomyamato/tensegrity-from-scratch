"""Run from the repository root: python3 -m tensegrity prism."""
import argparse
import csv
import json
import math
from pathlib import Path
from .models import (prism, lengths, equilibrium_matrix, nullspace,
                     analytic_self_stress, max_residual, cable_force,
                     euler_load, oscillator, integrate_power, controller_step)


def write_csv(path, rows):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    with open(path,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def main():
    p=argparse.ArgumentParser(description='Educational mechanics; SI units. No deployment certification.')
    sub=p.add_subparsers(dest='lab',required=True)
    q=sub.add_parser('prism'); q.add_argument('--radius',type=float,default=.08); q.add_argument('--height',type=float,default=.14); q.add_argument('--twist',type=float,default=30); q.add_argument('--output',default='outputs/prism.json')
    q=sub.add_parser('sweep'); q.add_argument('--output',default='outputs/twist-sweep.csv')
    q=sub.add_parser('spring'); q.add_argument('--stiffness',type=float,default=100); q.add_argument('--length',type=float,default=.15); q.add_argument('--rest-length',type=float,default=.14)
    q=sub.add_parser('buckling'); q.add_argument('--E',type=float,default=2e9); q.add_argument('--I',type=float,default=1e-10); q.add_argument('--length',type=float,default=.2); q.add_argument('--K',type=float,default=1)
    q=sub.add_parser('oscillator'); q.add_argument('--damping',type=float,default=.4); q.add_argument('--output',default='outputs/oscillator.csv')
    q=sub.add_parser('solar'); q.add_argument('input',nargs='?',default='examples/solar_readings.csv')
    q=sub.add_parser('controller'); q.add_argument('--output',default='outputs/controller.csv')
    a=p.parse_args()
    try:
        if a.lab=='prism':
            nodes,members=prism(a.radius,a.height,a.twist); lens=lengths(nodes,members); A=equilibrium_matrix(nodes,members); basis=nullspace(A)
            data={'units':{'length':'m','force_density':'N/m'},'twist_degrees':a.twist,'nodes':nodes,'members':[dict(name=m.name,a=m.a,b=m.b,kind=m.kind,length_m=l) for m,l in zip(members,lens)],'nullspace_dimension':len(basis),'nullspace_basis':basis,'note':'Self-stress equilibrium is not a stability test. Physical assembly has not been validated.'}
            if math.isclose(a.twist%360,30,abs_tol=1e-9):
                q=analytic_self_stress(); data['example_force_density']=q; data['example_member_force_N']=[x*l for x,l in zip(q,lens)]; data['max_nodal_residual_N']=max_residual(A,q)
            Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(data,indent=2)+'\n')
            print(json.dumps(data,indent=2))
        elif a.lab=='sweep':
            rows=[]
            for angle in [0,15,25,29,30,31,35,45,60]:
                n,m=prism(twist_degrees=angle); A=equilibrium_matrix(n,m)
                rows.append({'twist_degrees':angle,'nullspace_dimension':len(nullspace(A)),'reference_q_residual_N':max_residual(A,analytic_self_stress())})
            write_csv(a.output,rows); print(a.output)
        elif a.lab=='spring': print(f'cable force = {cable_force(a.stiffness,a.length,a.rest_length):.6g} N')
        elif a.lab=='buckling': print(f'ideal Euler load = {euler_load(a.E,a.I,a.length,a.K):.6g} N (idealization only)')
        elif a.lab=='oscillator': write_csv(a.output,oscillator(damping=a.damping)); print(a.output)
        elif a.lab=='solar':
            with open(a.input,newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
            print(f'energy over recorded interval = {integrate_power(rows):.8g} Wh')
        else:
            current=.15; rows=[]
            for t in range(20):
                reading=current; current=controller_step(current,.16,reading)
                rows.append({'step':t,'mock_reading_m':reading,'next_length_m':current})
            write_csv(a.output,rows); print(a.output+' (mock plant; no hardware connection)')
    except (ValueError,OSError,KeyError) as exc: p.error(str(exc))


if __name__=='__main__': main()
