#!/usr/bin/env python
"""Gzip the built JSON files into the package data directory.

Storing the data gzipped cuts the installed size of the package by about a
factor of six without costing load time, as the saved I/O offsets the
decompression. Keeping this a separate step means the bin/ scripts stay
plain JSON writers.
"""
import gzip
import shutil
from pathlib import Path

p_src = Path('datasets')
p_dst = Path('geonamescache', 'data')
p_dst.mkdir(parents=True, exist_ok=True)

for p_json in sorted(p_src.glob('*.json')):
    p_gz = p_dst.joinpath(p_json.name + '.gz')
    # mtime=0 keeps the output byte identical for identical input, so rebuilds
    # don't churn the package data.
    with p_json.open('rb') as f_in, gzip.GzipFile(p_gz, 'wb', compresslevel=9, mtime=0) as f_out:
        shutil.copyfileobj(f_in, f_out)
    print(f'{p_json.name}: {p_json.stat().st_size / 1e6:.1f} MB -> {p_gz.stat().st_size / 1e6:.1f} MB')
    p_json.unlink()
