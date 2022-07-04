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
    long_description_content_type='text/markdown',
    author='Ramiro Gómez',
    author_email='code@ramiro.org',
    url='https://github.com/yaph/geonamescache',
    license='MIT',
    packages=find_packages(exclude=('tests', 'scripts')),
    package_data={'': ['data/*.json', 'LICENSE']},
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='tests',
    tests_require=['pytest'],
)