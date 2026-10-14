#!/usr/bin/env python3
"""Check this repo against OpenAI's documented plugin rules before a submission (the Codex CLI installs packages
that break them, so an install is not proof). Standard library only. Usage: python3 scripts/check_plugin.py [repo_root]

Rules come from developers.openai.com: plugins/deploy/submission (listing limits, icons, skills-only scope),
codex/plugins/build (layout, marketplace entries) and the openai/plugins repo's own manifests (field shapes, categories).
"""
import json, re, struct, sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1])
CATEGORIES = {'Business & Operations', 'Communication', 'Creativity', 'Data & Analytics', 'Developer Tools',
              'Education & Research', 'Finance', 'Productivity', 'Scientific Research', 'Security'}
INSTALL = {'NOT_AVAILABLE', 'AVAILABLE', 'INSTALLED_BY_DEFAULT'}
AUTH = {'ON_INSTALL', 'ON_USE'}
errors = []
def err(m): errors.append(m)

def png_size(p):
    b = p.read_bytes()[:24]
    return struct.unpack('>II', b[16:24]) if b[:8] == b'\x89PNG\r\n\x1a\n' else None

def check_icon(base, rel, label):
    if not isinstance(rel, str) or not rel.startswith('./assets/'): return err(f'{label}: must be a ./assets/ path')
    p = base / rel
    if not p.is_file(): return err(f'{label}: missing file {rel}')
    if p.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.webp', '.svg'}: err(f'{label}: unsupported format {p.suffix}')
    if p.stat().st_size > 5 * 1024 * 1024: err(f'{label}: over 5 MiB')
    if p.suffix.lower() == '.png':
        wh = png_size(p)
        if not wh or wh[0] != wh[1] or wh[0] < 48 or wh[0] > 4096: err(f'{label}: must be square, 48 to 4096 px (got {wh})')
    if p.suffix.lower() == '.svg':
        vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', p.read_text(errors='ignore'))
        if not vb or vb[1] != vb[2]: err(f'{label}: SVG must be square')

mk_path = ROOT / '.agents/plugins/marketplace.json'
try: mk = json.loads(mk_path.read_text())
except Exception as e: mk = {}; err(f'marketplace: unreadable {e}')
if not mk.get('name') or not (mk.get('interface') or {}).get('displayName'): err('marketplace: needs name and interface.displayName')
for i, entry in enumerate(mk.get('plugins') or [{}]):
    tag = f"marketplace entry {entry.get('name', i)}"
    src = entry.get('source') or {}
    if src.get('source') != 'local' or not str(src.get('path', '')).startswith('./'): err(f'{tag}: source must be local with a ./ path')
    pol = entry.get('policy') or {}
    if pol.get('installation') not in INSTALL: err(f'{tag}: policy.installation missing or invalid')
    if pol.get('authentication') not in AUTH: err(f'{tag}: policy.authentication missing or invalid')
    if entry.get('category') not in CATEGORIES: err(f'{tag}: category not allowed')
    base = ROOT / str(src.get('path', ''))
    if base.name != entry.get('name'): err(f'{tag}: folder name must equal plugin name')
    try: pj = json.loads((base / '.codex-plugin/plugin.json').read_text())
    except Exception as e: err(f'{tag}: .codex-plugin/plugin.json unreadable {e}'); continue
    if pj.get('name') != entry.get('name') or not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', pj.get('name', '')): err(f'{tag}: manifest name must be kebab-case and match')
    if not re.fullmatch(r'\d+\.\d+\.\d+', str(pj.get('version', ''))): err(f'{tag}: version must be semantic')
    if not pj.get('description') or len(pj['description']) > 4000: err(f'{tag}: description missing or over 4000')
    if not (pj.get('author') or {}).get('name'): err(f'{tag}: author.name required')
    ui = pj.get('interface') or {}
    for k, n in (('displayName', 30), ('shortDescription', 30), ('longDescription', 4000), ('developerName', 80)):
        if not ui.get(k) or len(ui[k]) > n: err(f'{tag}: interface.{k} missing or over {n}')
    if ui.get('category') not in CATEGORIES: err(f'{tag}: interface.category not allowed')
    if not ui.get('capabilities'): err(f'{tag}: interface.capabilities required')
    for k in ('websiteURL', 'privacyPolicyURL', 'termsOfServiceURL'):
        if not str(ui.get(k, '')).startswith('https://'): err(f'{tag}: interface.{k} must be https')
    dp = ui.get('defaultPrompt') or []
    if len(dp) > 3 or any(len(x) > 128 for x in dp): err(f'{tag}: up to three default prompts of 128 characters')
    check_icon(base, ui.get('logo'), f'{tag}: logo'); check_icon(base, ui.get('composerIcon'), f'{tag}: composerIcon')
    if pj.get('hooks') or (base / 'hooks').exists() or ((pj.get('extensions') or {}).get('com.openai') or {}).get('hooks'): err(f'{tag}: lifecycle hooks are not allowed in the public directory')
    if pj.get('apps') or (base / '.app.json').exists(): err(f'{tag}: app references cannot be submitted')
    if (base / 'mcp.json').exists() or (base / '.mcp.json').exists(): err(f'{tag}: a skills-only package must not carry MCP configuration')
    skills = sorted((base / 'skills').glob('*/SKILL.md'))
    if not skills: err(f'{tag}: no skills')
    for s in skills:
        m = re.match(r'\A---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---\n', s.read_text())
        if not m or m[1].strip() != s.parent.name: err(f'skill {s.parent.name}: frontmatter name must equal folder name')
        elif len(m[2]) > 1024: err(f'skill {s.parent.name}: description over 1024 characters')
    cj = base / '.claude-plugin/plugin.json'
    if cj.exists() and json.loads(cj.read_text()).get('name') != pj.get('name'): err(f'{tag}: Claude manifest name differs')
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix in {'.md', '.json', '.txt'} and re.search(r'(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|BEGIN [A-Z ]*PRIVATE KEY)', p.read_text(errors='ignore')):
        err(f'possible secret in {p.relative_to(ROOT)}')
print(json.dumps({'ok': not errors, 'errors': errors}, indent=1))
sys.exit(1 if errors else 0)
