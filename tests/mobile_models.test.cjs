const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const M=require('../app/models.js');
const near=(a,b,tol=1e-10)=>assert.ok(Math.abs(a-b)<tol,`${a} differs from ${b}`);

test('prism lengths match independent closed forms',()=>{let r=M.prism();near(r.members[0].length,Math.sqrt(3)*.08);near(r.members[6].length,Math.sqrt(.14**2+(2-Math.sqrt(3))*.08**2));near(r.members[9].length,Math.sqrt(.14**2+(2+Math.sqrt(3))*.08**2));assert.equal(r.nullity,1);assert.ok(r.residual<1e-12);assert.ok(r.q.slice(0,9).every(x=>x>0));assert.ok(r.q.slice(9).every(x=>x<0));});
test('arbitrary twist does not balance the reference state',()=>{let r=M.prism(.08,.14,45);assert.equal(r.nullity,0);assert.ok(r.residual>.001);assert.throws(()=>M.prism(0,.14,30));});
test('tiny and large matrix scaling preserve known nullspace',()=>{for(const scale of [1e-12,1,1e12])assert.equal(M.nullspace([[scale,2*scale,3*scale],[2*scale,4*scale,6*scale]]).length,2);});
test('cable cannot push',()=>{near(M.spring(100,.15,.14),1);near(M.spring(100,.13,.14),0);assert.throws(()=>M.spring(-1,.15,.14));});
test('ideal Euler load has inverse square length dependence',()=>{near(M.buckling(2e9,1e-10,.2),49.34802200544678);near(M.buckling(2e9,1e-10,.4),M.buckling(2e9,1e-10,.2)/4);assert.throws(()=>M.buckling(1,0,.2));});
test('undamped oscillator matches cosine and known energy',()=>{let rows=M.oscillator(1,4,0);for(const r of rows){near(r.x,.01*Math.cos(2*r.time),2e-10);near(r.energy,.0002,1e-11);}});
test('positive damping dissipates energy',()=>{let rows=M.oscillator();for(let i=1;i<rows.length;i++)assert.ok(rows[i].energy<=rows[i-1].energy+1e-12);assert.throws(()=>M.oscillator(1,4,-1));});
test('solar integrator checks operating power and time order',()=>{let rows=M.parseSolar('time_s,voltage_V,current_A\n0,5,.1\n60,5,.12\n120,5,.1');near(M.energy(rows),.018333333333333333);near(M.energy([{time_s:0,voltage_V:5,current_A:.2},{time_s:3600,voltage_V:5,current_A:.2}]),1);assert.throws(()=>M.parseSolar('time_s,voltage_V,current_A\n0,,.1'));assert.throws(()=>M.energy([rows[0],rows[0]]));assert.throws(()=>M.energy([{time_s:0,voltage_V:5,current_A:.1},{time_s:1,voltage_V:NaN,current_A:.1}]));});
test('mock control applies step and length bounds',()=>{near(M.step(.15,.16,.15),.151);assert.equal(M.step(.18,1,0),.18);assert.equal(M.step(.12,0,1),.12);assert.throws(()=>M.step(.15,.16,NaN));});
test('all 48 lessons have independent quiz choices and correct answer keys',()=>{let data=JSON.parse(fs.readFileSync(path.join(__dirname,'../app/data.json')));assert.equal(data.lessons.length,48);for(const l of data.lessons){assert.equal(l.mobileQuiz.options.length,3);assert.equal(new Set(l.mobileQuiz.options).size,3);assert.ok(l.mobileQuiz.correct>=0&&l.mobileQuiz.correct<=2);assert.equal(l.questions.length,3);assert.equal(l.answers.length,3);assert.ok(l.mobileQuiz.options[l.mobileQuiz.correct].trim().length>0);}assert.equal(data.routes['full-core'].length,12);});
