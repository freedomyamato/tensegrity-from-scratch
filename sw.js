/* Cache only this app's published assets. No external references or user notes. */
importScripts('./precache.js');
const PREFIX='tensegrity-mobile-'+self.registration.scope.replace(/[^a-z0-9]/gi,'-')+'-';
const CACHE=PREFIX+self.APP_CACHE_VERSION;
const URLS=self.APP_ASSETS.map(path=>new URL(path,self.registration.scope).href);
self.addEventListener('install',event=>event.waitUntil((async()=>{const cache=await caches.open(CACHE);await cache.addAll(URLS);await self.skipWaiting();})()));
self.addEventListener('activate',event=>event.waitUntil((async()=>{for(const name of await caches.keys())if(name.startsWith(PREFIX)&&name!==CACHE)await caches.delete(name);await self.clients.claim();})()));
self.addEventListener('fetch',event=>{
 const url=new URL(event.request.url);if(event.request.method!=='GET'||url.origin!==self.location.origin||!url.href.startsWith(self.registration.scope))return;
 event.respondWith((async()=>{const cache=await caches.open(CACHE);if(event.request.mode==='navigate'){try{const live=await fetch(event.request);if(live.ok)return live;}catch(error){}const response=await cache.match(new URL('./index.html',self.registration.scope).href);if(response)return response;}const cached=await cache.match(event.request,{ignoreSearch:true});if(cached)return cached;return fetch(event.request);})());
});
self.addEventListener('message',event=>{if(event.data?.type==='OFFLINE_STATUS')event.waitUntil((async()=>{const cache=await caches.open(CACHE);let ready=true;for(const url of URLS)if(!await cache.match(url)){ready=false;break;}event.ports[0]?.postMessage({ready,version:self.APP_CACHE_VERSION});})());});
