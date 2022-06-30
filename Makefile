.PHONY: clean

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "dist - package"
	@echo "test - run tests quickly with the default Python"
	@echo "release - package and upload a release"


data/cities500.txt:
	curl -o data/cities500.zip http://download.geonames.org/export/dump/cities500.zip
	unzip data/cities500.zip -d data
	rm data/cities500.zip

data/cities1000.txt:
	curl -o data/cities1000.zip http://download.geonames.org/export/dump/cities1000.zip
	unzip data/cities1000.zip -d data
	rm data/cities1000.zip

data/cities5000.txt:
	curl -o data/cities5000.zip http://download.geonames.org/export/dump/cities5000.zip
	unzip data/cities5000.zip -d data
	rm data/cities5000.zip

data/cities15000.txt:
	curl -o data/cities15000.zip http://download.geonames.org/export/dump/cities15000.zip
	unzip data/cities15000.zip -d data
	rm data/cities15000.zip


data/countryInfo.txt:
	curl -o data/countryInfo.txt http://download.geonames.org/export/dump/countryInfo.txt

data/us_counties.txt:
	curl -o data/us_counties.txt https://www2.census.gov/geo/docs/reference/codes/files/national_county.txt


dl: data/cities500.txt data/cities1000.txt data/cities5000.txt data/cities15000.txt data/countryInfo.txt data/us_counties.txt


tojson:
	'./scripts/continents.py'
	'./scripts/countries.py'
	'./scripts/cities.py'
	'./scripts/us_counties.py'


clean: clean-build clean-json clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr *.egg-info/

clean-json:
	rm -fr geonamescache/*.json

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -fr htmlcov/


dist: clean
	python setup.py sdist
	python setup.py bdist_wheel


install: clean
	pip install -r requirements.txt --use-mirrors
	python setup.py install


# Call example: make release version=1.3.0
release: test dist
	git tag -a $(version) -m 'Create version $(version)'
	git push --tags
	twine upload dist/*


test:
	coverage run --source geonamescache -m pytest
	coverage report