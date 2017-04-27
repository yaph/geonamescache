#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import json
from collections import defaultdict

admin_level_2 = {}
admin_level_2_by_name = defaultdict(list)
data_file = io.open('data/admin2Codes.txt', 'r', encoding='utf-8')

for record in data_file:

    record = record.strip()
    record_list = record.split('\t')

    (admin_level_2_code, name, asciiname, geonameid) = record_list

    if len(record_list) != 4:
        raise ValueError('Invalid record format :\n' + record)

    # Handle any trailing and leading spaces
    name = name.strip()
    asciiname = asciiname.strip()

    # For few records the name field if empty
    if not name :
        name = asciiname

    # required fields
    if not geonameid or not name or not admin_level_2_code:
        continue

    admin_level_2_code_splits = admin_level_2_code.split('.')
    admin_level_1_code = admin_level_2_code_splits[0] + '.' + admin_level_2_code_splits[1]
    country_code = admin_level_2_code_splits[0]

    admin_level_2[admin_level_2_code] = {
        'geonameid': int(geonameid),
        'name': name,
        'asciiname': asciiname,
        'country_code': country_code,
        'admin_level_1_code': admin_level_1_code
    }

    all_names = set()
    all_names.add(name)
    if asciiname != '':
        all_names.add(asciiname)

    for possible_name in all_names:
        admin_level_2_by_name[possible_name].append(admin_level_2_code)

with open('geonamescache/admin_level_2.json', 'w') as f:
    json.dump(admin_level_2, f)

with open('geonamescache/admin_level_2_by_name.json', 'w') as f:
    json.dump(admin_level_2_by_name, f)
