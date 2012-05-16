# -*- coding: utf-8 -*-

"""
geonamescache
=============

:copyright: (c) 2012 by Ramiro Gómez.
:license: ISC, see LICENSE for more details.

"""

__title__ = 'geonamescache'
__version__ = '0.5'
__author__ = 'Ramiro Gómez'
__license__ = 'MIT'
__copyright__ = 'Copyright 2012 Ramiro Gómez'


from . import geonamesdata

class GeonamesCache:

    def get_continents(self):
        return geonamesdata.continents

    def get_countries(self):
        return geonamesdata.countries

    def get_us_states(self):
        return geonamesdata.us_states

