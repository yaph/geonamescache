# -*- coding: utf-8 -*-
import io
from setuptools import setup, find_packages
from geonamescache import __version__


# Use io.open to be able to set encoding to utf-8.
with io.open('README.rst', encoding='utf-8') as f:
    readme = f.read()


setup(
    name='geonamescache',
    version=__version__,
    description='Geonames data for continents, cities and US states.',
    long_description=readme,
    author='Ramiro Gómez',
    author_email='code@ramiro.org',
    url='https://github.com/yaph/geonamescache',
    license='MIT',
    packages=find_packages(exclude=('tests', 'data', 'scripts')),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='tests',
    tests_require=['tox'],
)