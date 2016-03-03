# -*- coding: utf-8 -*-
from fabric.api import env, lcd, local

env.use_ssh_config = True
CITIES = 'http://download.geonames.org/export/dump/cities15000.zip'
COUNTRIES = 'http://download.geonames.org/export/dump/countryInfo.txt'
# US counties URL points to a 404 page
US_COUNTIES = 'http://www.census.gov/geo/reference/codes/files/national_county.txt'


def git():
    local('git add . && git commit -a')
    local('git push')


def dl():
    local('mkdir -p data')
    local('curl %s -o data/cities15000.zip' % CITIES)
    local('curl %s -o data/countryInfo.txt' % COUNTRIES)
#    local('curl %s -o data/us_counties.txt' % US_COUNTIES)
    with lcd('data'):
        local('unzip cities15000.zip')


def tojson():
    with lcd('scripts'):
        local('./continents.py')
        local('./countries.py')
        local('./cities.py')
#        local('./us_counties.py')
