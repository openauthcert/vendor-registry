import json
import os

VENDORS_DIR = 'vendors'
OUTPUT_FILE = os.path.join('public', 'summary.json')

summary = []
for filename in os.listdir(VENDORS_DIR):
    if not filename.endswith('.json'):
        continue
    slug = filename[:-5]
    path = os.path.join(VENDORS_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    summary.append({
        'name': data.get('name'),
        'slug': slug,
        'oidc_support': data.get('oidc_support', False),
        'saml_support': data.get('saml_support', False),
    })

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2)
