# -*- coding: utf-8 -*-
"""
geonamescache
=============

:copyright: (c) 2016 by Ramiro Gómez.
:license: ISC, see LICENSE for more details.

"""

__title__ = 'geonamescache'
__version__ = '0.3.1'
__author__ = 'Ramiro Gómez'
__license__ = 'MIT'


import os
import json
from . import geonamesdata

class GeonamesCache:

    continents = None
    countries = None
    us_states = geonamesdata.us_states
    admin_level_1 = None
    admin_level_1_by_name = None
    us_counties = None
    admin_level_2 = None
    admin_level_2_by_name = None
    cities = None
    cities_by_name = None

    datadir = os.path.dirname(os.path.abspath(__file__))

    def get_dataset_by_key(self, dataset, key):
        return dict((d[key], d) for c, d in list(dataset.items()))

    def get_continents(self):
        if self.continents is None:
            self.continents = self._load_data(
                self.continents, 'continents.json')
        return self.continents

    def get_countries(self):
        if self.countries is None:
            self.countries = self._load_data(self.countries, 'countries.json')
        return self.countries

    def get_countries_by_names(self):
        return self.get_dataset_by_key(self.get_countries(), 'name')

    def get_us_states(self):
        return self.us_states

    def get_us_states_by_names(self):
        return self.get_dataset_by_key(self.get_us_states(), 'name')

    def get_admin_level_1(self):
        """Get a dictionary of admin_level_1 keyed by admin_level_1_code."""
        if self.admin_level_1 is None:
            self._load_admin_level_1_data()
        return self.admin_level_1

    def get_admin_level_1_by_name(self, name):
        if self.admin_level_1 is None:
            self._load_admin_level_1_data()

        if name in self.admin_level_1_by_name:
            return [dict({code: self.admin_level_1[code]})
                for code in self.admin_level_1_by_name[name]]
        return []

    def get_us_counties(self):
        if self.us_counties is None:
            self.us_counties = self._load_data(
                self.us_counties, 'us_counties.json')
        return self.us_counties

    def get_admin_level_2(self):
        """Get a dictionary of admin_level_2 keyed by admin_level_2_code."""
        if self.admin_level_2 is None:
            self._load_admin_level_2_data()
        return self.admin_level_2

    def get_admin_level_2_by_name(self, name):
        if self.admin_level_2 is None:
            self._load_admin_level_2_data()

        if name in self.admin_level_2_by_name:
            return [dict({code: self.admin_level_2[code]})
                for code in self.admin_level_2_by_name[name]]
        return []

    def get_cities(self):
        """Get a dictionary of cities keyed by geonameid."""
        if self.cities is None:
            self._load_cities_data()
        return self.cities

    def get_cities_by_name(self, name):
        if self.cities is None:
            self._load_cities_data()

        if name in self.cities_by_name:
            return [dict({gid: self.cities[gid]})
                for gid in self.cities_by_name[name]]
        return []

    def _load_cities_data(self):
            self.cities = self._load_data(self.cities, 'cities.json')
            self.cities_by_name = self._load_data(self.cities_by_name, 'cities_by_name.json')

    def _load_admin_level_1_data(self):
            self.admin_level_1 = self._load_data(self.admin_level_1, 'admin_level_1.json')
            self.admin_level_1_by_name = self._load_data(self.admin_level_1_by_name, 'admin_level_1_by_name.json')

    def _load_admin_level_2_data(self):
            self.admin_level_2 = self._load_data(self.admin_level_2, 'admin_level_2.json')
            self.admin_level_2_by_name = self._load_data(self.admin_level_2_by_name, 'admin_level_2_by_name.json')


    def _load_data(self, datadict, datafile):
        if datadict is None:
            with open(os.path.join(self.datadir, datafile), 'r') as f:
                datadict = json.load(f)
        return datadict
