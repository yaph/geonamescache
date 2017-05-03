# -*- coding: utf-8 -*-
import re
import csv
import json
import pdb
import requests
import sys
import traceback
from collections import defaultdict

from bs4 import BeautifulSoup
from bs4.element import NavigableString, CData, Comment

import utils
import geonames

def text_attrs(base):
    """Yield `(text, attr)` pairs for all descendants of `base`."""
    def _text_attrs(obj, attrs):
        if type(obj) in (NavigableString, CData, Comment):
            yield (obj, dict(attrs))
        else:
            attrs = attrs.copy()
            for k, attr in obj.attrs.iteritems():
                attrs[k].append(attr)

            for child in obj.children:
                for child_obj in _text_attrs(child, attrs):
                    yield child_obj

    return _text_attrs(base, defaultdict(list))


def css_style(raw_style):
    """Return a dictionary of CSS `(property, value)` pairs from (potentially multiple)
    "property:value; property:value" CSS styling strings."""
    if isinstance(raw_style, basestring):
        raw_style = [raw_style]

    concatenated_style = u';'.join(raw_style)
    property_values = filter(bool, map(unicode.strip,
                                       concatenated_style.split(';')))

    return dict(pv.split(':') for pv in property_values)

def _get_wikipedia(search_term):
    """If the `search_term` is *not* present in the cache, crawl Wikipedia and return a non-empty
    dictionary on success, an empty dictionary if no entry is found, and `None` if a `requests`
    error occurs. (The distinction between "not found" and a `requests` exception is made so that
    the former can be cached while excluding the latter.)"""

    url = 'https://en.wikipedia.org/wiki/%s' % search_term.replace(' ', '_')
    headers = {'User-agent': 'Mozilla/5.0'}

    try:
        req = requests.get(url, headers=headers, timeout=10)
    except requests.RequestException, e:
        # `requests` exceptions are handled externally so that the result is not cached.
        return None

    soup = BeautifulSoup(req.text, 'lxml')

    first_heading = soup('h1', {'id' : 'firstHeading'})
    if not first_heading:
        return {}

    page_name = first_heading[0].get_text()
    if page_name == 'Search results':
        return {}

    mw_content_text = soup('div', {'id' : 'mw-content-text'})
    if not mw_content_text:
        return {}

    paragraphs_text = []
    for paragraph in mw_content_text[0]('p', recursive=False):
        # Don't include any `text` in `paragraph` which has 'font-size' in the CSS styling or is set
        # to 'display: none'.
        paragraph_text = []
        for text, attrs in text_attrs(paragraph):
            style = css_style(attrs.get('style', []))
            if 'font-size' in style or style.get('display', '') == 'none':
                continue

            paragraph_text.append(text)

        # Don't include empty paragraphs.
        paragraph_text = ''.join(paragraph_text)
        if not paragraph_text:
            continue

        paragraphs_text.append(paragraph_text)

    if not paragraphs_text:
        return {}

    first_paragraph = paragraphs_text[0]
    if not first_paragraph or re.findall(r'refer[s]? to:', first_paragraph):
        return {}

    redirected_from = soup('span', **{'class' : 'mw-redirectedfrom'})
    if redirected_from:
        redirected_from = redirected_from[0].a['title']
    else:
        redirected_from = None

    names = [page_name]
    disambig_links = [a for a in soup.select('.hatnote .mw-disambig') if a.name == 'a']
    names.extend([link.text for link in disambig_links])

    for element in soup.select('.hatnote'):
        redirects_here_match = re.match(r'"(.*)" redirects here', element.text)
        if redirects_here_match:
            names.append(redirects_here_match.groups()[0])

    names = set(fix_name(name) for name in names)
    names.discard(utils.standardize_loc_name(search_term))

    return {
        'concept' : page_name,
        'redirected_from' : redirected_from,
        'alt_names': list(names),
    }

def fix_name(name):
    name = name.split('(')[0].strip()
    name = name.split(',')[0].strip()
    return utils.standardize_loc_name(name)

def search(query):
    result = _get_wikipedia(query)

    if not result:
        if ' ' in query:
            result = _get_wikipedia(query.replace(' ', '-'))

    if not result:
        if '(' in query:
            result = _get_wikipedia(query.split('(')[0].strip())

    return result

def check_alts():
    """
    Compare the results of this crawler with the earlier results from Leonard's older version.
    """
    missing_loc = 0
    missing_alt = 0
    extra_alt = 0
    count = 0

    with open('data/Alternative_City_Names.tsv') as f:
        reader = csv.reader(f, delimiter='\t')

        for row in reader:
            assert len(row) == 2
            name, alt_name = row
            if count % 100 == 0:
                print count, missing_loc, missing_alt, extra_alt

            alt_name = unicode(alt_name, 'utf8')
            result = search(name)
            if not result:
                print 'NO LOC FOUND!!!', name
                missing_loc += 1
                continue

            found_names = result['alt_names']
            if alt_name not in found_names:
                print 'Missing!!!!', name, alt_name, found_names
                missing_alt += 1
            if len(found_names) > 1:
                print 'Extra names', name, alt_name, found_names
                extra_alt += 1

            count += 1

def run(out_filename):
    """
    Find the alternate names of locations in the osm dataset and write them to the output file.
    """
    locations_by_name, locations_by_id = geonames.load_data()
    alt_names_found = {}
    ambig_locs = {}
    resolved_locs = {}
    misses = [0] * 4
    hits = 0

    for i, (name, locations_with_name) in enumerate(locations_by_name.iteritems()):
        if not locations_with_name:
            continue

        if (i + 1) % 100 == 0:
            print 'Search number', i
            print misses, hits
            # Write to file just in case job breaks
            with open(out_filename, 'w') as out:
                json.dump(alt_names_found, out)
            with open('ambig.txt', 'w') as out:
                for loc in sorted(ambig_locs.iteritems(), key=lambda pair: pair[1], reverse=True):
                    out.write(str(loc) + '\n')
            with open('resolved.txt', 'w') as out:
                for loc in sorted(
                    resolved_locs.iteritems(), key=lambda pair: pair[1][0], reverse=True
                ):
                    out.write(str(loc) + '\n')

        location = None
        if len(locations_with_name) == 1:
            location = locations_with_name.values()[0]
        else:
            locations_by_pop = sorted(
                locations_with_name.values(), key=lambda loc: loc.get('population', 0),
                reverse=True
            )
            top_population = locations_by_pop[0].get('population', 0)
            next_population = locations_by_pop[1].get('population', 0)
            if top_population > 10 ** 3 and top_population > 1 * next_population:
                location = locations_by_pop[0]
                resolved_locs[name] = (top_population, location['country'])

        if not location:
            ambig_locs[name] = max(
                loc.get('population', 0) for loc in locations_with_name.values()
            )
            misses[0] += 1
            continue

        result = search(name)
        if result is None:
            print 'Warning: could not fetch results for ', name
        if not result:
            misses[1] += 1
            continue

        found_names = result['alt_names']
        if not found_names:
            misses[2] += 1
            continue

        hits += 1
        alt_names_found[location['id']] = found_names

    with open(out_filename, 'w') as out:
        json.dump(alt_names_found, out)


if __name__ == '__main__':
    try:
        run(sys.argv[1])
    except:
        type, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)
