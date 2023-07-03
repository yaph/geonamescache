# -*- coding: utf-8 -*-
# GeonamesCache Mappings test cases.
from geonamescache import mappings
from geonamescache.mappers import country


# Test a few mappings to make sure mappings work.
def test_mappings():
    assert mappings.country_names['Macau'] == 'Macao'
    assert mappings.country_names['Pitcairn Islands'] == 'Pitcairn'
    assert mappings.country_names['Saint Barthélemy'] == 'Saint Barthelemy'


def test_country_name_iso3_mapper():
    mapper = country(from_key='name', to_key='iso3')
    assert mapper('Burma') == 'MMR'
    assert mapper('South Korea') == 'KOR'
    assert mapper('The Netherlands') == 'NLD'
    assert mapper('USA') == 'USA'
