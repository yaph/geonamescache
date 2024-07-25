#!/usr/bin/env python
import pandas as pd

from geonamescache import GeonamesCache

gc = GeonamesCache()
countries = gc.get_countries()
df = pd.DataFrame.from_dict(countries, orient='index')
df.to_csv('data/countries.csv', index=False)
