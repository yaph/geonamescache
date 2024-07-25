#!/usr/bin/env python
import csv
import json
from pathlib import Path

countries = {}
p_data = Path('data')

reader = csv.reader(p_data.joinpath('countryInfo.txt').open(), 'excel-tab')
for record in reader:
    if record[0].startswith('#'):
        continue

    (iso, iso3, isonumeric, fips, name, capital, areakm2, population,
    continentcode, tld, currencycode, currencyname, phone, postalcodeformat,
    postalcoderegex, languages, geonameid, neighbours,
    equivalentfipscode) = record

    countries[iso] = {
        'geonameid': int(geonameid) if geonameid else 0,
        'name': name,
        'iso': iso,
        'iso3': iso3,
        'isonumeric': int(isonumeric),
        'fips': fips,
        'continentcode': continentcode,
        'capital': capital,
        'areakm2': int(float(areakm2)) if areakm2 else 0,
        'population': int(population) if population else 0,
        'tld': tld,
        'currencycode': currencycode,
        'currencyname': currencyname,
        'phone': phone,
        'postalcoderegex': postalcoderegex,
        'languages': languages,
        'neighbours': neighbours
    }


Path('data', 'countries.json').write_text(json.dumps(countries))
