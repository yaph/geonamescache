# -*- coding: utf-8 -*-
from fabric.api import env, lcd, local

env.use_ssh_config = True
CITIES = 'http://download.geonames.org/export/dump/cities15000.zip'
COUNTRIES = 'http://download.geonames.org/export/dump/countryInfo.txt'


def git():
    local('git add . && git commit -a')
    local('git push')


def dl():
    local('curl %s -o data/cities15000.zip' % CITIES)
    local('curl %s -o data/countryInfo.txt' % COUNTRIES)
    with lcd('data'):
        local('unzip cities15000.zip')


def tojson():
    with lcd('scripts'):
        local('./continents.py')
        local('./countries.py')
        local('./cities.py')


def up():
    dl()
    tojson()


def pypi():
    local('python setup.py sdist upload')