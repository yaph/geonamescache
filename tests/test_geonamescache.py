from geonamescache import GeonamesCache

gc = GeonamesCache()


def test_get_admin1_codes():
    admin1 = gc.get_admin1_codes()
    assert len(admin1) > 3000
    for key, name, geonameid in (
        ('US.CA', 'California', 5332921),
        ('ES.51', 'Andalusia', 2593109),
    ):
        assert name == admin1[key]['name']
        assert geonameid == admin1[key]['geonameid']


def test_admin1_code_resolves_city_reference():
    # Cities store countrycode and admin1code separately, the composite
    # admin1 key allows resolving these references.
    city = gc.get_cities()['5368361']
    assert 'Los Angeles' == city['name']
    key = f"{city['countrycode']}.{city['admin1code']}"
    assert 'California' == gc.get_admin1_codes()[key]['name']


def test_get_countries_by_names():
    # Length of get_countries_by_names dict and get_countries dict must be
    # the same, unless country names wouldn't be unique.
    assert len(gc.get_countries_by_names()), len(gc.get_countries())


def test_get_cities_by_name():
    cities = gc.get_cities()
    for gid, name in (('3191316', 'Samobor'), ('3107112', 'Rivas-Vaciamadrid')):
        assert name == cities[gid]['name']


def test_get_cities_by_name_madrid():
    assert len(gc.get_cities_by_name('Madrid')) > 1


def test_cities_in_us_states():
    cities = gc.get_cities()
    for gid, name, us_state in (('4164138', 'Miami', 'FL'), ('4525353', 'Springfield', 'OH')):
        assert name == cities[gid]['name']
        assert us_state == cities[gid]['admin1code']


def test_search_cities():
    cities = gc.search_cities('Kiev')
    assert len(cities) >= 1


def test_search_cities_case_sensitive():
    cities = gc.search_cities('Stoke-On-Trent', case_sensitive=True)
    assert len(cities) == 0
    cities = gc.search_cities('Stoke-On-Trent')
    assert len(cities) == 1


def test_search_cities_alternatenames_contains_search():
    assert (
        len(gc.search_cities('London'))
        > len(gc.search_cities('London', contains_search=False))
        > 1
    )


def test_search_cities_name_contains_search():
    assert (
        len(gc.search_cities('London', 'name'))
        > len(gc.search_cities('London', 'name', contains_search=False))
        > 1
    )


def test_search_cities_alternatenames_contains_search_and_case_sensitive():
    assert (
        len(gc.search_cities('London', case_sensitive=True))
        > len(gc.search_cities('London', case_sensitive=True, contains_search=False))
        > 1
    )


def test_search_cities_name_contains_search_and_case_sensitive():
    assert (
        len(gc.search_cities('London', 'name', case_sensitive=True))
        > len(gc.search_cities('London', 'name', case_sensitive=True, contains_search=False))
        > 1
    )
