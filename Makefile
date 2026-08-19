.PHONY: clean

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-datasets - remove all downloaded files in datasets/"
	@echo "clean-dev - remove test and coverage artifacts"
	@echo "clean-py - remove Python file artifacts"


dl:
	./bin/download_data.py

json:
	mkdir -p geonamescache/data/
	./bin/admin1.py
	./bin/admin2.py
	./bin/continents.py
	./bin/countries.py
	./bin/cities.py
	./bin/us_counties.py
	./bin/us_states.py
	./bin/timezones.py
	./bin/compress_data.py

clean: clean-build clean-py clean-dev clean-datasets

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

clean-dev:
	rm -f .coverage
	rm -fr .mypy_cache/
	rm -fr .pytest_cache/
	rm -fr .ruff_cache/
	rm -fr htmlcov/