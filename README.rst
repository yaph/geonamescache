Geonames Cache
==============

.. image:: https://badge.fury.io/py/geonamescache.png
        :target: http://badge.fury.io/py/geonamescache
.. image:: https://travis-ci.org/yaph/geonamescache.png?branch=master
        :target: https://travis-ci.org/yaph/geonamescache

A Python library that provides functions to retrieve names and codes of
continents, countries and US states as Python dictionaries.

Geonames data is obtained from `GeoNames
<http://www.geonames.org/>`_.


Installation
------------

To install geonamescache, run: ::

    $ sudo pip install geonamescache

Or, if necessary: ::

    $ sudo easy_install geonamescache


Usage
-----

A simple usage example: ::

    import geonamescache

    gc = geonamescache.GeonamesCache()
    countries = gc.get_countries()
    # print countries dictionary
    print(countries)
    # you really wanna do something more useful with the data...


Methods
-------

Currently geonamescache provides the following methods, that all return
dictionaries with the requested data:

- get_continents()
- get_countries()
- get_us_states()
- get_cities()
- get_countries_by_names()
- get_us_states_by_names()
- get_cities_by_name(name)

TODOs
-----

- analyze performance of get_cities_by_name
- call get_dataset_by_key with name of dataset, so there is no need for \*_by_names methods

Contributing
------------

1. Fork `the repository`_ on GitHub
2. Commit your changes to the **develop** branch
3. Write test(s) for any new feature
4. Push your changes and send a pull request

.. _`the repository`: http://github.com/yaph/geonamescache