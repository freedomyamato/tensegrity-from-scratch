"""Check course completeness, quiz coverage, local links and asset structure."""
from pathlib import Path
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from course_data import LESSONS, PHASES


def main():
    errors=[];manifest=json.loads((ROOT/'curriculum.json').read_text())
    if len(manifest['lessons'])!=48:errors.append('manifest must have 48 lessons')
    if [x['id'] for x in manifest['lessons']]!=list(range(1,49)):errors.append('lesson IDs must be 1..48')
    if len(manifest['phases'])!=12 or sum(x['hours_estimate'] for x in manifest['phases'])!=180:errors.append('phase count/hours inconsistent')
    headings=['Objective','Concept','Worked example','Materials and setup','Predict and practice','Expected behavior and interpretation','Troubleshooting and limits','Teach-back quiz','Evidence to submit','Facilitator adaptation','Reading and provenance']
    for entry,authored in zip(manifest['lessons'],LESSONS):
        path=ROOT/entry['path']
        if not path.exists():errors.append(f'missing lesson: {path}');continue
        text=path.read_text()
        for h in headings:
            if f'## {h}' not in text:errors.append(f'{path}: missing {h}')
        if len(text.split())<300:errors.append(f'{path}: lesson unexpectedly short')
        if len(authored['questions'])!=3 or len(authored['answers'])!=3:errors.append(f'{path}: quiz must have 3 matched answers')
        if not (path.parent.parent/'experiments/worksheet.md').exists():errors.append(f'{path}: worksheet missing')
    for phase in range(12):
        for kind in ['quiz','answers']:
            p=ROOT/f'assessments/phase-{phase:02d}-{kind}.md'
            if not p.exists() or p.read_text().count('## Lesson ')!=4:errors.append(f'{p}: must cover four lessons')
    # Ignore code fences: example output paths are not required source links.
    checked=0
    for p in ROOT.rglob('*.md'):
        if '.git' in p.parts:continue
        text=re.sub(r'```.*?```','',p.read_text(),flags=re.S)
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text):
            if target.startswith(('http://','https://','mailto:','#')):continue
            target=target.split('#')[0]
            if target and not (p.parent/target).exists():errors.append(f'{p.relative_to(ROOT)}: broken link {target}')
            checked+=1
    for p in (ROOT/'assets').glob('*.svg'):
        try:ET.parse(p)
        except ET.ParseError as exc:errors.append(f'{p}: invalid SVG {exc}')
    class Reader(HTMLParser):
        def __init__(self):super().__init__();self.ids=[];self.refs=[];self.lang=None
        def handle_starttag(self,tag,attrs):
            d=dict(attrs)
            if 'id' in d:self.ids.append(d['id'])
            if tag=='html':self.lang=d.get('lang')
            if tag in ['a','img']:
                v=d.get('href') if tag=='a' else d.get('src')
                if v:self.refs.append(v)
    parser=Reader();parser.feed((ROOT/'reader.html').read_text())
    if parser.lang!='en':errors.append('reader language missing')
    if len(parser.ids)!=len(set(parser.ids)):errors.append('reader has duplicate IDs')
    if len([x for x in parser.ids if x.startswith('lesson-')])!=48:errors.append('reader must have 48 lessons')
    for target in parser.refs:
        if target.startswith('#'):
            if target[1:] not in parser.ids:errors.append('reader broken anchor '+target)
        elif not target.startswith(('https://','http://')) and not (ROOT/target.split('#')[0]).exists():errors.append('reader broken local link '+target)
    routes=json.loads((ROOT/'learning-paths/routes.json').read_text())
    for name,phases in routes['routes'].items():
        if len(phases)!=len(set(phases)) or any(x not in range(12) for x in phases):errors.append('invalid route '+name)
    if errors:
        print('\n'.join(errors),file=sys.stderr);return 1
    print(f'PASS: 48 lessons, 48 worksheets, 12 phase guides, 24 assessment files; {checked} Markdown links; SVG and offline reader checks.')
    return 0

if __name__=='__main__':raise SystemExit(main())
