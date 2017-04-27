.PHONY: clean docs

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "dist - package"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "docs-release - generate and upload docs to PyPI"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "release - package and upload a release"


data/cities1000.zip:
	curl -o data/cities1000.zip http://download.geonames.org/export/dump/cities1000.zip

data/countryInfo.txt:
	curl -o data/countryInfo.txt http://download.geonames.org/export/dump/countryInfo.txt

data/admin1CodesASCII.txt:
	curl -o data/admin1CodesASCII.txt http://download.geonames.org/export/dump/admin1CodesASCII.txt

data/admin2Codes.txt:
	curl -o data/admin2Codes.txt http://download.geonames.org/export/dump/admin2Codes.txt

data/us_counties.txt:
	curl -o data/us_counties.txt https://www2.census.gov/geo/docs/reference/codes/files/national_county.txt

data/cities1000.txt: data/cities1000.zip
	unzip data/cities1000.zip -d data

dl: data/cities1000.txt data/countryInfo.txt data/admin1CodesASCII.txt data/us_counties.txt data/admin2Codes.txt

tojson:
	#'./scripts/continents.py'
	'./scripts/countries.py'
	'./scripts/admin_level_1.py'
	'./scripts/admin_level_2.py'
	'./scripts/cities.py'
	'./scripts/us_counties.py'

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel

docs:
	rm -f docs/geonamescache.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ geonamescache
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	firefox docs/_build/html/index.html

docs-release: docs
	python setup.py upload_docs

install: clean
	pip install -r dev_requirements.txt --use-mirrors
	python setup.py install

release: clean
	python setup.py sdist upload
	python setup.py bdist_wheel upload

test:
	python setup.py test

test-all:
	tox
