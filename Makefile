.PHONY: clean

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-py - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "clean-data - remove all downloaded files in data/"

make_data:
	mkdir -p data

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
	curl -o data/us_counties.txt https://www2.census.gov/geo/docs/reference/codes2020/national_county2020.txt

dl: make_data data/cities500.txt data/cities1000.txt data/cities5000.txt data/cities15000.txt data/countryInfo.txt data/us_counties.txt

json:
	'./bin/continents.py'
	'./bin/countries.py'
	'./bin/cities.py'
	'./bin/us_counties.py'
	mv data/*.json geonamescache/data/

clean: clean-build clean-py clean-test clean-data

clean-data:
	rm -fr data/

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr *.egg-info/

clean-py:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -fr .mypy_cache/
	rm -fr .pytest_cache/
	rm -fr htmlcov/
