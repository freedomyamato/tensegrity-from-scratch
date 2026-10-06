const {test}=require('node:test');
const assert=require('node:assert/strict');
const vm=require('node:vm');
const fs=require('node:fs');
const path=require('node:path');

test('service worker installs complete cache and serves course while offline',async()=>{
 const events={},stores=new Map(),scope='https://example.test/app/';let claimed=false;
 const cacheFor=name=>{if(!stores.has(name))stores.set(name,new Map());const map=stores.get(name);return {
  async addAll(urls){for(const url of urls)map.set(url,{url,body:url.endsWith('data.json')?'course':'asset'});},
  async match(request){const key=typeof request==='string'?request:request.url;return map.get(key);}
 };};
 const context=vm.createContext({URL,caches:{open:async name=>cacheFor(name),keys:async()=>[...stores.keys()],delete:async name=>stores.delete(name)},fetch:async()=>{throw Error('offline');}});
 context.self={registration:{scope},location:{origin:'https://example.test'},clients:{claim:async()=>{claimed=true;}},skipWaiting:async()=>{},addEventListener:(name,fn)=>events[name]=fn};
 context.importScripts=()=>vm.runInContext(fs.readFileSync(path.join(__dirname,'../app/precache.js'),'utf8'),context);
 vm.runInContext(fs.readFileSync(path.join(__dirname,'../app/sw.js'),'utf8'),context);
 let promise;events.install({waitUntil:p=>promise=p});await promise;
 stores.set('another-app-cache',new Map());events.activate({waitUntil:p=>promise=p});await promise;assert.ok(claimed);assert.ok(stores.has('another-app-cache'));
 let response;events.fetch({request:{method:'GET',url:scope+'data.json',mode:'cors'},respondWith:p=>response=p});assert.equal((await response).body,'course');
 events.fetch({request:{method:'GET',url:scope+'lesson/16',mode:'navigate'},respondWith:p=>response=p});assert.equal((await response).url,scope+'index.html');
 let status;events.message({data:{type:'OFFLINE_STATUS'},ports:[{postMessage:s=>status=s}],waitUntil:p=>promise=p});await promise;assert.equal(status.ready,true);
 const appStore=[...stores.entries()].find(([key])=>key.startsWith('tensegrity-mobile-'))[1];appStore.delete(scope+'data.json');
 events.message({data:{type:'OFFLINE_STATUS'},ports:[{postMessage:s=>status=s}],waitUntil:p=>promise=p});await promise;assert.equal(status.ready,false);
});
