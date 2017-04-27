import csv
import os
import re
from collections import defaultdict
from unidecode import unidecode


class ResolutionTypes(object):

    OTHER = 'OTHER'
    COUNTRY = 'COUNTRY'
    ADMIN_1 = 'ADMIN_1'
    ADMIN_2 = 'ADMIN_2'
    CITY = 'CITY'

def _fix_loc_name_str(name):
    if name is not None:
        return unidecode(unicode(name, 'utf8')).title()

def _get_resolution(data):
    if data['city']:
        return ResolutionTypes.CITY
    if data['county']:
        return ResolutionTypes.ADMIN_2
    if data['state']:
        return ResolutionTypes.ADMIN_1
    if data['country']:
        return ResolutionTypes.COUNTRY
    raise ValueError

def _load_data():
    locations = defaultdict(list)

    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'osm_data.tsv')
    ) as loc_file:
        csv_reader = csv.reader(loc_file, delimiter='\t')
        keys = next(csv_reader)

        for row in csv_reader:
            assert len(row) == 23
            loc_info = dict(zip(keys, row))

            data = dict(
                resolution=_get_resolution(loc_info),
                name=_fix_loc_name_str(loc_info['name']),
                latitude=float(loc_info['lat']),
                longitude=float(loc_info['lon']),
                country_code=loc_info['country_code'].upper(),
                importance=float(loc_info['importance']),
                city=_fix_loc_name_str(loc_info['city']),
                admin2=_fix_loc_name_str(loc_info['county']),
                admin1=_fix_loc_name_str(loc_info['state']),
                country=_fix_loc_name_str(loc_info['country']),
            )
            ascii_alt_names = [
                name for name in loc_info['alternative_names'].split(',')
                if all(ord(c) < 128 for c in name)
            ]
            all_names = set(
                _fix_loc_name_str(name) for name in [loc_info['name']] + ascii_alt_names
            )
            for name in all_names:
                locations[name].append(data)

    return locations

_LOCATIONS = _load_data()

# for testing
def print_search(name):
    for result in _LOCATIONS[name]:
        print result['resolution'], result['name'], result['admin1'], result['country_code']

def city_search(city_name):
    gc_search_name = re.sub(r'^St\b', 'St.', city_name, flags=re.IGNORECASE)
    gc_search_name = re.sub(r'^N\.?Y\.?C\.?$', 'New York City', gc_search_name, flags=re.IGNORECASE)
    gc_search_name = re.sub(r'Manhattan', 'New York City', gc_search_name, flags=re.IGNORECASE)
    gc_search_name = re.sub(r'^City\s+Of\s+', '', gc_search_name, flags=re.IGNORECASE)

    return [e for e in _LOCATIONS[gc_search_name] if e['resolution'] == ResolutionTypes.CITY]

def admin1_search(admin1_name):
    return [e for e in _LOCATIONS[admin1_name] if e['resolution'] == ResolutionTypes.ADMIN_1]

def admin2_search(admin2_name):
    return [e for e in _LOCATIONS[admin2_name] if e['resolution'] == ResolutionTypes.ADMIN_2]

US_RE = re.compile(r'^(u\.?s\.?a\.?|u\.s\.?)$', flags=re.IGNORECASE)
BRITAIN_RE = re.compile(r'^(england|britain|u\.?k\.?)$', flags=re.IGNORECASE)

def country_search(country_name):
    if US_RE.search(country_name):
        country_name = u'United States'
    elif BRITAIN_RE.search(country_name):
        country_name = u'United Kingdom'
    elif country_name == u'Holland':
        country_name = u'Netherlands'

    return [e for e in _LOCATIONS[country_name] if e['resolution'] == ResolutionTypes.COUNTRY]

CONTINENTS = {
    u'Africa', u'Asia', u'Europe', u'North America', u'South America', u'Oceania',
    u'Antarctica', u'Central America', u'Middle East',
}
OCEANS = {u'Atlantic', u'Pacific', u'Indian', u'Southern', u'Arctic'}

def continent_search(continent_name):
    if continent_name not in CONTINENTS:
        return []
    return [dict(
        resolution=ResolutionTypes.OTHER,
        name=continent_name,
    )]

def ocean_search(ocean_name):
    if ocean_name not in OCEANS:
        return []
    return [dict(
        resolution=ResolutionTypes.OTHER,
        name=ocean_name,
    )]

def find_all_location_matches(name):
    matches = []
    for lookup in (
        city_search, admin1_search, admin2_search, country_search, continent_search, ocean_search
    ):
        matches.extend(lookup(name))
    return matches
