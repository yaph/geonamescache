# -*- coding: utf-8 -*-
from geonamescache import GeonamesCache
from . import mappings


def country(from_key='name', to_key='iso'):
    gc = GeonamesCache()
    dataset = gc.get_dataset_by_key(gc.get_countries(), from_key)

    def mapper(key):
        if 'name' == from_key and key in mappings.country_names:
            key = mappings.country_names[key]
        item = dataset.get(key)
        if item:
            return item[to_key]

    return mapper