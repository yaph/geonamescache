#!/usr/bin/env python
# coding: utf-8
import json
import unicodecsv as csv

counties = []

with open('../data/us_counties.txt', 'r') as f:
    r = csv.reader(f, encoding='utf-8')
    headers = r.next()
    for line in r:
        counties.append({
            'fips': line[1] + line[2],
            'name': line[3],
            'state': line[0]
        })

with open('../geonamescache/us_counties.json', 'w') as f:
    json.dump(counties, f)
