__title__ = 'geonamescache'
__version__ = '3.0.2'
__author__ = 'Ramiro Gómez'
__license__ = 'MIT'


import gzip
import json
import os
from collections.abc import Mapping
from typing import Any, TypeVar

from geonamescache.types import (
    Admin1,
    Admin1CodeStr,
    Admin2,
    Admin2CodeStr,
    City,
    CitySearchAttribute,
    Continent,
    ContinentCode,
    Country,
    GeoNameIdStr,
    ISOStr,
    TimeZoneIdStr,
    TimeZoneInfo,
    USCounty,
    USState,
    USStateCode,
    USStateName,
)

TDict = TypeVar('TDict', bound=Mapping[str, Any])


class GeonamesCache:
    admin1: dict[Admin1CodeStr, Admin1] | None = None
    admin2: dict[Admin2CodeStr, Admin2] | None = None
    continents: dict[ContinentCode, Continent] | None = None
    countries: dict[ISOStr, Country] | None = None
    cities: dict[GeoNameIdStr, City] | None = None
    timezones: dict[TimeZoneIdStr, TimeZoneInfo] | None = None
    us_counties: list[USCounty] | None = None
    us_states: dict[USStateCode, USState] | None = None

    def __init__(self, min_city_population: int = 15000):
        self.min_city_population = min_city_population
        # Per instance, because it indexes one particular cities dataset.
        self.cities_by_names: dict[str, list[City]] | None = None

    def get_dataset_by_key(self, dataset: dict[Any, TDict], key: str) -> dict[Any, TDict]:
        return {d[key]: d for c, d in list(dataset.items())}

    def get_continents(self) -> dict[ContinentCode, Continent]:
        if self.continents is None:
            self.continents = self._load_data('continents')
        return self.continents

    def get_countries(self) -> dict[ISOStr, Country]:
        if self.countries is None:
            self.countries = self._load_data('countries')
        return self.countries

    def get_admin1_codes(self) -> dict[Admin1CodeStr, Admin1]:
        """Get first-level administrative divisions keyed by <countrycode>.<admin1code>, e. g. US.CA."""
        if self.admin1 is None:
            self.admin1 = self._load_data('admin1')
        return self.admin1

    def get_admin2_codes(self) -> dict[Admin2CodeStr, Admin2]:
        """Get second-level administrative divisions keyed by <countrycode>.<admin1code>.<admin2code>, e. g. NL.11.0599."""
        if self.admin2 is None:
            self.admin2 = self._load_data('admin2')
        return self.admin2

    def get_admin1_by_city(self, city: City) -> Admin1 | None:
        """Get the first-level administrative division a city belongs to, None if unresolvable.

        Not every city record has an admin1code, and not every code pair is
        present in the admin1 dataset, so callers should handle None.
        """
        if not city.get('countrycode') or not city.get('admin1code'):
            return None
        return self.get_admin1_codes().get(f"{city['countrycode']}.{city['admin1code']}")

    def get_admin2_by_city(self, city: City) -> Admin2 | None:
        """Get the second-level administrative division a city belongs to, None if unresolvable.

        Requires all three of countrycode, admin1code and admin2code, as the
        admin2 dataset is keyed by the concatenation of them.
        """
        if not city.get('countrycode') or not city.get('admin1code') or not city.get('admin2code'):
            return None
        return self.get_admin2_codes().get(f"{city['countrycode']}.{city['admin1code']}.{city['admin2code']}")

    def get_timezones(self) -> dict[TimeZoneIdStr, TimeZoneInfo]:
        """Get time zones keyed by IANA time zone id, e. g. Europe/Amsterdam."""
        if self.timezones is None:
            self.timezones = self._load_data('timezones')
        return self.timezones

    def get_timezones_by_country(self, countrycode: str) -> list[TimeZoneInfo]:
        """Get the time zones of a country as a list sorted by time zone id.

        Takes an ISO alpha-2 country code, case insensitive. Returns an empty
        list for unknown codes.
        """
        countrycode = countrycode.upper()
        return sorted(
            (tz for tz in self.get_timezones().values() if tz['countrycode'] == countrycode),
            key=lambda tz: tz['timezoneid'],
        )

    def get_us_states(self) -> dict[USStateCode, USState]:
        if self.us_states is None:
            self.us_states = self._load_data('us_states')
        return self.us_states

    def get_countries_by_names(self) -> dict[str, Country]:
        return self.get_dataset_by_key(self.get_countries(), 'name')

    def get_us_states_by_names(self) -> dict[USStateName, USState]:
        return self.get_dataset_by_key(self.get_us_states(), 'name')

    def get_cities(self) -> dict[GeoNameIdStr, City]:
        """Get a dictionary of cities keyed by geonameid."""
        if self.cities is None:
            self.cities = self._load_data(f'cities{self.min_city_population}')
        return self.cities

    def get_cities_by_names(self) -> dict[str, list[City]]:
        """Get city records grouped by name.

        City names are not unique, so each name maps to a list of records.
        """
        if self.cities_by_names is None:
            index: dict[str, list[City]] = {}
            for city in self.get_cities().values():
                index.setdefault(city['name'], []).append(city)
            self.cities_by_names = index
        return self.cities_by_names

    def get_cities_by_name(self, name: str) -> list[City]:
        """Get the city records with the given name, empty list if there are none.

        Builds an index of all city names on first call, so looking up many
        names costs one pass over the dataset rather than one pass per name.
        """
        return self.get_cities_by_names().get(name, [])

    def get_us_counties(self) -> list[USCounty]:
        if self.us_counties is None:
            self.us_counties = self._load_data('us_counties')
        return self.us_counties

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
    def _load_data(dataset: str) -> Any:
        """Read and parse a bundled dataset. Callers are responsible for caching."""
        path = os.path.join(os.path.dirname(__file__), 'data', dataset + '.json.gz')
        with gzip.open(path, 'rt', encoding='utf-8') as f:
            return json.load(f)
