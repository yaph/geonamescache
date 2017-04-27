#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import json

fcsv = open('data/countryInfo.txt', 'r')
reader = csv.reader(fcsv, 'excel-tab')
headers = next(reader)
countries = {}

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

with open('geonamescache/countries.json', 'w') as f:
    json.dump(countries, f)
