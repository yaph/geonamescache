#!/usr/bin/env python
# coding: utf-8
import json
import re

re_county = re.compile(r'(\d{5})\s+([^,]+),\s+(\w{2})')
counties = []

with open('../data/us_counties.txt', 'r') as f:
    lines = f.read().splitlines()

for line in lines:
    m = re.match(re_county, line)
    if m:
        counties.append({
            'fips': m.group(1),
            'name': m.group(2),
            'state': m.group(3)
        })

with open('../geonamescache/us_counties.json', 'w') as f:
    json.dump(counties, f, ensure_ascii=False)
