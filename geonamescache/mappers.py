from collections.abc import Callable
from typing import Any, Literal, overload

from geonamescache import GeonamesCache, mappings
from geonamescache.types import ContinentCode, CountryFields, CountryNumericFields, CountryStringFields


@overload
def country(from_key: str = "name", *, to_key: CountryNumericFields) -> Callable[[str], int]: ...


@overload
def country(from_key: str = "name", to_key: CountryStringFields = "iso") -> Callable[[str], str]: ...


@overload
def country(from_key: str = "name", *, to_key: Literal["continentcode"]) -> Callable[[str], ContinentCode]: ...


def country(from_key: str = "name", to_key: CountryFields = "iso") -> Callable[[str], Any]:
    """Creates and returns a mapper function to access country data.

    The mapper function that is returned must be called with one argument. In
    the default case you call it with a name and it returns a 3-letter
    ISO_3166-1 code, e. g. called with ``Spain`` it would return ``ESP``.

    :param from_key: (optional) the country attribute you give as input.
        Defaults to ``name``.
    :param to_key: (optional) the country attribute you want as output.
        Defaults to ``iso``.
    :return: mapper
    :rtype: function
    """

    gc = GeonamesCache()
    dataset = gc.get_dataset_by_key(gc.get_countries(), from_key)

    def mapper(value: str) -> Any:
        # For country names take the mappings into account.
        if from_key == "name":
            value = mappings.country_names.get(value, value)
        # If there is a record return the corresponding attribute value.
        item = dataset.get(value)
        if item:
            return item[to_key]
        return None

    return mapper
