from pathlib import Path
import json, re
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / '.claude-plugin/plugin.json').read_text())
assert manifest['name'] == 'tensegrity-teaching'
assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])
repo = root.parents[1]
market = json.loads((repo / '.claude-plugin/marketplace.json').read_text())
assert (repo / market['plugins'][0]['source']).resolve() == root
skill = root / 'skills/tensegrity-teaching-assistant'
body = (skill / 'SKILL.md').read_text()
for target in re.findall(r'references/[a-z-]+\.md', body):
    assert (skill / target).is_file(), target
commands = list((root / 'commands').glob('*.md'))
assert len(commands) == 6
for command in commands:
    text = command.read_text()
    assert text.startswith('---\n') and '$ARGUMENTS' in text
lesson = (root / 'examples/beginner-lesson.md').read_text()
intervals = re.findall(r'^\| (\d+)–(\d+) \|', lesson, re.M)
assert sum(int(b)-int(a) for a,b in intervals) == 60
assert all(int(intervals[i][1]) == int(intervals[i+1][0]) for i in range(len(intervals)-1))
for f in root.rglob('*.md'):
    assert '[TODO' not in f.read_text(), f
print('PASS: manifests, 6 commands, reference paths, placeholders, contiguous 60-minute example')
