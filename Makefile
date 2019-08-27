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


data/cities15000.zip:
	curl -o data/cities15000.zip http://download.geonames.org/export/dump/cities15000.zip

data/countryInfo.txt:
	curl -o data/countryInfo.txt http://download.geonames.org/export/dump/countryInfo.txt

data/us_counties.txt:
	curl -o data/us_counties.txt https://www2.census.gov/geo/docs/reference/codes/files/national_county.txt

data/cities15000.txt: data/cities15000.zip
	unzip data/cities15000.zip -d data
	rm data/cities15000.zip

dl: data/cities15000.txt data/countryInfo.txt data/us_counties.txt

tojson:
	'./scripts/continents.py'
	'./scripts/countries.py'
	'./scripts/cities.py'
	'./scripts/us_counties.py'

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr *.egg-info/

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
	pip install -r requirements.txt --use-mirrors
	python setup.py install

# Call example: make release version=1.0.3
release: clean
	git tag -a $(version) -m 'Create version $(version)'
	git push --tags
	python setup.py sdist upload
	python setup.py bdist_wheel upload

test:
	python setup.py test

test-all:
	tox