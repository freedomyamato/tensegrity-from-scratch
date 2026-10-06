"""Package tracked source without caches, outputs or private learner records."""
from pathlib import Path
import argparse
import zipfile
ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',default=str(ROOT.parent/'Tensegrity_From_Scratch_Teaching_Repository_v1.zip'));a=p.parse_args()
    dest=Path(a.output).resolve();dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.is_relative_to(ROOT):p.error('output archive must be outside the source tree')
    excluded={'.git','__pycache__','.venv','outputs','learner-data'};included=[]
    with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for file in sorted(ROOT.rglob('*')):
            rel=file.relative_to(ROOT)
            if not file.is_file() or any(x in excluded for x in rel.parts) or file.suffix in {'.pyc','.tmp'}:continue
            if file.is_symlink():raise ValueError('symlinks are not included in release archives')
            name=(Path(ROOT.name)/rel).as_posix();info=zipfile.ZipInfo(name,date_time=(2026,10,6,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
            z.writestr(info,file.read_bytes());included.append(name)
    with zipfile.ZipFile(dest) as z:
        if z.testzip() is not None:raise ValueError('archive integrity failed')
    print(f'{dest}\n{len(included)} files; {dest.stat().st_size} bytes; private data and generated lab output excluded')

if __name__=='__main__':main()
