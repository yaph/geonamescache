from geonamescache import GeonamesCache

geonamescache = GeonamesCache()


def test_cities_len():
    # Make sure there are more than 25000 cities
    assert len(geonamescache.get_cities()) > 25000


def test_countries_len():
    # Make sure there are more than 250 countries
    assert len(geonamescache.get_countries()) > 250


def test_us_counties_len():
    # Make sure there are more than 3000 counties
    us_counties = geonamescache.get_us_counties()
    assert len(us_counties) > 3000
