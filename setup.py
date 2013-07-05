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
    author_email='code@ramiro.org',
    url='https://github.com/yaph/geonamescache',
    license=license,
    packages=find_packages(exclude=('tests', 'data', 'scripts')),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Topic :: Software Development :: Libraries :: Python Modules'
    )
)