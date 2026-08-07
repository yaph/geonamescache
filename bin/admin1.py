#!/usr/bin/env python
import csv
import json
from pathlib import Path

p_data = Path('datasets')

admin1 = {}

reader = csv.reader(p_data.joinpath('admin1CodesASCII.txt').open(encoding='utf-8'), 'excel-tab')
for record in reader:
    code, name, asciiname, geonameid = record

    # required because used as key
    if not code:
        continue

    admin1[code] = {
        'asciiname': asciiname,
        'geonameid': int(geonameid) if geonameid else 0,
        'name': name,
    }

p_data.joinpath('admin1.json').write_text(json.dumps(admin1, ensure_ascii=False))
