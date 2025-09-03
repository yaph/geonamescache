#!/usr/bin/env python
import csv
import json
from pathlib import Path

p_data = Path('datasets')

for min_population in [500, 1000, 5000, 15000]:
    cities = {}
    slug = f'cities{min_population}'
    reader = csv.reader(p_data.joinpath(slug + '.txt').open(encoding='utf-8'), 'excel-tab')

    for record in reader:
        (
            geonameid,
            name,
            asciiname,
            alternatenames,
            latitude,
            longitude,
            featureclass,
            featurecode,
            countrycode,
            cc2,
            admin1code,
            admin2code,
            admin3code,
            admin4code,
            population,
            elevation,
            dem,
            timezone,
            modificationdate,
        ) = record

        # required because used as key
        if not geonameid:
            continue

        cities[geonameid] = {
            'geonameid': int(geonameid),
            'name': name,
            'latitude': float(latitude),
            'longitude': float(longitude),
            'countrycode': countrycode,
            'population': int(population),
            'timezone': timezone,
            'admin1code': admin1code,
            'alternatenames': alternatenames.split(','),
        }

    p_data.joinpath(slug + '.json').write_text(json.dumps(cities))
