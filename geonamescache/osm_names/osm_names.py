import csv
import json
import os
from collections import defaultdict

from utils import (
    get_alt_punc_names,
    ResolutionTypes,
    standardize_loc_name,
)


def load_data():
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

    alt_names_by_id = _load_alt_names_if_possible(os.path.join(data_dir, 'alt_wiki_names.json'))
    locations_by_name, locations_by_id = _load_main_data(
        os.path.join(data_dir, 'osm_data.tsv'), alt_names_by_id
    )
    _add_state_abbreviations(os.path.join(data_dir, 'us_states.tsv'), locations_by_name)
    _add_missing_countries(
        os.path.join(data_dir, 'countries.json'), locations_by_name, locations_by_id
    )
    _assign_parent_loc_ids(locations_by_name, locations_by_id)
    _add_fixed_alt_names(locations_by_name)

    del locations_by_name['']

    return locations_by_name, locations_by_id

def _load_alt_names_if_possible(filepath):
    alt_names_by_id = defaultdict(list)
    if not os.path.isfile(filepath) or True:
        return alt_names_by_id

    with open(filepath) as alt_names_file:
        alt_names_by_id_copy = json.load(alt_names_file)
        for id_, alt_names in alt_names_by_id_copy.iteritems():
            assert int(id_) not in alt_names_by_id
            alt_names_by_id[int(id_)] = alt_names

    return alt_names_by_id

def _load_main_data(filepath, alt_names_by_id):
    locations_by_name = defaultdict(dict)
    locations_by_id = {}

    with open(filepath) as loc_file:
        csv_reader = csv.reader(loc_file, delimiter='\t')
        keys = next(csv_reader)
        last_importance = 1.

        for row in csv_reader:
            assert len(row) == 23
            loc_info = dict(zip(keys, row))
            importance = float(loc_info['importance'])
            assert importance <= last_importance
            last_importance = importance

            resolution = _get_resolution(loc_info)
            if not resolution:
                continue

            data = dict(
                id=int(loc_info['osm_id']),
                resolution=resolution,
                name=standardize_loc_name(loc_info['name']),
                latitude=float(loc_info['lat']),
                longitude=float(loc_info['lon']),
                importance=importance,
                city=standardize_loc_name(loc_info['city']),
                admin_level_2=standardize_loc_name(loc_info['county']),
                admin_level_1=standardize_loc_name(loc_info['state']),
                country=standardize_loc_name(loc_info['country']),
                country_code=loc_info['country_code'].upper(),
            )

            if _should_skip_location(data, locations_by_name):
                continue

            alt_osm_names = [
                name for name in loc_info['alternative_names'].split(',')
                if all(ord(c) < 128 for c in name)
            ]
            alt_wiki_names = alt_names_by_id[data['id']]
            alt_punc_name = get_alt_punc_names(loc_info['name'])

            all_names = set(
                standardize_loc_name(name)
                for name in [loc_info['name']] + alt_osm_names + alt_wiki_names + alt_punc_name
            )
            for name in all_names:
                locations_by_name[name][data['id']] = data

            assert data['id'] not in locations_by_id
            locations_by_id[data['id']] = data

    return locations_by_name, locations_by_id

def _get_resolution(data):
    for res_name, resolution in (
        (data['city'], ResolutionTypes.CITY),
        (data['county'], ResolutionTypes.ADMIN_2),
        (data['state'], ResolutionTypes.ADMIN_1),
        (data['country'], ResolutionTypes.COUNTRY),
    ):
        if res_name:
            if data['name'] != res_name:
                # Location name does not match the highest resolution field.
                if resolution == ResolutionTypes.COUNTRY:
                    # There are some unusual results here; ignore them.
                    return None
                if resolution == ResolutionTypes.CITY:
                    # The city name seems generally more accurate, make the location name the
                    # city name.
                    data['name'] = data['city']
                else:
                    # Otherwise, assume this location is a city.
                    data['city'] = data['name']
                return ResolutionTypes.CITY
            return resolution

    raise ValueError("Location is missing names for all location levels")

def _should_skip_location(loc_data, locations_by_name):
    for other_location in locations_by_name[loc_data['name']].itervalues():
        if all(
            other_location[field] == loc_data[field]
            for field in ('name', 'city', 'admin_level_1', 'admin_level_2', 'country')
        ):
            # Some locations appear as twice in the data set. If we already saw a location with
            # the same location identifiers, just the keep the first (most important) entry.
            return True

        if (
            loc_data['resolution'] == ResolutionTypes.CITY and
            other_location['resolution'] == ResolutionTypes.CITY and
            all(
                loc_data[field] == other_location[field] or not loc_data[field]
                for field in ('name', 'city', 'admin_level_1', 'admin_level_2', 'country')
            )
        ):
            # Some cities appear as less specific versions of previous cities. Again just keep
            # the first entry.
            return True
    return False

