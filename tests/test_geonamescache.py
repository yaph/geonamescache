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
        cdata = (('AF', 'Africa'), ('AN', 'Antarctica'), ('AS', 'Asia'),
                 ('EU', 'Europe'), ('NA', 'North America'), ('OC', 'Oceania'),
                 ('SA', 'South America'))
        for cc, name in cdata:
            self.assertIn(cc, continents)
            self.assertEqual(name, continents[cc]['name'])

        self.assertNotIn('XX', continents)
        self.assertNotIn('OO', continents)


    def test_get_countries(self):
        countries = self.geonamescache.get_countries()

        self.assertIn('ES', countries)
        self.assertEqual('Spain', countries['ES']['name'])

        self.assertIn('FR', countries)
        self.assertEqual('France', countries['FR']['name'])

        self.assertNotIn('XX', countries)
        self.assertNotIn('OO', countries)


    def test_us_states(self):
        us_states = self.geonamescache.get_us_states()

        self.assertIn('NM', us_states)
        self.assertEqual('New Mexico', us_states['NM']['name'])

        self.assertIn('CA', us_states)
        self.assertEqual('California', us_states['CA']['name'])

        self.assertNotIn('XX', us_states)
        self.assertNotIn('OO', us_states)


if __name__ == '__main__':
    unittest.main()

