# -*- coding: utf-8 -*-
import unittest

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from geonamescache import GeonamesCache


class GeonamesCacheTestSuite(unittest.TestCase):
    """GeonamesCache test cases."""

    def setUp(self):
        self.geonamescache = GeonamesCache()


    def test_continents(self):
        continents = self.geonamescache.get_continents()
        testdata = (('AF', 'Africa'), ('AN', 'Antarctica'), ('AS', 'Asia'),
                 ('EU', 'Europe'), ('NA', 'North America'), ('OC', 'Oceania'),
                 ('SA', 'South America'))
        for code, name in testdata:
            self.assertTrue(code in continents)
            self.assertEqual(name, continents[code]['name'])

        for code in ['XX', 'OO']:
            self.assertTrue(code not in continents)


    def test_get_countries(self):
        countries = self.geonamescache.get_countries()

        testdata = (('ES', 'Spain'), ('FR', 'France'), ('US', 'United States'))
        for code, name in testdata:
            self.assertTrue(code in countries)
            self.assertEqual(name, countries[code]['name'])

        for code in ['XX', 'OO']:
            self.assertTrue(code not in countries)


    def test_us_states(self):
        us_states = self.geonamescache.get_us_states()

        testdata = (('NM', 'New Mexico'), ('CA', 'California'), ('NV', 'Nevada'))
        for code, name in testdata:
            self.assertTrue(code in us_states)
            self.assertEqual(name, us_states[code]['name'])

        for code in ['XX', 'OO']:
            self.assertTrue(code not in us_states)


if __name__ == '__main__':
    unittest.main()

