#!/usr/bin/env python
import csv
import json
from pathlib import Path

p_data = Path('datasets')

admin2 = {}

reader = csv.reader(p_data.joinpath('admin2Codes.txt').open(encoding='utf-8'), 'excel-tab')
for record in reader:
    code, name, asciiname, geonameid = record

    # required because used as key
    if not code:
        continue

    admin2[code] = {
        'asciiname': asciiname,
        'geonameid': int(geonameid) if geonameid else 0,
        'name': name,
    }

p_data.joinpath('admin2.json').write_text(json.dumps(admin2, ensure_ascii=False))
