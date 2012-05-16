# -*- coding: utf-8 -*-
import csv

fcsv = open('../data/countryInfo.txt', 'rb')
reader = csv.reader(fcsv, 'excel-tab')
headers = reader.next()
for record in reader:
    (ISO, ISO3, ISONumeric, fips, Country, Capital, Area, Population, Continent, tld, CurrencyCode, CurrencyName, Phone, PostalCodeFormat, PostalCodeRegex, Languages, geonameid, neighbours, EquivalentFipsCode) = record
    if not geonameid:
        geonameid = None
    print "'%s': {'name': '%s', 'continent_code': '%s', 'geonameid': %s}," % (ISO, Country, Continent, geonameid)
    
