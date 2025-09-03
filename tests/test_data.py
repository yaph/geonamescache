from geonamescache import GeonamesCache

gc = GeonamesCache()


def test_cities_len():
    # Make sure there are more than 25000 cities
    assert len(gc.get_cities()) > 25000


def test_countries_len():
    # Make sure there are more than 250 countries
    assert len(gc.get_countries()) > 250


def test_us_counties_len():
    # Make sure there are more than 3000 counties
    us_counties = gc.get_us_counties()
    assert len(us_counties) > 3000


def test_continents():
    continents = gc.get_continents()
    testdata = (
        ('AF', 'Africa'),
        ('AN', 'Antarctica'),
        ('AS', 'Asia'),
        ('EU', 'Europe'),
        ('NA', 'North America'),
        ('OC', 'Oceania'),
        ('SA', 'South America'),
    )
    for code, name in testdata:
        assert code in continents
        assert name == continents[code]['name']

    for code in ['XX', 'OO']:
        assert code not in continents


def test_countries():
    countries = gc.get_countries()
    testdata = (('ES', 'Spain'), ('FR', 'France'), ('US', 'United States'))
    for code, name in testdata:
        assert code in countries
        assert name == countries[code]['name']

    for code in ['XX', 'OO']:
        assert code not in countries


def test_us_counties_fips():
    # Ensure correct mapping
    us_counties = {c['fips']: c for c in gc.get_us_counties()}
    assert us_counties['01001']['name'] == 'Autauga County'
    assert us_counties['06037']['name'] == 'Los Angeles County'


def test_us_states():
    us_states = gc.get_us_states()

    testdata = (('NM', 'New Mexico'), ('CA', 'California'), ('NV', 'Nevada'))
    for code, name in testdata:
        assert code in us_states
        assert name == us_states[code]['name']

    for code in ['XX', 'OO']:
        assert code not in us_states
