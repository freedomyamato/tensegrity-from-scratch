"""Rebuild authored lessons, course manifest, assessments, diagrams and reader.

Uses only the Python standard library. Run from any working directory.
"""
from pathlib import Path
import sys
import json
import re
import html
import math
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from course_data import PHASES, LESSONS
from tensegrity.models import prism, lengths

def write(path,text):
    p=ROOT/path; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text,encoding='utf-8')

def slug(text): return re.sub(r'[^a-z0-9]+','-',text.lower()).strip('-')

def inline(text):
    # Limited authored Markdown, escaping all content before adding markup.
    s=html.escape(text)
    s=re.sub(r'!\[([^\]]*)\]\(([^\s)]+)\)',r'<img src="\2" alt="\1" loading="lazy" style="max-width:100%">',s)
    s=re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)',r'<a href="\2">\1</a>',s)
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    return s

def render(markdown):
    out=[]; paragraph=[]; code=[]; in_code=False; table=[]; listing=None
    def flush():
        nonlocal listing
        if paragraph: out.append('<p>'+inline(' '.join(paragraph))+'</p>'); paragraph.clear()
        if table:
            rows=[]
            for idx,line in enumerate(table):
                cells=[x.strip() for x in line.strip('|').split('|')]
                if all(re.fullmatch(r':?-+:?',x) for x in cells): continue
                tag='th' if idx==0 else 'td'
                rows.append('<tr>'+''.join(f'<{tag}>{inline(x)}</{tag}>' for x in cells)+'</tr>')
            out.append('<div class="table-wrap"><table>'+''.join(rows)+'</table></div>');table.clear()
        if listing: out.append('</'+listing+'>');listing=None
    for line in markdown.splitlines():
        if line.startswith('```'):
            if in_code: out.append('<pre><code>'+html.escape('\n'.join(code))+'</code></pre>');code=[];in_code=False
            else: flush();in_code=True
            continue
        if in_code: code.append(line);continue
        if not line.strip(): flush();continue
        m=re.match(r'^(#{1,6}) (.+)',line)
        if m:
            flush();level=len(m[1]);out.append(f'<h{level}>{inline(m[2])}</h{level}>');continue
        if line.startswith('|'):
            if paragraph or listing: flush()
            table.append(line);continue
        m=re.match(r'^(?:([-*]) |\d+\. )(.+)',line)
        if m:
            if paragraph or table: flush()
            tag='ul' if m[1] else 'ol'
            if listing!=tag: flush();listing=tag;out.append('<'+tag+'>')
            out.append('<li>'+inline(m[2])+'</li>');continue
        if listing or table: flush()
        if line.startswith('> '): out.append('<blockquote>'+inline(line[2:])+'</blockquote>')
        else: paragraph.append(line)
    flush()
    return ''.join(out)

