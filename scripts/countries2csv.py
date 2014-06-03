# -*- coding: utf-8 -*-
import pandas as pd
from geonamescache import GeonamesCache

gc = GeonamesCache()
countries = gc.get_countries()
df = pd.DataFrame.from_dict(countries, orient='index')
df.to_csv('../geonamescache/countries-by-iso.csv')