# -*- coding: utf-8 -*-

"""
geonamescache
=============

:copyright: (c) 2012 by Ramiro Gómez.
:license: ISC, see LICENSE for more details.

"""

__title__ = 'geonamescache'
__version__ = '0.6dev'
__author__ = 'Ramiro Gómez'
__license__ = 'MIT'
__copyright__ = 'Copyright 2012 Ramiro Gómez'


from . import geonamesdata

class GeonamesCache:

    continents = geonamesdata.continents
    countries = geonamesdata.countries
    us_states = geonamesdata.us_states
    cities = None


    def get_continents(self):
        return self.continents


    def get_countries(self):
        return self.countries


    def get_us_states(self):
        return self.us_states


    def get_countries_by_names(self):
        return dict((d['name'], d) for c, d in self.countries.items())


    def get_cities(self):
        """Get a dictionary of cities keyed by geonameid."""

        return self._load_cities()


    def get_cities_by_name(self, name):
        """Get a list of city dictionaries with the given name.

        City names cannot be used as keys, as they are not unique.
        """
        pass


    def _load_cities(self):
        if self.cities is None:
            import os
            try:
                import cPickle as pickle
            except:
                import pickle
            fc = open(os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                'cities.pickle'), 'rb')
            self.cities = pickle.load(fc)
            fc.close()
        return self.cities

