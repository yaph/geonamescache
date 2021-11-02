# -*- coding: utf-8 -*-
import unittest
from geonamescache import mappings
from geonamescache.mappers import country


class MappingsTestSuite(unittest.TestCase):
    """GeonamesCache Mappings test cases."""

    # Test a few mappings to make sure mappings work.
    def test_mappings(self):
        self.assertEqual(mappings.country_names['Macau'], 'Macao')
        self.assertEqual(mappings.country_names['Pitcairn Islands'], 'Pitcairn')
        self.assertEqual(mappings.country_names['Saint Barthélemy'], 'Saint Barthelemy')

    def test_country_name_iso3_mapper(self):
        mapper = country(from_key='name', to_key='iso3')
        self.assertEqual(mapper('Burma'), 'MMR')
        self.assertEqual(mapper('South Korea'), 'KOR')
        self.assertEqual(mapper('The Netherlands'), 'NLD')
        self.assertEqual(mapper('USA'), 'USA')


if __name__ == '__main__':
    unittest.main()
