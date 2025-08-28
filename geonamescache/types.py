from typing import Literal

from typing_extensions import NotRequired, TypedDict

GeoNameIdStr = str
ISOStr = str
ContinentCode = Literal["AF", "AN", "AS", "EU", "NA", "OC", "SA"]
USStateCode = Literal[
    "AK",
    "AL",
    "AR",
    "AZ",
    "CA",
    "CO",
    "CT",
    "DC",
    "DE",
    "FL",
    "GA",
    "HI",
    "IA",
    "ID",
    "IL",
    "IN",
    "KS",
    "KY",
    "LA",
    "MA",
    "MD",
    "ME",
    "MI",
    "MN",
    "MO",
    "MS",
    "MT",
    "NC",
    "ND",
    "NE",
    "NH",
    "NJ",
    "NM",
    "NV",
    "NY",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VA",
    "VT",
    "WA",
    "WI",
    "WV",
    "WY",
]
USStateName = Literal[
    "Alaska",
    "Alabama",
    "Arkansas",
    "Arizona",
    "California",
    "Colorado",
    "Connecticut",
    "District of Columbia",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Iowa",
    "Idaho",
    "Illinois",
    "Indiana",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Massachusetts",
    "Maryland",
    "Maine",
    "Michigan",
    "Minnesota",
    "Missouri",
    "Mississippi",
    "Montana",
    "North Carolina",
    "North Dakota",
    "Nebraska",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "Nevada",
    "New York",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Virginia",
    "Vermont",
    "Washington",
    "Wisconsin",
    "West Virginia",
    "Wyoming",
]
CitySearchAttribute = Literal["alternatenames", "admin1code", "countrycode", "name", "timezone"]


class TimeZone(TypedDict):
    dstOffset: int
    gmtOffset: int
    timeZoneId: str


class BBox(TypedDict):
    accuracyLevel: int
    east: float
    north: float
    south: float
    west: float


class ContinentAlternateName(TypedDict):
    lang: str
    name: str
    isPreferredName: NotRequired[bool]
    isShortName: NotRequired[bool]
    isColloquial: NotRequired[bool]


class Continent(TypedDict):
    alternateNames: list[ContinentAlternateName]
    adminName1: str
    adminName2: str
    adminName3: str
    adminName4: str
    adminName5: str
    asciiName: str
    continentCode: ContinentCode
    fclName: str
    fcodeName: str
    astergdem: int
    bbox: BBox
    geonameId: int
    fcl: str
    fcode: str
    lat: str
    lng: str
    name: str
    population: int
    timezone: TimeZone
    toponymName: str
    srtm3: int
    wikipediaURL: str
    cc2: NotRequired[str]


class City(TypedDict):
    alternatenames: list[str]
    admin1code: str
    countrycode: str
    geonameid: int
    latitude: float
    longitude: float
    name: str
    population: int
    timezone: str


CountryNumericFields = Literal["areakm2", "isonumeric", "geonameid", "population"]
CountryStringFields = Literal[
    "capital",
    "currencycode",
    "currencyname",
    "iso",
    "iso3",
    "fips",
    "languages",
    "name",
    "neighbours",
    "phone",
    "postalcoderegex",
    "tld",
]
CountryFields = Literal[CountryNumericFields, CountryStringFields, "continentcode"]


class Country(TypedDict):
    areakm2: int
    capital: str
    continentcode: ContinentCode
    currencycode: str
    currencyname: str
    iso: str
    isonumeric: int
    iso3: str
    fips: str
    geonameid: int
    languages: str
    name: str
    neighbours: str
    phone: str
    population: int
    postalcoderegex: str
    tld: str


class USState(TypedDict):
    code: USStateCode
    fips: str
    geonameid: int
    name: USStateName


class USCounty(TypedDict):
    fips: str
    name: str
    state: USStateCode
