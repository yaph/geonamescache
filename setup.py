# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from geonamescache import __version__

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='geonamescache',
    version=__version__,
    description='Geonames data for continents, cities and US states.',
    long_description=readme,
    author='Ramiro Gómez',
    author_email='www@ramiro.org',
    url='https://github.com/yaph/geonamescache',
    license=license,
    packages=find_packages(exclude=('tests', 'data', 'scripts'))
)
