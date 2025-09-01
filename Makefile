.PHONY: clean

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-py - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "clean-datasets - remove all downloaded files in datasets/"


dl:
	./bin/download_data.py

json:
	./bin/continents.py
	./bin/countries.py
	./bin/cities.py
	./bin/us_counties.py
	mv datasets/*.json geonamescache/data/

clean: clean-build clean-py clean-test clean-datasets

clean-datasets:
	rm -fr datasets/

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
