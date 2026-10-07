const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const APP=fs.existsSync('dist/index.html')?'dist':'app';
const listeners={},storage=new Map(),elements={};
const document={addEventListener:(k,f)=>(listeners[k]??=[]).push(f),querySelector:k=>elements[k],createElement:()=>({click(){}})};
const ctx={document,window:{},localStorage:{getItem:k=>storage.get(k),setItem:(k,v)=>storage.set(k,v)},location:{hash:'#assistant/plan'},navigator:{},Blob,URL,setTimeout(){},Date};vm.createContext(ctx);vm.runInContext(fs.readFileSync(APP+'/assistant.js','utf8'),ctx);
const t=ctx.window.TensegrityTeaching,course=JSON.parse(fs.readFileSync(APP+'/data.json'));let html='';const bridge={course,refresh:()=>{html=t.render(bridge,ctx.location.hash.slice(1).split('/').slice(1).join('/'));}};
const click=async(action,extras={})=>{for(const f of listeners.click)await f({target:{closest:()=>({dataset:{teach:action,...extras}})}});};
const change=async(id,value)=>{for(const f of listeners.change)await f({target:{id,value}});};
(async()=>{
 for(const tool of ['plan','coach','quiz','review','adapt','experiment']){html=t.render(bridge,tool);assert(html.includes('id="teaching-assistant"'));assert(!html.includes('undefined'));}
 html=t.render(bridge,'plan/10');assert(html.includes('Build a three-strut prism'));let mins=[...html.matchAll(/<td>(\d+)–(\d+)<\/td>/g)];assert.equal(mins.reduce((a,x)=>a+Number(x[2])-Number(x[1]),0),60);
 await change('teach-duration','45');mins=[...html.matchAll(/<td>(\d+)–(\d+)<\/td>/g)];assert.equal(mins.reduce((a,x)=>a+Number(x[2])-Number(x[1]),0),45);
 await change('teach-language','zh');assert(html.includes('把课程变成实践'));html=t.render(bridge,'quiz');assert(!html.includes('class="feedback'));ctx.location.hash='#assistant/quiz';await click('answer',{key:'basic-0',choice:'0'});assert(html.includes('正确。'));
 html=t.render(bridge,'coach');ctx.location.hash='#assistant/coach';elements['#teach-observation']={value:'Joint witness mark unchanged'};await click('coach-next');assert(html.includes('步骤 2 / 8'));assert.equal(JSON.parse(storage.get('tensegrity.teach.v1')).observations[0],'Joint witness mark unchanged');
 ctx.location.hash='#assistant/review';html=t.render(bridge,'review');elements['#teach-learner']={value:'<img src=x onerror=evil()>'};elements['#teach-evidence']={value:'Identified cable tension with visual prompt.'};elements['#teach-support']={value:'visual'};[0,1,2,3].forEach(i=>elements['#teach-rating-'+i]={value:i===0?'1':''});elements['#assistant-status']={textContent:''};for(const f of listeners.submit)f({target:{id:'teach-review-form'},preventDefault(){}});assert(html.includes('1/4'));assert(html.includes('1.00'));assert(html.includes('&lt;img'));assert(!html.includes('<img src=x'));const saved=JSON.parse(storage.get('tensegrity.teach.v1'));assert.equal(saved.reviews[0].ratings[1],null);assert.equal(saved.reviews[0].support,'visual');
 assert.equal(t.summary({ratings:[null,null,null,null]}).average,null);assert.equal(t.summary({ratings:[0,null,2,null]}).average,1);
 assert.throws(()=>t.validate({...saved,reviews:[{...saved.reviews[0],ratings:[9,null,null,null]}]}));assert.equal(t.validate(saved).reviews.length,1);
 const idx=fs.readFileSync(APP+'/index.html','utf8');assert(idx.includes('data-nav="assistant"'));assert(idx.indexOf('assistant.js')<idx.indexOf('app.js'));const app=fs.readFileSync(APP+'/app.js','utf8');assert(app.includes('window.TensegrityTeaching.render'));assert(app.includes('#assistant/plan/'));
 const cache={};vm.runInNewContext(fs.readFileSync(APP+'/precache.js','utf8'),{self:cache});for(const file of cache.APP_ASSETS)if(file!=='./')assert(fs.existsSync(APP+'/'+file.slice(2)),file);assert(cache.APP_ASSETS.includes('./assistant.js'));assert(cache.APP_ASSETS.includes('./assistant.css'));
 console.log('PASS: six screens; contextual lesson routing; 45/60-minute plans; Chinese controls; answer reveal; coach save; sparse review averages; output escaping; backup rejection and roundtrip; offline asset coverage.');
})().catch(e=>{console.error(e);process.exitCode=1;});
