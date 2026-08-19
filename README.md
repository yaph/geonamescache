# GeonamesCache

[![image](https://img.shields.io/pypi/v/geonamescache.svg)](https://pypi.python.org/pypi/geonamescache)

A Python library that provides functions to retrieve names, ISO and FIPS codes of continents, countries and first- and second-level administrative divisions as well as US states and counties as Python dictionaries. The country and city datasets also include population and geographic data.

Geonames data is obtained from [GeoNames](http://www.geonames.org/).

## Installation

    pip install geonamescache

## Usage

A simple example:

    import geonamescache

    gc = geonamescache.GeonamesCache()
    print(gc.get_countries())

The datasets are bundled gzipped and parsed on first use, so the installed package is about 36 MB. Each `GeonamesCache` instance caches every dataset it loads, so keep one instance around rather than creating a new one per lookup.

## Settings

### Cities dataset

When creating a `GeonamesCache` you can set the `min_city_population` parameter to either of 500, 1000, 5000 or the default 15000. The smaller the minimum population the more cities are included in the cities dataset.

## Methods

Currently geonamescache provides the following methods, that return dictionaries with the requested data:

* get\_continents()
* get\_countries()
* get\_admin1\_codes()
* get\_admin2\_codes()
* get\_us\_states()
* get\_cities()
* get\_countries\_by\_names()
* get\_us\_states\_by\_names()
* get\_cities\_by\_name(name)
* get\_cities\_by\_names()
* get\_us\_counties()
* get\_timezones()

In addition you can search for cities by name.

* search\_cities(\'NAME\', case\_sensitive=True, contains\_search=True)

This function returns a list of city records that match the given `NAME`.

* By default the `alternatenames` attribute is searched for matches.
* By default the search is case insensitive, it can be made case sensitive by changing `case_sensitive` to True.
* By default the search is contains, it can be made exact equality by changing `contains_search` to False.

To resolve the administrative division a city belongs to, use:

* get\_admin1\_by\_city(city)
* get\_admin2\_by\_city(city)

Both take a city record and return the matching division record, or `None` if the city's codes are missing or not present in the division dataset.

To get the time zones of a country, use:

* get\_timezones\_by\_country(countrycode)

## Data formats

All examples below assume `gc = geonamescache.GeonamesCache()`.

### get_continents()

A dictionary keyed by the two-letter continent code. Records come from the GeoNames web service and contain more fields than shown here.

    >>> gc.get_continents()['EU']['name']
    'Europe'

### get_countries()

A dictionary of 252 countries keyed by ISO alpha-2 code.

    >>> gc.get_countries()['US']
    {
        'geonameid': 6252001,
        'name': 'United States',
        'iso': 'US',
        'iso3': 'USA',
        'isonumeric': 840,
        'fips': 'US',
        'continentcode': 'NA',
        'capital': 'Washington',
        'areakm2': 9629091,
        'population': 327167434,
        'tld': '.us',
        'currencycode': 'USD',
        'currencyname': 'Dollar',
        'phone': '1',
        'postalcoderegex': '^\\d{5}(-\\d{4})?$',
        'languages': 'en-US,es-US,haw,fr',
        'neighbours': 'CA,MX,CU'
    }

`get_countries_by_names()` returns the same records keyed by country name instead, e. g. `gc.get_countries_by_names()['Spain']`.

### get_cities()

A dictionary keyed by geonameid **as a string**, holding 34078 cities at the default minimum population of 15000.

    >>> gc.get_cities()['2747891']
    {
        'geonameid': 2747891,
        'name': 'Rotterdam',
        'latitude': 51.9225,
        'longitude': 4.47917,
        'countrycode': 'NL',
        'population': 868135,
        'timezone': 'Europe/Amsterdam',
        'admin1code': '11',
        'admin2code': '0599',
        'featurecode': 'PPL',
        'alternatenames': ['RTM', 'Ratehrdam', 'Roterdam', ...]
    }

`featurecode` is the GeoNames [feature code](http://www.geonames.org/export/codes.html), which distinguishes a capital (`PPLC`) or an administrative seat (`PPLA` through `PPLA5`) from an ordinary populated place (`PPL`). It is what lets the datasets include capitals below their population threshold, such as Nuuk and Tórshavn. The feature *class* is always `P` in these datasets, so it is not stored. You can search on it:

    >>> len(gc.search_cities('PPLC', attribute='featurecode', contains_search=False))
    241

City names are not unique, so `get_cities_by_name()` returns a list of records. There is a Rotterdam in both the Netherlands and the US state of New York:

    >>> [(c['geonameid'], c['countrycode']) for c in gc.get_cities_by_name('Rotterdam')]
    [(2747891, 'NL'), (5134453, 'US')]

Unknown names give an empty list. The first call builds an index of every city name, so looking up many names costs one pass over the dataset instead of one pass per name. `get_cities_by_names()` returns that whole index, a dictionary mapping each name to its list of records:

    >>> len(gc.get_cities_by_names())
    32215

`search_cities()` returns a flat list of city records instead. It searches `alternatenames` by default, so it matches places whose *other* names contain the query, here the Rotterdam district of Hoogvliet:

    >>> [(c['name'], c['countrycode']) for c in gc.search_cities('Rotterdam')]
    [('Rotterdam', 'NL'), ('Hoogvliet', 'NL')]

Pass `attribute='name'` to search the primary name instead, which finds the US Rotterdam that has no alternate names:

    >>> [(c['name'], c['countrycode']) for c in gc.search_cities('Rotterdam', attribute='name')]
    [('Rotterdam', 'NL'), ('Rotterdam', 'US')]

### get_admin1_codes()

First-level administrative divisions (states, provinces, regions), 3865 records keyed by the composite code `<countrycode>.<admin1code>`, for example `US.CA` for California or `NL.11` for South Holland.

    >>> gc.get_admin1_codes()['NL.11']
    {'asciiname': 'South Holland', 'geonameid': 2743698, 'name': 'South Holland'}

### get_admin2_codes()

Second-level administrative divisions (counties, municipalities, districts), 47592 records keyed by `<countrycode>.<admin1code>.<admin2code>`.

    >>> gc.get_admin2_codes()['NL.11.0599']
    {'asciiname': 'Rotterdam', 'geonameid': 2747890, 'name': 'Rotterdam'}

Note the `geonameid` here is the municipality of Rotterdam (2747890), which is a different place from the city of Rotterdam (2747891).

### get_admin1_by_city() and get_admin2_by_city()

Cities store `countrycode`, `admin1code` and `admin2code` separately, so resolving a division means joining them into the composite key. These helpers do that and handle the cases where a city has no code:

    >>> city = gc.get_cities()['2747891']
    >>> gc.get_admin1_by_city(city)['name']
    'South Holland'
    >>> gc.get_admin2_by_city(city)['name']
    'Rotterdam'

Both return `None` when the city lacks the required codes or the composite key is not in the division dataset, which is why the return value should be checked before subscripting it:

    admin1 = gc.get_admin1_by_city(city)
    region = admin1['name'] if admin1 else 'unknown'

Building the key by hand works too, but silently produces a partial key such as `'NL.'` for cities without an admin1code, so prefer the helpers.

### get_timezones()

Time zones with their UTC offsets, 418 records keyed by IANA time zone id.

    >>> gc.get_timezones()['Europe/Amsterdam']
    {
        'countrycode': 'NL',
        'timezoneid': 'Europe/Amsterdam',
        'gmtoffset': 1.0,
        'dstoffset': 2.0,
        'rawoffset': 1.0
    }

`rawoffset` is the offset excluding daylight saving time. `gmtoffset` and `dstoffset` are the offsets in effect on 1 January and 1 July of the year the dataset was published, so they are a snapshot rather than a live value; use a proper time zone library such as `zoneinfo` if you need the offset at a given moment.

The `timezone` field of every city record is a key into this dictionary:

    >>> city = gc.get_cities()['2747891']
    >>> gc.get_timezones()[city['timezone']]['rawoffset']
    1.0

### get_timezones_by_country(countrycode)

The time zones of one country as a list sorted by time zone id. The country code is an ISO alpha-2 code and is matched case insensitively.

    >>> [tz['timezoneid'] for tz in gc.get_timezones_by_country('NL')]
    ['Europe/Amsterdam']

    >>> len(gc.get_timezones_by_country('US'))
    29

Unknown country codes return an empty list rather than raising:

    >>> gc.get_timezones_by_country('ZZ')
    []

### get_us_states()

A dictionary keyed by the two-letter state code.

    >>> gc.get_us_states()['CA']
    {'code': 'CA', 'name': 'California', 'fips': '06', 'geonameid': 5332921}

`get_us_states_by_names()` returns the same records keyed by state name, e. g. `gc.get_us_states_by_names()['California']`.

### get_us_counties()

A **list** of 3235 county records, not a dictionary, sourced from the US Census Bureau rather than GeoNames.

    >>> gc.get_us_counties()[0]
    {'fips': '01001', 'name': 'Autauga County', 'state': 'AL'}

To look counties up, key the list yourself:

    counties = {c['fips']: c for c in gc.get_us_counties()}
    counties['06037']['name']  # 'Los Angeles County'

## Mappers

The mappers module provides function(s) to map data properties. Currently you can create a mapper that maps country properties, e. g. the `name` property to the `iso3` property, to do so you'd write the following code:

    from geonamescache.mappers import country
    mapper = country(from_key='name', to_key='iso3')

    iso3 = mapper('Spain') # iso3 is assigned ESP

## Contributing

Please write test(s) for any new feature. If you wish to build the data from scratch, run `make dl` and `make json`. The `bin/` scripts write plain JSON into `datasets/`, and `bin/compress_data.py` gzips it into `geonamescache/data/` as the last step of `make json`.
