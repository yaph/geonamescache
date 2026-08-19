#!/usr/bin/env python
import csv
import json
from pathlib import Path

p_data = Path('datasets')

timezones = {}

reader = csv.reader(p_data.joinpath('timeZones.txt').open(encoding='utf-8'), 'excel-tab')
for record in reader:
    countrycode, timezoneid, gmtoffset, dstoffset, rawoffset = record

    # The header row names the offset columns after the current year, so match
    # on the first column instead, which is stable.
    if countrycode == 'CountryCode':
        continue

    # required because used as key
    if not timezoneid:
        continue

    timezones[timezoneid] = {
        'countrycode': countrycode,
        'timezoneid': timezoneid,
        'gmtoffset': float(gmtoffset),
        'dstoffset': float(dstoffset),
        'rawoffset': float(rawoffset),
    }

p_data.joinpath('timezones.json').write_text(json.dumps(timezones, ensure_ascii=False))
