"""Build course data and offline assets into app/; optionally copy to a Site dist.

Run: python3 scripts/build_mobile.py
     python3 scripts/build_mobile.py --site-dist /absolute/path/to/dist
UI sources live in app/. No third-party runtime dependencies.
"""
from pathlib import Path
import argparse
import sys
import json
import shutil
import hashlib
import re
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from course_data import LESSONS,PHASES

# One explicitly authored multiple-choice knowledge check per lesson.
# Existing three-question teach-back checks and model answers remain available.
QUIZZES=[
('A named action and observable artifact.','An impressive-sounding topic.','A promise without a measurable outcome.'),
('Knots and attachments consume additional length.','A ruler always measures force.','Node spans are independent of joints.'),
('No; repeated measurements can share a bias.','Yes; repeatability guarantees accuracy.','Only if the readings have many decimal places.'),
('Before testing.','After adjusting the design to match the result.','Only after the observation is known.'),
('No; in this ideal model it becomes slack.','Yes; it carries compression like a rigid strut.','Yes; tightening it makes it push.'),
('Into the table and its supports.','Nowhere; internal tension cancels gravity.','Only into the highest cable.'),
('Internal member forces balanced without external loads.','Any load applied to a roof.','The weight of the model alone.'),
('The definition being applied.','Whether the product is advertised as floating.','Only its color and appearance.'),
('Nine cables.','Three cables.','Twelve cables.'),
('To accommodate joints and gently tune geometry.','To create the greatest possible tension.','To eliminate the need for node labels.'),
('No, when radius is fixed.','Yes; triangle edge length is equal to height.','Yes; it doubles for any height increase.'),
('Named parts, endpoint labels and an observable check.','A photo without labels.','A command to make it look right.'),
('0.14 m.','1.4 m.','14 m.'),
('Toward its other endpoint.','Away from its other endpoint.','Always vertically downward.'),
('N·m.','N/m.','kg/m³.'),
('Axial force divided by member length.','Axial force multiplied by member length.','Member mass divided by time.'),
('N/m.','N·m.','m/N.'),
('The ideal Euler load becomes one quarter.','The ideal load doubles.','The ideal load stays unchanged.'),
('Relative slip at an attachment.','The exact breaking strength.','The strut’s elastic modulus.'),
('Repeated loading cycles and material response.','Only the first static loading event.','The number of labels attached.'),
('Distance from the central axis to a node.','The distance between adjacent nodes.','The total strut length.'),
('18 rows by 12 columns.','6 rows by 3 columns.','12 rows by 18 columns.'),
('The top-triangle twist.','Every material property at once.','The entire roof and electrical system.'),
('Checking implementation against equations or known results.','Comparing with independent physical measurements.','Declaring a design approved for public use.'),
('It dissipates mechanical energy in this model.','It creates energy without an input.','It removes the need for mass and stiffness.'),
('It becomes four times larger.','It becomes twice as large.','It becomes one quarter.'),
('With the square of wind speed.','Linearly with wind speed.','Independently of wind speed.'),
('No; the connectivity and equilibrium problem change.','Yes; missing members have no effect.','Yes; the appearance is sufficient evidence.'),
('Simultaneous loaded voltage and current at the same operating point.','Open-circuit voltage times short-circuit current.','Voltage alone without a load.'),
('Through defined attachments into the building.','Into the air without support reactions.','Only around the internal cables.'),
('No; flotation is a separate subsystem.','Yes; tensegrity automatically creates buoyancy.','Only if its rods are colored blue.'),
('The task, baseline, metrics and methods.','The winning design regardless of evidence.','Only the final advertising claim.'),
('A defined stable datum, such as the same tabletop.','Any different surface in each trial.','No reference is needed.'),
('200 counts per newton.','20 counts per newton.','210 newtons per count.'),
('0.151 m.','0.160 m.','0.152 m without applying the step limit.'),
('0.14 m.','1.4 m.','14 m.'),
('Labels remain meaningful without color.','Labels guarantee every physical joint is safe.','Only color is sufficient for everyone.'),
('No; knot tying and structural understanding are different tasks.','Yes; knot difficulty proves poor understanding.','Only spoken explanations count.'),
('Yes; 139 mm lies within 140 ± 2 mm.','No; only exactly 140 mm passes.','No; every specimen must be over 142 mm.'),
('Specific observed evidence.','A diagnosis inferred without support.','A judgment about the learner’s worth.'),
('Traceable feedback rather than a designer’s assumption.','A fictional quote presented as a real survey.','An attractive rendering alone.'),
('Different decisions affecting requirements or tradeoffs.','Only different colors.','All concepts having identical constraints and structure.'),
('They are real resource use.','They guarantee the project is profitable.','They replace the need for a maintenance owner.'),
('Scope, loads, users and required review.','Only the name prototype or product.','Whether the model looks impressive.'),
('Design, comparator, metric and conditions.','Only a broad slogan about efficiency.','Only the desired result.'),
('To reduce systematic effects of time or order drift.','To delete inconvenient trials.','To guarantee statistical significance.'),
('Variation, outliers and missing or failed trials.','A full stability proof.','All uncontrolled differences automatically.'),
('Another person reproduces a specified task using the instructions.','The author says the model looks correct.','A rendered image without methods or data.')
]

