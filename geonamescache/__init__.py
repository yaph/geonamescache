__title__ = 'geonamescache'
__version__ = '3.0.0'
__author__ = 'Ramiro Gómez'
__license__ = 'MIT'


import json
import os
from collections.abc import Mapping
from typing import Any, ClassVar, TypeVar

from geonamescache.types import (
    City,
    CitySearchAttribute,
    Continent,
    ContinentCode,
    Country,
    GeoNameIdStr,
    ISOStr,
    USCounty,
    USState,
    USStateCode,
    USStateName,
)

TDict = TypeVar('TDict', bound=Mapping[str, Any])


class GeonamesCache:
    continents: dict[ContinentCode, Continent] | None = None
    countries: dict[ISOStr, Country] | None = None
    cities: dict[GeoNameIdStr, City] | None = None
    cities_items: list[tuple[GeoNameIdStr, City]] | None = None
    cities_by_names: ClassVar[dict[str, list[dict[GeoNameIdStr, City]]]] = {}
    us_counties: list[USCounty] | None = None
    us_states: dict[USStateCode, USState] | None = None

    def __init__(self, min_city_population: int = 15000):
        self.min_city_population = min_city_population

    def get_dataset_by_key(self, dataset: dict[Any, TDict], key: str) -> dict[Any, TDict]:
        return {d[key]: d for c, d in list(dataset.items())}

    def get_continents(self) -> dict[ContinentCode, Continent]:
        return self._load_data(self.continents, 'continents.json')

    def get_countries(self) -> dict[ISOStr, Country]:
        return self._load_data(self.countries, 'countries.json')

    def get_us_states(self) -> dict[USStateCode, USState]:
        return self._load_data(self.us_states, 'us_states.json')

    def get_countries_by_names(self) -> dict[str, Country]:
        return self.get_dataset_by_key(self.get_countries(), 'name')

    def get_us_states_by_names(self) -> dict[USStateName, USState]:
        return self.get_dataset_by_key(self.get_us_states(), 'name')

    def get_cities(self) -> dict[GeoNameIdStr, City]:
        """Get a dictionary of cities keyed by geonameid."""
        return self._load_data(self.cities, f'cities{self.min_city_population}.json')

    def get_cities_by_name(self, name: str) -> list[dict[GeoNameIdStr, City]]:
        """Get a list of city dictionaries with the given name.

        City names cannot be used as keys, as they are not unique.
        """

        if name not in self.cities_by_names:
            if self.cities_items is None:
                self.cities_items = list(self.get_cities().items())
            self.cities_by_names[name] = [{gid: city} for gid, city in self.cities_items if city['name'] == name]
        return self.cities_by_names[name]

    def get_us_counties(self):
        return self._load_data(self.us_counties, 'us_counties.json')

    def search_cities(
        self,
        query: str,
        attribute: CitySearchAttribute = 'alternatenames',
        *,
        case_sensitive: bool = False,
        contains_search: bool = True,
    ) -> list[City]:
        """Search all city records and return list of records, that match query for given attribute."""
        results = []
        query = (case_sensitive and query) or query.casefold()
        for record in self.get_cities().values():
            record_value = record[attribute]
            if contains_search:
                if isinstance(record_value, list):
                    if any(query in ((case_sensitive and value) or value.casefold()) for value in record_value):
                        results.append(record)
                elif query in ((case_sensitive and record_value) or record_value.casefold()):
                    results.append(record)
            elif isinstance(record_value, list):
                if case_sensitive:
                    if query in record_value:
                        results.append(record)
                elif any(query == value.casefold() for value in record_value):
                    results.append(record)
            elif query == ((case_sensitive and record_value) or record_value.casefold()):
                results.append(record)
        return results

    @staticmethod
    def _load_data(datadict: dict[Any, Any] | None, datafile: str) -> dict[Any, Any]:
        if datadict is None:
            with open(os.path.join(os.path.dirname(__file__), 'data', datafile)) as f:
                datadict = json.load(f)
        return datadict
