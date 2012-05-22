# -*- coding: utf-8 -*-

"""
geonamescache
=============

:copyright: (c) 2012 by Ramiro Gómez.
:license: ISC, see LICENSE for more details.

"""

__title__ = 'geonamescache'
__version__ = '0.6'
__author__ = 'Ramiro Gómez'
__license__ = 'MIT'
__copyright__ = 'Copyright 2012 Ramiro Gómez'


from . import geonamesdata

class GeonamesCache:

    continents = geonamesdata.continents
    countries = geonamesdata.countries
    us_states = geonamesdata.us_states

    cities = None
    cities_items = None
    cities_by_names = {}


    def get_dataset_by_key(self, dataset, key):
        return dict((d[key], d) for c, d in dataset.items())


    def get_continents(self):
        return self.continents


    def get_countries(self):
        return self.countries


    def get_us_states(self):
        return self.us_states


    def get_countries_by_names(self):
        return self.get_dataset_by_key(self.countries, 'name')


    def get_us_states_by_names(self):
        return self.get_dataset_by_key(self.us_states, 'name')


    def get_cities(self):
        """Get a dictionary of cities keyed by geonameid."""

        return self._load_cities()


    def get_cities_by_name(self, name):
        """Get a list of city dictionaries with the given name.

        City names cannot be used as keys, as they are not unique.
        """

        if name not in self.cities_by_names:
            if self.cities_items is None:
                self.cities_items = self.get_cities().items()
            self.cities_by_names[name] = [dict({gid: city}) 
                for gid, city in self.cities_items if city['name'] == name]
        return self.cities_by_names[name]


    def _load_cities(self):
        if self.cities is None:
            import os, json
            fc = open(os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 'cities.json'), 'r')
            self.cities = json.load(fc)
            fc.close()
        return self.cities

