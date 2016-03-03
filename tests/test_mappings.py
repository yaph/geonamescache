# -*- coding: utf-8 -*-
import unittest
from geonamescache import mappings


class MappingsTestSuite(unittest.TestCase):
    """GeonamesCache Mappings test cases."""

    # Test a few mappings to make sure mappings work.
    def test_mappings(self):
        self.assertEquals(mappings.country_names['Macau'], 'Macao')
        self.assertEquals(mappings.country_names['Pitcairn Islands'], 'Pitcairn')
        self.assertEquals(mappings.country_names['Saint Barthélemy'], 'Saint Barthelemy')


if __name__ == '__main__':
    unittest.main()
