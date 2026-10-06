"""Local evidence index. Does not grade or certify learners."""
from pathlib import Path
import argparse
import json
from datetime import date
ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser(description='Record evidence locally; no automatic completion or grade.')
    sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('list')
    r=sub.add_parser('record');r.add_argument('lesson',type=int);r.add_argument('--evidence',required=True);r.add_argument('--note',default='')
    a=p.parse_args();course=json.loads((ROOT/'curriculum.json').read_text());directory=ROOT/'learner-data';file=directory/'progress.json'
    try:data=json.loads(file.read_text()) if file.exists() else {'entries':[]}
    except (OSError,json.JSONDecodeError) as exc:p.error(f'cannot read existing record: {exc}')
    if a.command=='record':
        if not 1<=a.lesson<=48:p.error('lesson must be 1..48')
        evidence=Path(a.evidence)
        if not evidence.is_absolute():evidence=ROOT/evidence
        if not evidence.is_file():p.error('evidence must be an existing file; no evidence is invented')
        data['entries'].append({'lesson':a.lesson,'date':date.today().isoformat(),'evidence':str(evidence),'note':a.note,'status':'recorded, not graded'})
        directory.mkdir(exist_ok=True);temp=directory/'progress.json.tmp';temp.write_text(json.dumps(data,indent=2)+'\n');temp.replace(file)
        print('Evidence recorded locally; a facilitator still reviews the rubric.')
    else:
        seen={x['lesson'] for x in data['entries']}
        for lesson in course['lessons']:print(f'{lesson["id"]:02d} {"evidence recorded" if lesson["id"] in seen else "pending"}: {lesson["title"]}')

if __name__=='__main__':main()
