# GeonamesCache

[![image](https://img.shields.io/pypi/v/geonamescache.svg)](https://pypi.python.org/pypi/geonamescache)

A Python library that provides functions to retrieve names, ISO and FIPS codes of continents, countries as well as US states and counties as Python dictionaries. The country and city datasets also include population and geographic data.

Geonames data is obtained from [GeoNames](http://www.geonames.org/).

## Installation

    pip install geonamescache

## Usage

A simple usage example:

    import geonamescache

    gc = geonamescache.GeonamesCache()
    countries = gc.get_countries()
    # print countries dictionary
    print(countries)
    # you really wanna do something more useful with the data...

## Settings

### Cities dataset

When creating a `GeonamesCache` you can set the `min_city_population` parameter to either of 500, 1000, 5000 or the default 15000. The smaller the minimum popluation the more cities are included in the cities dataset.

*New in version 1.4*

## Methods

Currently geonamescache provides the following methods, that return dictionaries with the requested data:

* get\_continents()
* get\_countries()
* get\_us\_states()
* get\_cities()
* get\_countries\_by\_names()
* get\_us\_states\_by\_names()
* get\_cities\_by\_name(name)
* get\_us\_counties()

In addition you can search for cities by name.

* search\_cities(\'NAME\', case\_sensitive=True)

This function returns a list of city records that match the given `NAME`.

* By default the `alternatenames` attribute is searched for matches.
* By default the search is case sensitive, it can be made case insensitive by changing `case_sensitive` to False.

## Mappers

The mappers module provides function(s) to map data properties. Currently you can create a mapper that maps country properties, e. g. the `name` property to the `iso3` property, to do so you\'d write the following code:

    from geonamescache.mappers import country
    mapper = country(from_key='name', to_key='iso3')

    iso3 = mapper('Spain') # iso3 is assigned ESP

## Contributing

Please write test(s) for any new feature. If you wish to build the data from scratch, run `make dl` and `make json`.
