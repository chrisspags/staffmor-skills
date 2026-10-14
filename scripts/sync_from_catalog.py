#!/usr/bin/env python3
"""Rebuild plugins/staffmor/skills from Staffmor's local skill catalog, so the public plugin carries exactly the skills
customers can select (catalog entries with dispatchEligible true), word for word. Chris, 10/14/2026: "make sure it matches
our local skills database so when i tell someone to add it, it gets added".

  python3 scripts/sync_from_catalog.py [--catalog DIR]          rewrite skills/ and catalog-sync.json from the catalog
  python3 scripts/sync_from_catalog.py --check [--catalog DIR]  exit 1 if the plugin differs from the catalog

Each SKILL.md is YAML frontmatter (name, description) followed by the catalog guide's exact bytes; catalog-sync.json pins
the catalog version and every guide's SHA-256. Held (quarantined) entries are never copied. Standard library only.
"""
import argparse, hashlib, json, re, shutil, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PLUGIN = REPO / 'plugins/staffmor'
DEFAULT_CATALOG = Path.home() / 'Documents/Mara/splash-play-staffmor-office/app/src/catalog/runtime'

def slugify(name):
    s = re.sub(r'[^a-z0-9]+', '-', name.lower().replace('&', ' and ')).strip('-')
    return s[:64].strip('-')

def yaml_quote(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

def plan(catalog):
    cat = json.loads((catalog / 'catalog.json').read_text())
    rows, used = [], {}
    for e in sorted((x for x in cat['entries'] if x.get('dispatchEligible')), key=lambda x: x['name'].lower()):
        guide = catalog / e['guideRef']['path'].replace('runtime/', '', 1)
        body = guide.read_bytes()
        if hashlib.sha256(body).hexdigest() != e['guideRef']['sha256']:
            sys.exit(f"refused: {e['publicId']} guide bytes do not match the catalog's pinned SHA-256")
        slug = slugify(e['name'])
        if slug in used: slug = f"{slug}-{e['publicId'][-6:]}"
        used[slug] = e['publicId']
        jobs = [j.strip().rstrip('.') for j in (e.get('exampleJobs') or []) if j.strip()]
        desc = e['purpose'].strip().rstrip('.') + '.' + (f" Use it to {jobs[0][0].lower() + jobs[0][1:]}." if jobs else '')
        desc = re.sub(r'\s+', ' ', desc)[:1000]
        rows.append({'publicId': e['publicId'], 'key': e['key'], 'name': e['name'], 'slug': slug, 'origin': e.get('origin'),
                     'guideSha256': e['guideRef']['sha256'], 'description': desc, 'body': body})
    return cat, rows

def render(r):
    return f"---\nname: {r['slug']}\ndescription: {yaml_quote(r['description'])}\n---\n\n".encode() + r['body']

def main():
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument('--catalog', type=Path, default=DEFAULT_CATALOG); ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    cat, rows = plan(a.catalog)
    skills = PLUGIN / 'skills'
    want = {r['slug']: render(r) for r in rows}
    if a.check:
        have = {p.parent.name: p.read_bytes() for p in skills.glob('*/SKILL.md')}
        extra, missing = sorted(set(have) - set(want)), sorted(set(want) - set(have))
        changed = sorted(s for s in set(want) & set(have) if want[s] != have[s])
        rec = json.loads((PLUGIN / 'catalog-sync.json').read_text()) if (PLUGIN / 'catalog-sync.json').exists() else {}
        ok = not (extra or missing or changed) and rec.get('catalogVersion') == cat['version'] and rec.get('count') == len(rows)
        print(json.dumps({'ok': ok, 'catalogVersion': cat['version'], 'catalogSelectable': len(rows), 'pluginSkills': len(have),
                          'missing': missing, 'extra': extra, 'changed': changed, 'recordVersion': rec.get('catalogVersion')}, indent=1))
        sys.exit(0 if ok else 1)
    if skills.exists(): shutil.rmtree(skills)
    for slug, data in want.items():
        (skills / slug).mkdir(parents=True); (skills / slug / 'SKILL.md').write_bytes(data)
    (PLUGIN / 'catalog-sync.json').write_text(json.dumps({'catalogVersion': cat['version'], 'count': len(rows),
        'rule': 'catalog entries with dispatchEligible true; held entries are never copied',
        'entries': [{k: r[k] for k in ('publicId', 'key', 'name', 'slug', 'origin', 'guideSha256')} for r in rows]}, indent=1) + '\n')
    lic = a.catalog / 'LICENSE-agency.txt'
    if lic.exists(): shutil.copyfile(lic, REPO / 'LICENSES/agency-agents-MIT.md')
    print(f"synced {len(rows)} skills from catalog {cat['version']}")

if __name__ == '__main__':
    main()
