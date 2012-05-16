Geonames Cache
==============

A Python library that provides functions to retrieve names and codes of continents, countries and US states as Python dictionaries.

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

Currently geonamescache provides the following methods, that all return dictionaries with the requested data:

- get_continents()
- get_countries()
- get_us_states()


Contributing
------------

1. Fork `the repository`_ on GitHub
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Added some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

.. _`the repository`: http://github.com/yaph/geonamescache