def _add_state_abbreviations(filepath, locations_by_name):
    """
    We think the abbreviation for a US state can be a name, so add them to the locations map.
    """
    with open(filepath) as states_file:
        csv_reader = csv.reader(states_file, delimiter='\t')
        for state, abbrev in csv_reader:
            assert len(abbrev) == 2
            state = standardize_loc_name(state)

            state_found = False
            for candidate in locations_by_name[state].itervalues():
                if (
                    candidate['resolution'] == ResolutionTypes.ADMIN_1 and
                    candidate['admin_level_1'] == state and
                    candidate['country_code'] == u'US'
                ):
                    for abbrev_name in (abbrev, '%s.%s.' % (abbrev[0], abbrev[1])):
                        abbrev_name = standardize_loc_name(abbrev_name)
                        locations_by_name[abbrev_name][candidate['id']] = candidate
                    state_found = True
                    break

            if not state_found:
                raise ValueError

def _add_missing_countries(filepath, locations_by_name, locations_by_id):
    """
    Some countries appear as countries for another location, but don't appear as a distinct row
    themselves. Add these precalculated countries to the data.
    """
    if not os.path.isfile(filepath):
        return

    with open(filepath) as country_file:
        missing_countries = json.load(country_file)

    for country in missing_countries:
        alt_wiki_names = country['alt_names']
        del country['alt_names']

        for alt_name in set(
            standardize_loc_name(name)
            for name in [country['name']] + alt_wiki_names + get_alt_punc_names(country['name'])
        ):
            locations_by_name[alt_name][country['id']] = country

        assert country['id'] not in locations_by_id
        locations_by_id[country['id']] = country

def _assign_parent_loc_ids(locations_by_name, locations_by_id):
    country_code_to_id = {}
    for location in locations_by_id.itervalues():
        if location['resolution'] == ResolutionTypes.COUNTRY:
            assert location['country_code'] not in country_code_to_id
            country_code_to_id[location['country_code']] = location['id']

    for location in locations_by_id.itervalues():
        location['country_id'] = country_code_to_id.get(location['country_code'])

        if location['resolution'] in (ResolutionTypes.CITY, ResolutionTypes.ADMIN_2):
            location['admin_level_1_id'] = _find_admin_id(
                locations_by_name, location, ResolutionTypes.ADMIN_1
            )
        if location['resolution'] == ResolutionTypes.CITY:
            location['admin_level_2_id'] = _find_admin_id(
                locations_by_name, location, ResolutionTypes.ADMIN_2
            )

def _find_admin_id(locations_by_name, location, resolution):
    """
    Searches for an admin that matches the desired name, resolution, admin1, and country.
    If the location does not have an admin name or if we cannot find exactly one match, the
    returned id will be 0.
    """
    assert resolution in (ResolutionTypes.ADMIN_1, ResolutionTypes.ADMIN_2)
    if resolution == ResolutionTypes.ADMIN_1:
        admin_name = location['admin_level_1']
    else:
        admin_name = location['admin_level_2']

    if not admin_name:
        return 0

    admin_candidates = [
        loc for loc in locations_by_name[admin_name].itervalues()
        if (
            loc['resolution'] == resolution and
            loc['name'] == admin_name and
            loc['admin_level_1'] == location['admin_level_1'] and
            loc['country_code'] == location['country_code']
        )
    ]
    if len(admin_candidates) == 0:
        # Data set is missing lots of admins as distinct locations
        return 0
    elif len(admin_candidates) == 1:
        return admin_candidates[0]['id']
    else:
        # There are multiple possibilities for the admin.
        # (This occurred only once in my testing.)
        return 0

def _add_fixed_alt_names(locations_by_name):
    for real_name, alt_names, resolution in (
        (
            'United States of America',
            ('USA', 'U.S.A.', 'US', 'U.S.', 'the United States'),
            ResolutionTypes.COUNTRY
        ),
        ('United Kingdom', ('Great Britain', 'Britain', 'UK', 'U.K.'), ResolutionTypes.COUNTRY),
        ('South Korea', ('Korea',), ResolutionTypes.COUNTRY),
        ('North Korea', ('Korea',), ResolutionTypes.COUNTRY),
        ('The Netherlands', ('Netherlands', 'Holland',), ResolutionTypes.COUNTRY),
        ('New York City', ('NYC', 'N.Y.C.'), ResolutionTypes.CITY),
    ):
        locations = [
            loc for loc in locations_by_name[standardize_loc_name(real_name)].itervalues()
            if loc['resolution'] == resolution
        ]
        assert len(locations) == 1
        location = locations[0]

        for alt_name in alt_names:
            locations_by_name[standardize_loc_name(alt_name)][location['id']] = location

