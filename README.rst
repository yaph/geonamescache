Geonames Cache
==============

.. image:: https://img.shields.io/pypi/v/geonamescache.svg
        :target: https://pypi.python.org/pypi/geonamescache
.. image:: https://travis-ci.org/yaph/geonamescache.png?branch=master
        :target: https://travis-ci.org/yaph/geonamescache

A Python library that provides functions to retrieve names, ISO and FIPS codes of continents, countries as well as US states and counties as Python dictionaries. The country and city datasets also include population and geographic data.

Geonames data is obtained from `GeoNames <http://www.geonames.org/>`_.


Installation
------------

To install geonamescache, run: ::

    $ sudo pip install geonamescache

Or, if necessary: ::

    $ sudo easy_install geonamescache


Usage
-----

A simple usage example:

::

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
- get_us_counties()


Mappers
-------

The mappers module provides function(s) to map data properties. Currently you can create a mapper that maps country properties, e. g. the ``name`` property to the ``iso3`` property, to do so you'd write the following code:

::

    from geonamescache.mappers import country
    mapper = country(from_key='name', to_key='iso3')

    iso3 = mapper('Spain') # iso3 is assigned ESP


Contributing
------------

1. Fork `the repository`_ on GitHub
2. Commit your changes to the **develop** branch
3. Write test(s) for any new feature
4. Push your changes and send a pull request

If you wish to build the data from scratch, you can run the fabric file, fabfile.py. Before you can run this, you need to `create an account`_ in the Geonames system, then `activate your account`_ for API usage. Once you've created your account, you can run:

fab dl  # Download the geonames data to the data directory
GEONAMES_USER=<your-username-here> fab tojson  # Convert the downloaded data to json

.. _`the repository`: http://github.com/yaph/geonamescache
.. _`activate your account`: http://www.geonames.org/manageaccount
.. _`create an account`: http://www.geonames.org/login
