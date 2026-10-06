/* Educational models in SI units. No engineering approval or hardware control. */
(function(root){
'use strict';
function finite(x,name){if(!Number.isFinite(x))throw Error(name+' must be a finite number');return x;}
function positive(x,name){finite(x,name);if(x<=0)throw Error(name+' must be positive');return x;}
function nullspace(matrix,tol=1e-10){
  if(!matrix.length||!matrix[0].length||matrix.some(r=>r.length!==matrix[0].length))throw Error('Invalid matrix');
  let scale=Math.max(...matrix.flat().map(x=>Math.abs(finite(x,'Matrix entry'))));
  const n=matrix[0].length;
  if(!scale)return Array.from({length:n},(_,j)=>Array.from({length:n},(_,i)=>+(i===j)));
  let a=matrix.map(r=>r.map(x=>x/scale)),row=0,pivots=[];
  for(let c=0;c<n&&row<a.length;c++){
    let p=row;for(let r=row+1;r<a.length;r++)if(Math.abs(a[r][c])>Math.abs(a[p][c]))p=r;
    if(Math.abs(a[p][c])<=tol)continue;
    [a[row],a[p]]=[a[p],a[row]];const divisor=a[row][c];a[row]=a[row].map(x=>x/divisor);
    for(let r=0;r<a.length;r++)if(r!==row){let factor=a[r][c];a[r]=a[r].map((x,i)=>x-factor*a[row][i]);}
    pivots.push(c);row++;
  }
  let basis=[];for(let f=0;f<n;f++)if(!pivots.includes(f)){let v=Array(n).fill(0);v[f]=1;pivots.forEach((p,r)=>v[p]=-a[r][f]);basis.push(v);}return basis;
}
function prism(radius=.08,height=.14,twist=30){
  positive(radius,'Radius');positive(height,'Height');finite(twist,'Twist');
  let alpha=twist*Math.PI/180;
  const nodes=Array.from({length:6},(_,i)=>{let a=2*Math.PI*i/3+(i>=3?alpha:0);return [radius*Math.cos(a),radius*Math.sin(a),i>=3?height:0];});
  const members=[];
  for(let i=0;i<3;i++)members.push({name:'B'+i,a:i,b:(i+1)%3,kind:'cable'});
  for(let i=0;i<3;i++)members.push({name:'T'+i,a:i+3,b:(i+1)%3+3,kind:'cable'});
  for(let i=0;i<3;i++)members.push({name:'C'+i,a:i,b:i+3,kind:'cable'});
  for(let i=0;i<3;i++)members.push({name:'S'+i,a:i,b:(i+1)%3+3,kind:'strut'});
  let A=Array.from({length:18},()=>Array(12).fill(0));
  members.forEach((m,j)=>{m.length=Math.hypot(...nodes[m.b].map((v,k)=>v-nodes[m.a][k]));for(let k=0;k<3;k++){let d=nodes[m.b][k]-nodes[m.a][k];A[3*m.a+k][j]=d;A[3*m.b+k][j]=-d;}});
  const q=[...Array(6).fill(1/Math.sqrt(3)),...Array(3).fill(1),...Array(3).fill(-1)];
  const residual=Math.max(...A.map(r=>Math.abs(r.reduce((s,x,i)=>s+x*q[i],0))));
  return {nodes,members,q,residual,nullity:nullspace(A).length};
}
function spring(k,L,L0){positive(k,'Stiffness');positive(L,'Length');positive(L0,'Rest length');return k*Math.max(0,L-L0);}
function buckling(E,I,L,K=1){[E,I,L,K].forEach((v,i)=>positive(v,['E','I','L','K'][i]));return Math.PI**2*E*I/(K*L)**2;}
function oscillator(m=1,k=4,c=.4,duration=5,dt=.01){
  positive(m,'Mass');positive(k,'Stiffness');finite(c,'Damping');if(c<0)throw Error('Damping cannot be negative');positive(duration,'Duration');positive(dt,'Time step');
  if(dt*Math.sqrt(k/m)>.2||duration/dt>100000)throw Error('Time step outside teaching range');
  let t=0,x=.01,v=0,rows=[];const f=(x,v)=>[v,-(c*v+k*x)/m];
  const record=()=>rows.push({time:t,x,v,energy:.5*m*v*v+.5*k*x*x});record();
  while(t<duration-1e-12){let h=Math.min(dt,duration-t);let [a,b]=f(x,v),[d,e]=f(x+h*a/2,v+h*b/2),[g,j]=f(x+h*d/2,v+h*e/2),[p,q]=f(x+h*g,v+h*j);x+=h*(a+2*d+2*g+p)/6;v+=h*(b+2*e+2*j+q)/6;t+=h;record();}return rows;
}
function energy(rows){
  if(rows.length<2)throw Error('Enter at least two readings');let previous=null,total=0;
  for(const r of rows){let t=Number(r.time_s),v=Number(r.voltage_V),i=Number(r.current_A);[t,v,i].forEach(x=>finite(x,'Reading'));if(t<0||v<0||i<0)throw Error('Readings cannot be negative');if(previous&&t<=previous.t)throw Error('Time must strictly increase');let power=v*i;if(previous)total+=(t-previous.t)*(power+previous.power)/2;previous={t,power};}return total/3600;
}
function parseSolar(text){
  const lines=text.trim().split(/\r?\n/).filter(l=>l.trim());
  if(lines[0]?.replace(/\s/g,'')!=='time_s,voltage_V,current_A')throw Error('Use the header time_s,voltage_V,current_A');
  return lines.slice(1).map((line,i)=>{const cells=line.split(',').map(x=>x.trim());if(cells.length!==3||cells.some(x=>x===''))throw Error('Three readings are required on row '+(i+2));return {time_s:Number(cells[0]),voltage_V:Number(cells[1]),current_A:Number(cells[2])};});
}
function step(current,target,reading,gain=.2,maxStep=.001,lower=.12,upper=.18){
  [current,target,reading,gain,maxStep,lower,upper].forEach(x=>finite(x,'Controller input'));positive(gain,'Gain');positive(maxStep,'Step');if(lower>=upper||current<lower||current>upper)throw Error('Invalid length bounds');return Math.max(lower,Math.min(upper,current+Math.max(-maxStep,Math.min(maxStep,gain*(target-reading)))));
}
function controller(target=.16,gain=.2){let current=.15,rows=[];for(let i=0;i<20;i++){let reading=current;current=step(current,target,reading,gain);rows.push({time:i,x:current,reading});}return rows;}
const api={prism,nullspace,spring,buckling,oscillator,energy,parseSolar,step,controller};
if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.TensegrityModels=api;
})(typeof globalThis!=='undefined'?globalThis:this);
