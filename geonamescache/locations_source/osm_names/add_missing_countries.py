import csv
import json
import sys
from collections import defaultdict

import osm_names
from utils import ResolutionTypes
from lookup_alt_names_on_wiki import search


def get_alt_names(name):
    result = search(name)
    if result is None:
        print 'Warning: could not fetch results for ', name
        return []

    return result.get('alt_names', [])

def run(out_filepath):
    """
    There are about 50 countries that appear as a country of a location in the data set, but do
    not appear as a location themselves. Add them to the location map with:
    
    1. a unique id that's larger than the largest existing osm id. 
    2. the lat / long from the countries file
    3. the importance as the importance of the most important city plus .1
    """
    all_country_codes = {}
    present_country_codes = set()
    city_importance_by_country = defaultdict(float)
    locations_by_name, locations_by_id = osm_names.load_data()

    for location in locations_by_id.itervalues():
        country_code = location['country_code']
        country = location['country']

        if country_code in all_country_codes:
            assert all_country_codes[country_code] == country
        else:
            all_country_codes[country_code] = country

        city_importance_by_country[country_code] = max(
            city_importance_by_country[country_code],
            location['importance'],
        )

        if location['resolution'] == ResolutionTypes.COUNTRY:
            present_country_codes.add(country_code)

    google_countries = {}
    with open('data/countries.csv') as country_file:
        csv_reader = csv.reader(country_file)
        for country_code, latitude, longitude, name in csv_reader:
            google_countries[country_code] = dict(
                country_code=country_code,
                latitude=latitude,
                longitude=longitude,
            )

    missing_countries = []
    next_free_id = max(locations_by_id.keys()) + 1

    for country_code, country in all_country_codes.iteritems():
        if country_code in present_country_codes:
            continue

        data = google_countries.get(country_code)
        if not data:
            data = dict(country_code=country_code)

        data.update(dict(
            id=next_free_id,
            resolution=ResolutionTypes.COUNTRY,
            name=country,
            country=country,
            importance=city_importance_by_country[country_code] + .1,
            alt_names=get_alt_names(country),
        ))
        missing_countries.append(data)
        next_free_id += 1

    with open(out_filepath, 'w') as out_file:
        json.dump(missing_countries, out_file)


if __name__ == '__main__':
    run(sys.argv[1])