def main():
 p=argparse.ArgumentParser();p.add_argument('--site-dist');a=p.parse_args();app=ROOT/'app'
 for filename in ['index.html','app.css','app.js','models.js','sw.js']:
  if not (app/filename).is_file():raise ValueError('Missing app source '+filename)
 route_data=json.loads((ROOT/'learning-paths/routes.json').read_text())
 data={'version':'2.0.0','phases':[{'id':i,'title':title,'hours':h} for i,(_,title,h) in enumerate(PHASES)],'routes':route_data['routes'],
       'routeNames':{'solar-builder':'Solar sculpture builder','community-facilitator':'Community facilitator','prototype-technician':'Prototype technician','robotics':'Robotics study','research':'Research explorer','full-core':'Full course'},'lessons':[],'resources':[]}
 for i,l in enumerate(LESSONS):
  options=list(QUIZZES[i]);correct=(i+1)%3;options.insert(correct,options.pop(0))
  item=dict(l);item.update(id=i+1,phase=i//4,mobileQuiz={'question':l['questions'][0],'options':options,'correct':correct,'explanation':l['answers'][0]})
  data['lessons'].append(item)
 (app/'assets').mkdir(exist_ok=True)
 for file in (ROOT/'assets').iterdir():
  if file.is_file():shutil.copy2(file,app/'assets'/file.name)
 resources=[('docs/START_HERE_ZH.md','Chinese getting-started guide'),('docs/GLOSSARY.md','English–Chinese glossary'),('assessments/RUBRIC.md','Evidence rubric'),('builds/three-strut-prism.md','Prism build guide'),('templates/experiment.md','Experiment record'),('templates/inspection.csv','Inspection log'),('templates/bill-of-materials.csv','Bill of materials'),('templates/capstone-report.md','Capstone report'),('facilitator/WORKSHOP_90_MIN.md','90-minute workshop')]
 (app/'resources').mkdir(exist_ok=True)
 for source,title in resources:
  name=Path(source).name
  content=(ROOT/source).read_text()
  def rewrite_link(match):
   label,target=match.group(1),match.group(2)
   if target.startswith(('http://','https://','#')):return match.group(0)
   resolved=((ROOT/source).parent/target.split('#')[0]).resolve().relative_to(ROOT)
   url='../'+resolved.as_posix() if resolved.parts[0]=='assets' else 'https://github.com/freedomyamato/tensegrity-from-scratch/blob/main/'+resolved.as_posix()
   return '['+label+']('+url+')'
  content=re.sub(r'\[([^\]]*)\]\(([^)]+)\)',rewrite_link,content)
  (app/'resources'/name).write_text(content);data['resources'].append({'file':name,'title':title})
 (app/'data.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n')
 manifest={'id':'./','name':'Tensegrity Learn','short_name':'Tensegrity','description':'48 practical tensegrity lessons, quizzes and mobile labs.','lang':'en','start_url':'./','scope':'./','display':'standalone','background_color':'#f3f6fa','theme_color':'#0d2035','icons':[{'src':'./icons/icon-192.png','sizes':'192x192','type':'image/png','purpose':'any'},{'src':'./icons/icon-512.png','sizes':'512x512','type':'image/png','purpose':'any maskable'}]}
 (app/'manifest.webmanifest').write_text(json.dumps(manifest,indent=2)+'\n')
 # Icons are geometric marks generated once; no icon-generation package needed.
 import struct,zlib
 def icon(size):
  pixels=bytearray(bytes([13,32,53,255])*(size*size));points=[(.25,.72),(.5,.25),(.75,.72)]
  def line(a,b,width,color):
   ax,ay=[v*size for v in a];bx,by=[v*size for v in b];dx,dy=bx-ax,by-ay;dd=dx*dx+dy*dy
   for y in range(max(0,int(min(ay,by)-width)),min(size,int(max(ay,by)+width)+1)):
    for x in range(max(0,int(min(ax,bx)-width)),min(size,int(max(ax,bx)+width)+1)):
     t=max(0,min(1,((x-ax)*dx+(y-ay)*dy)/dd));distance=((x-ax-t*dx)**2+(y-ay-t*dy)**2)**.5
     if distance<=width/2:pixels[(y*size+x)*4:(y*size+x)*4+4]=bytes(color)
  for n in range(3):line(points[n],points[(n+1)%3],size*.035,(77,225,207,255))
  line((.25,.72),(.65,.43),size*.023,(243,146,86,255));line((.75,.72),(.36,.43),size*.023,(77,225,207,255))
  def chunk(kind,value):return struct.pack('>I',len(value))+kind+value+struct.pack('>I',zlib.crc32(kind+value)&0xffffffff)
  scan=b''.join(b'\0'+pixels[y*size*4:(y+1)*size*4] for y in range(size))
  return b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',size,size,8,6,0,0,0))+chunk(b'IDAT',zlib.compress(scan,9))+chunk(b'IEND',b'')
 (app/'icons').mkdir(exist_ok=True)
 for size in [192,512]:(app/'icons'/f'icon-{size}.png').write_bytes(icon(size))
 assets=['./','./index.html']+['./'+f.relative_to(app).as_posix() for f in sorted(app.rglob('*')) if f.is_file() and f.name not in ['index.html','sw.js','precache.js','README.md']]
 digest=hashlib.sha256(b''.join(f.read_bytes() for f in sorted(app.rglob('*')) if f.is_file() and f.name not in ['precache.js','README.md'])).hexdigest()[:16]
 (app/'precache.js').write_text('self.APP_CACHE_VERSION='+json.dumps(digest)+';\nself.APP_ASSETS='+json.dumps(assets)+';\n')
 if a.site_dist:
  destination=Path(a.site_dist).resolve();destination.mkdir(parents=True,exist_ok=True)
  if destination==app:raise ValueError('Choose a separate Site dist')
  for f in app.rglob('*'):
   if f.is_file() and f.name!='README.md':
    target=destination/f.relative_to(app);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,target)
 print(f'Built 48 mobile lessons, 48 quizzes, seven labs and {len(assets)} offline asset URLs; cache {digest}')

if __name__=='__main__':main()
