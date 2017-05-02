import re

from geonames import geonames
from osm_names import osm_names
from osm_names.utils import ResolutionTypes, standardize_loc_name


class LocationsSource(object):

    """
    Allows search for locations by name or id.
    
    Returns results of the form
    
    {
        id: {
            id: int,
            resolution: str,
            name: str,
            country: str,
            country_code: str,
            country_id: int,
            admin_level_1: Optional[str],
            admin1_level_1_id: Optional[int],   # can be 0 if admin1 is not present in data set
            admin_level_2: Optional[str],
            admin_level_2_id: Optional[int],   # can be 0 if admin2 is not present in data set
            city: Optional[str],
            importance: Optional[float],
            population: Optional[int],
            latitude: Optional[float],
            longitude: Optional[float],
        }
    }
    """

    def __init__(self, source='osm'):
        assert source in ('osm', 'geonames')
        if source == 'osm':
            self._locations_by_name, self._locations_by_id = osm_names.load_data()
        else:
            self._locations_by_name, self._locations_by_id = geonames.load_data()

    def city_search(self, city_name):
        city_name = re.sub(r'^N\.?Y\.?C\.?$', 'New York City', city_name, flags=re.IGNORECASE)
        city_name = re.sub(r'^City\s+Of\s+', '', city_name, flags=re.IGNORECASE)
        city_name = standardize_loc_name(city_name)

        return dict(
            (id_, loc.copy()) for id_, loc in self._locations_by_name[city_name].iteritems()
            if loc['resolution'] == ResolutionTypes.CITY
        )

    def admin_level_1_search(self, admin1_name):
        admin1_name = standardize_loc_name(admin1_name)
        return dict(
            (id_, loc.copy()) for id_, loc in self._locations_by_name[admin1_name].iteritems()
            if loc['resolution'] == ResolutionTypes.ADMIN_1
        )

    def _admin_level_2_search(self, admin2_name):
        admin2_name = standardize_loc_name(admin2_name)
        return dict(
            (id_, loc.copy()) for id_, loc in self._locations_by_name[admin2_name].iteritems()
            if loc['resolution'] == ResolutionTypes.ADMIN_2
        )

    def admin_level_2_search(self, admin2_name):
        locations = self._admin_level_2_search(admin2_name)
        locations.update(self._admin_level_2_search('%s County' % admin2_name))
        return locations

    US_RE = re.compile(r'^(u\.?s\.?a\.?|u\.s\.?)$', flags=re.IGNORECASE)
    BRITAIN_RE = re.compile(r'^(england|britain|u\.?k\.?)$', flags=re.IGNORECASE)

    def country_search(self, country_name):
        if LocationsSource.US_RE.search(country_name):
            country_name = u'United States'
        elif LocationsSource.BRITAIN_RE.search(country_name):
            country_name = u'United Kingdom'
        elif country_name == u'Holland':
            country_name = u'Netherlands'
        country_name = standardize_loc_name(country_name)

        return dict(
            (id_, loc.copy()) for id_, loc in self._locations_by_name[country_name].iteritems()
            if loc['resolution'] == ResolutionTypes.COUNTRY
        )

    def all_locations_search(self, name):
        matches = {}
        for lookup in (
            self.city_search, self.admin_level_1_search, self.admin_level_2_search,
            self.country_search,
        ):
            matches.update(lookup(name))
        return matches

    def get_location_by_id(self, id_):
        return self._locations_by_id[id_].copy()