def diagram_assets():
    nodes,members=prism(); lens=lengths(nodes,members)
    projection=[(280+1200*(x-.45*y),330-1200*(z+.28*y)) for x,y,z in nodes]
    s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 460" role="img" aria-labelledby="title desc">',
       '<title id="title">Three-strut prism: nine cables and three separated struts</title><desc id="desc">Bottom nodes 0,1,2; top nodes 3,4,5. Struts connect 0–4,1–5,2–3. Projection is not to scale.</desc>',
       '<rect width="560" height="460" fill="#f8fafc"/><text x="24" y="32" font-family="sans-serif" font-size="20">Three-strut prism · 30° twist</text>']
    for m in members:
        a,b=projection[m.a],projection[m.b]; color='#b91c1c' if m.kind=='strut' else '#1d4ed8';width=8 if m.kind=='strut' else 2.5
        dash=' stroke-dasharray="6 4"' if m.name.startswith('C') else ''
        s.append(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{color}" stroke-width="{width}"{dash}/>')
        s.append(f'<text x="{(a[0]+b[0])/2+5:.2f}" y="{(a[1]+b[1])/2-5:.2f}" font-family="sans-serif" font-size="12" fill="{color}">{m.name}</text>')
    for i,(x,y) in enumerate(projection):
        s.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="7" fill="white" stroke="#0f172a"/><text x="{x+12:.2f}" y="{y+5:.2f}" font-family="sans-serif" font-size="18" fill="#0f172a">{i}</text>')
    s.append('<text x="24" y="410" font-family="sans-serif" font-size="14">Blue cables · dashed cross cables · thick red struts</text><text x="24" y="436" font-family="sans-serif" font-size="13">R=80 mm · h=140 mm · projected view, not a cutting plan</text></svg>')
    write('assets/prism.svg','\n'.join(s))
    rows=['member,node_a,node_b,kind,node_span_mm']+[f'{m.name},{m.a},{m.b},{m.kind},{l*1000:.6f}' for m,l in zip(members,lens)]
    write('assets/member-schedule.csv','\n'.join(rows)+'\n')
    rows=['node,x_mm,y_mm,z_mm']+[f'{i},{x*1000:.6f},{y*1000:.6f},{z*1000:.6f}' for i,(x,y,z) in enumerate(nodes)]
    write('assets/node-coordinates.csv','\n'.join(rows)+'\n')
    # Two A4 plan views with a physical print-scale check, exact nominal mm.
    for name,offset in [('bottom',0),('top',3)]:
        s=['<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">',
           f'<title>Nominal {name} node-position jig</title><rect width="210" height="297" fill="white"/>',
           f'<text x="12" y="18" font-size="5" font-family="sans-serif">{name.title()} triangle · print at 100% / actual size</text>',
           '<circle cx="105" cy="125" r="80" fill="none" stroke="#94a3b8" stroke-width=".3"/>',
           '<path d="M 100 125 H 110 M 105 120 V 130" stroke="black" stroke-width=".3"/>']
        for i in range(offset,offset+3):
            x,y,z=nodes[i];px=105+x*1000;py=125-y*1000
            s.append(f'<circle cx="{px}" cy="{py}" r="2" fill="none" stroke="black" stroke-width=".5"/><text x="{px+3}" y="{py-3}" font-size="6">{i}</text>')
        s.append('<path d="M 30 245 H 80 M 30 242 V 248 M 80 242 V 248" fill="none" stroke="black" stroke-width=".4"/><text x="30" y="255" font-family="sans-serif" font-size="4">This line must measure 50 mm.</text><text x="12" y="275" font-family="sans-serif" font-size="4">Node positions only. No load capacity or joint design implied.</text></svg>')
        write(f'assets/jig-{name}.svg','\n'.join(s))
    plots=[('force-balance','Force balance at a node','Cable pulls toward far endpoint','Compressed strut pushes away','Include external load when present'),
           ('solar-measurement','Solar measurement chain','Support orientation and shading','Simultaneous loaded V and I','Power integrated over time'),
           ('learning-loop','Evidence-based learning','Predict and explain','Build or simulate; measure','Compare, record and teach back')]
    for filename,title,*labels in plots:
        s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 340"><title>{title}</title><rect width="650" height="340" fill="#f8fafc"/><text x="24" y="32" font-size="20" font-family="sans-serif">{title}</text>']
        for j,label in enumerate(labels):
            y=55+85*j
            s.append(f'<rect x="24" y="{y}" width="600" height="60" rx="9" fill="white" stroke="#2563eb"/><text x="40" y="{y+36}" font-size="17" font-family="sans-serif">{html.escape(label)}</text>')
            if j<2:s.append(f'<path d="M 320 {y+63} v 17 m -5 -5 l 5 5 l 5 -5" stroke="#334155" fill="none"/>')
        write(f'assets/{filename}.svg',''.join(s)+'</svg>')


def main():
    if len(LESSONS)!=48: raise ValueError('The course must contain 48 authored lessons')
    diagram_assets(); manifest={'version':'1.0.0','hours_estimate':180,'phases':[],'lessons':[]}
    nav=[]; sections=[]; index=['# Course contents','', '48 lessons · 12 phases · approximately 180 hours including practice. Estimates are not validated study-time measurements.','']
    for phase,(key,title,hours) in enumerate(PHASES):
        phase_path=f'phases/{phase:02d}-{key}'; entries=[]; assessment=[]; keys=[]
        index += [f'## Phase {phase:02d}: {title}', '', f'Planning allowance: {hours} hours.', '']
        for local in range(4):
            number=phase*4+local+1; item=LESSONS[number-1]; lesson_key=f'{number:02d}-{slug(item["title"])}'; path=f'{phase_path}/{lesson_key}'
            relroot='../../../..'; previous=number-1 if number>1 else None
            prereq=f'Lesson {previous:02d}; or demonstrate its evidence check' if previous else 'None. Bring a learning goal and a way to record observations.'
            diagram='prism.svg' if 1<=phase<=5 else 'solar-measurement.svg' if phase==7 else 'learning-loop.svg'
            minutes=round(hours*60/4)
            content=f'# Lesson {number:02d}: {item["title"]}\n\n[Course contents]({relroot}/COURSE.md) · Phase {phase:02d}: {title}\n\n'
            content+=f'## Objective\n\n{item["objective"]}\n\n**Prerequisite:** {prereq}.\n\n**Planning time:** approximately {minutes} minutes including practice and recording. Split into short sessions as needed.\n\n'
            content+=f'## Concept\n\n{item["concept"]}\n\n![Supporting diagram for this phase]({relroot}/assets/{diagram})\n\n## Worked example\n\n{item["worked"]}\n\n'
            content+=f'## Materials and setup\n\n{item["materials"]}\n\nUse a private copy of the [experiment record]({relroot}/templates/experiment.md). Assign a specimen or activity ID and record which values are measured, calculated or illustrative.\n\n'
            content+='## Predict and practice\n\nBefore acting, write the result you expect and one observation that could disagree with it.\n\n'
            content+='\n'.join(f'{i+1}. {step}' for i,step in enumerate(item['steps']))+'\n\n'
            if item['lab']:
                command={'solar':'python3 -m tensegrity solar examples/solar_readings.csv'}.get(item['lab'],f'python3 -m tensegrity {item["lab"]}')
                content+=f'## Runnable lab\n\nFrom the repository root (the folder containing README.md):\n\n```bash\n{command}\n```\n\nSee the [lab guide]({relroot}/labs/README.md) for expected output and parameter changes. Compare one output with a calculation before interpreting the result. If you cannot run Python, use the worked example and label the task as a manual exercise.\n\n'
            content+=f'## Expected behavior and interpretation\n\n{item["expected"]}\n\nIf your result differs, keep it. Recheck units, endpoint definitions, instruments and assumptions before changing the design. A mismatch can be the most useful evidence.\n\n## Troubleshooting and limits\n\n{item["pitfall"]}\n\n'
            content+='## Teach-back quiz\n\n'+'\n'.join(f'{i+1}. {q}' for i,q in enumerate(item['questions']))+'\n\n'
            content+=f'[Facilitator answer key]({relroot}/assessments/phase-{phase:02d}-answers.md) — attempt the questions first.\n\n'
            content+=f'## Evidence to submit\n\n{item["artifact"]}\n\nInclude your prediction, setup, results with units or criteria, and one limitation. Use the [rubric]({relroot}/assessments/RUBRIC.md): demonstrate each applicable dimension at level 2 or above before progressing. Numerical examples count as calculation evidence; they are not physical test results.\n\n'
            content+=f'## Facilitator adaptation\n\nOffer a sketch, demonstration or pointing response as alternatives to speech. Provide pre-labeled parts, shorter sessions or a quiet workspace if chosen by the learner. Preserve the objective while adapting unnecessary task demands.\n\n## Reading and provenance\n\nSee [source notes]({relroot}/references/README.md). This lesson is original course material. Hypothetical numbers are teaching examples; no field deployment or institutional endorsement is implied.\n'
            write(path+'/docs/en.md',content)
            worksheet=f'# Lesson {number:02d} worksheet\n\nTopic: {item["title"]}\n\n## Before\n\nRecord date, specimen/activity ID, prediction and setup.\n\n## During\n\n'+'\n'.join(f'- [ ] {step}' for step in item['steps'])+f'\n\n## After\n\nRequired evidence: {item["artifact"]}\n\nRecord raw observations, units, disagreements, support used and one next step. Do not invent missing data.\n'
            write(path+'/experiments/worksheet.md',worksheet)
            entry={'id':number,'phase':phase,'title':item['title'],'path':path+'/docs/en.md','lab':item['lab'],'minutes_estimate':minutes}
            entries.append(entry);manifest['lessons'].append(entry)
            index.append(f'- [{number:02d} · {item["title"]}]({entry["path"]})')
            nav.append(f'<a href="#lesson-{number:02d}">{number:02d} {html.escape(item["title"])}</a>')
            # Reader links retain root-relative paths so offline assets open normally.
            readercontent=content.replace(relroot+'/','')
            sections.append(f'<details class="lesson" id="lesson-{number:02d}"><summary><span>{number:02d}</span> {html.escape(item["title"])}</summary><article>{render(readercontent)}</article></details>')
            assessment += [f'## Lesson {number:02d}: {item["title"]}','']+[f'{i+1}. {q}' for i,q in enumerate(item['questions'])]+['']
            keys += [f'## Lesson {number:02d}: {item["title"]}','']+[f'{i+1}. {ans}' for i,ans in enumerate(item['answers'])]+['',f'Evidence check: {item["artifact"]}','']
        manifest['phases'].append({'id':phase,'title':title,'hours_estimate':hours,'path':phase_path,'lesson_ids':[e['id'] for e in entries]})
        write(phase_path+'/README.md',f'# Phase {phase:02d}: {title}\n\n[Course contents](../../COURSE.md)\n\nPlanning allowance: {hours} hours.\n\n'+'\n'.join(f'- [{e["id"]:02d} · {e["title"]}]({Path(e["path"]).relative_to(phase_path).as_posix()})' for e in entries)+f'\n\n[Phase quiz](../../assessments/phase-{phase:02d}-quiz.md) · [Answer key](../../assessments/phase-{phase:02d}-answers.md)\n\nComplete each lesson’s evidence check before moving on. Quiz answers alone do not replace practical evidence.\n')
        write(f'assessments/phase-{phase:02d}-quiz.md',f'# Phase {phase:02d} quiz\n\nTry these before opening the separate answer key.\n\n'+'\n'.join(assessment))
        write(f'assessments/phase-{phase:02d}-answers.md',f'# Phase {phase:02d} facilitator answers\n\nAccept equivalent explanations supported by correct reasoning. Review practical evidence separately.\n\n'+'\n'.join(keys))
    write('COURSE.md','\n'.join(index)+'\n')
    write('curriculum.json',json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
    shell='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Tensegrity from Scratch — Course reader</title><style>
:root{color-scheme:light;--ink:#14263b;--blue:#1857b6}*{box-sizing:border-box}body{margin:0;color:var(--ink);background:#f4f7fb;font:17px/1.65 system-ui,sans-serif}header{padding:34px 6%;background:#14263b;color:white}header h1{margin:0;font-size:clamp(28px,5vw,45px)}header p{max-width:850px}header a{color:#c2dcff}.layout{display:grid;grid-template-columns:290px minmax(0,900px);gap:28px;margin:24px auto;max-width:1240px;padding:0 18px}aside{position:sticky;top:16px;height:calc(100vh - 35px);overflow:auto;background:white;padding:16px;border-radius:12px}aside a{display:block;color:var(--ink);font-size:14px;margin:9px 0;text-decoration:none}input{width:100%;padding:10px;border:1px solid #8aa0bb;border-radius:6px;font:inherit}main{min-width:0}.lesson{background:white;margin:0 0 15px;border:1px solid #dce5ef;border-radius:12px;scroll-margin-top:18px}summary{cursor:pointer;padding:18px;font-weight:650}summary span{color:var(--blue);margin-right:10px}article{padding:0 24px 28px}article h1{font-size:26px}article h2{font-size:21px;margin-top:28px}a{color:var(--blue)}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#eff3f8;padding:15px;border-radius:7px;font-size:14px}code{font-size:.9em}.table-wrap{overflow:auto}table{border-collapse:collapse}td,th{border:1px solid #ccd8e6;padding:7px}blockquote{border-left:4px solid #8cb0de;padding-left:16px;margin-left:0}#count{font-size:14px}button{padding:9px 12px;background:#1857b6;color:white;border:0;border-radius:7px;font:inherit;cursor:pointer}.hidden{display:none!important}@media(max-width:800px){.layout{display:block}aside{position:static;height:auto;margin-bottom:20px}aside nav{max-height:180px;overflow:auto}article{padding:0 16px 20px}}@media print{header{background:white;color:black}aside,.actions{display:none}.layout{display:block;margin:0}.lesson{break-inside:avoid}details:not([open]) article{display:block}}
</style></head><body><header><h1>Tensegrity from Scratch</h1><p>A practical course for solar sculptures, community learning and evidence-based structural exploration. 48 authored lessons; English lessons with a Chinese getting-started guide. Educational models, not deployment certification.</p><p><a href="README.md">Repository guide</a> · <a href="docs/START_HERE_ZH.md">中文入门</a> · <a href="facilitator/HANDBOOK.md">Facilitator handbook</a></p><div class="actions"><button id="open-all">Expand all lessons</button> <button id="close-all">Collapse all</button></div></header><div class="layout"><aside><label for="search">Find a topic</label><input id="search" type="search" placeholder="e.g. solar, cable, teaching"><p id="count" aria-live="polite">48 lessons</p><nav aria-label="Lessons">NAV</nav></aside><main>SECTIONS</main></div><script>
const lessons=[...document.querySelectorAll('.lesson')], links=[...document.querySelectorAll('nav a')];
document.getElementById('search').addEventListener('input',e=>{const q=e.target.value.trim().toLowerCase();let count=0;lessons.forEach((d,i)=>{const show=d.textContent.toLowerCase().includes(q);d.classList.toggle('hidden',!show);links[i].classList.toggle('hidden',!show);if(show)count++});document.getElementById('count').textContent=count+' lessons'});
function openHash(){const d=document.getElementById(location.hash.slice(1));if(d&&d.classList.contains('lesson')){d.open=true;d.classList.remove('hidden')}}
window.addEventListener('hashchange',openHash);openHash();document.getElementById('open-all').onclick=()=>lessons.forEach(d=>d.open=true);document.getElementById('close-all').onclick=()=>lessons.forEach(d=>d.open=false);
</script></body></html>'''
    write('reader.html',shell.replace('NAV',''.join(nav)).replace('SECTIONS',''.join(sections)))
    print(f'Built {len(LESSONS)} lessons, 12 phase guides, 24 assessment files and reader.html')

if __name__=='__main__':main()
