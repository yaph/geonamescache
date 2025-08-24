#!/usr/bin/env python
import csv
import json
from pathlib import Path

p_data = Path('data')

reader = csv.reader(p_data.joinpath('us_counties.txt').open())

state_name_idx = 0
state_fips_idx = 1
county_fips_idx = 2
county_name_idx = 4

counties = []
for line in reader: 
    current_line = line[0].split("|")
    counties.append(
        {
            'fips': current_line[state_fips_idx] + current_line[county_fips_idx], 
            'name': current_line[county_name_idx], 
            'state': current_line[state_name_idx]
        }
    )

p_data.joinpath('us_counties.json').write_text(json.dumps(counties))
