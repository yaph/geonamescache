#!/usr/bin/env python
# coding: utf-8
import json
import csv

from pathlib import Path


counties = []
p_data = Path('data')

reader = csv.reader(p_data.joinpath('us_counties.txt').open())
for line in reader:
    counties.append({
        'fips': line[1] + line[2],
        'name': line[3],
        'state': line[0]
    })

p_data.joinpath('us_counties.json').write_text(json.dumps(counties))