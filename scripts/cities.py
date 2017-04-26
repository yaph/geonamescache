#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import json
from collections import defaultdict

cities = {}
cities_by_name = defaultdict(list)
data_file = io.open('data/cities1000.txt', 'r', encoding='utf-8')

for record in data_file:

    record = record.strip()
    record_list = record.split('\t')

    (geonameid, name, asciiname, alternatenames, latitude, longitude,
    featureclass, featurecode, countrycode, cc2, admin1code, admin2code,
    admin3code, admin4code, population, elevation, dem, timezone,
    modificationdate) = record_list

    if len(record_list) != 19:
        raise ValueError('Invalid record format :\n' + record)

    # Handle any trailing and leading spaces
    name = name.strip()
    asciiname = asciiname.strip()

    # required because used as key
    if not geonameid or not name:
        continue

    # Filter out records which are not of featureclass type P
    # http://www.geonames.org/export/codes.html
    if featureclass and featureclass != 'P':
        continue

    admin_level_1_code = None
    admin_level_2_code = None

    if countrycode and admin1code :
        admin_level_1_code = countrycode + '.' + admin1code
        if admin2code :
            admin_level_2_code = admin_level_1_code + '.' + admin2code


    alternatenames_list = [alternatename.strip() for alternatename in alternatenames.split(',')
                            if alternatename.strip() != '']

    cities[geonameid] = {
        'geonameid': int(geonameid),
        'name': name,
        'asciiname': asciiname.strip(),
        'alternatenames': alternatenames_list,
        'latitude': float(latitude),
        'longitude': float(longitude),
        'countrycode': countrycode,
        'population': int(population),
        'timezone': timezone,
        'admin_level_1_code': admin_level_1_code,
        'admin_level_2_code': admin_level_2_code
    }


    all_names = set()
    all_names.add(name)
    if asciiname != '':
        all_names.add(asciiname)

    all_names.update(alternatenames_list)

    for possible_name in all_names:
        cities_by_name[possible_name].append(geonameid)


with open('geonamescache/cities.json', 'w') as f:
    json.dump(cities, f)

with open('geonamescache/cities_by_name.json', 'w') as f:
    json.dump(cities_by_name, f)
