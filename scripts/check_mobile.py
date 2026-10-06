"""Check mobile app assets, course parity, manifest and offline cache coverage."""
from pathlib import Path
from html.parser import HTMLParser
import json,re,sys,struct
ROOT=Path(__file__).resolve().parents[1];APP=ROOT/'app'
sys.path.insert(0,str(ROOT/'scripts'))
from course_data import LESSONS

def main():
 data=json.loads((APP/'data.json').read_text());assert len(data['lessons'])==48
 for i,(l,source) in enumerate(zip(data['lessons'],LESSONS)):
  assert l['id']==i+1
  for field in ['title','objective','concept','worked','materials','steps','expected','pitfall','questions','answers','artifact','lab']:assert l[field]==source[field],f'course mismatch: {i+1} {field}'
  assert len(set(l['mobileQuiz']['options']))==3
 manifest=json.loads((APP/'manifest.webmanifest').read_text());assert manifest['display']=='standalone';assert manifest['start_url']=='./';assert manifest['scope']=='./'
 for icon in manifest['icons']:
  p=APP/icon['src'];raw=p.read_bytes();assert raw[:8]==b'\x89PNG\r\n\x1a\n';width,height=struct.unpack('>II',raw[16:24]);assert f'{width}x{height}'==icon['sizes']
 class HTML(HTMLParser):
  def handle_starttag(self,tag,attrs):
   attrs=dict(attrs)
   for key in ['href','src']:
    value=attrs.get(key)
    if value and not value.startswith(('http:','https:','data:','#')):assert (APP/value).is_file(),value
 HTML().feed((APP/'index.html').read_text())
 precache=(APP/'precache.js').read_text();assets=json.loads(re.search(r'self.APP_ASSETS=(.*);',precache).group(1));assert './data.json' in assets
 for asset in assets:
  if asset=='./':continue
  assert (APP/asset).is_file(),asset
  assert not asset.startswith(('http:','https:'))
 for name in ['index.html','app.css','app.js','models.js','manifest.webmanifest','data.json']:
  assert './'+name in assets
 assert 'localStorage' in (APP/'app.js').read_text()
 print(f'PASS: 48 mobile lessons match the course; 48 quizzes, PNG icons, install manifest, {len(assets)} offline assets and HTML links checked.')

if __name__=='__main__':main()
