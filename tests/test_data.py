# -*- coding: utf-8 -*-
from geonamescache import GeonamesCache


geonamescache = GeonamesCache()


def test_cities_len():
    # Make sure there are more than 25000 cities
    assert 25000 < len(geonamescache.get_cities())


def test_countries_len():
    # Make sure there are more than 250 countries
    assert 250 < len(geonamescache.get_countries())


def test_us_counties_len():
    # Make sure there are more than 3000 counties
    us_counties = geonamescache.get_us_counties()
    assert 3000 < len(us_counties)