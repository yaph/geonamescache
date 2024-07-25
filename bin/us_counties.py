#!/usr/bin/env python
import csv
import json
from pathlib import Path

p_data = Path('data')

reader = csv.reader(p_data.joinpath('us_counties.txt').open())

counties = [{'fips': line[1] + line[2], 'name': line[3], 'state': line[0]} for line in reader]

p_data.joinpath('us_counties.json').write_text(json.dumps(counties))
