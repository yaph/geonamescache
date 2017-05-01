# -*- coding: utf-8 -*-
import re
import csv
import pdb
import requests
import sys
import traceback
from collections import defaultdict

from bs4 import BeautifulSoup
from bs4.element import NavigableString, CData, Comment

import osm_names

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

    names = set(name.split('(')[0].strip() for name in names)
    names.discard(unicode(search_term, 'utf8'))

    return {
        'concept' : page_name,
        'redirected_from' : redirected_from,
        'alt_names': [name.encode('utf8') for name in names],
    }

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
    locations_by_name, locations_by_id = osm_names.load_data()

    with open(out_filename, 'w') as out:
        for i, (name, locations_with_name) in enumerate(locations_by_name.iteritems()):
            if not locations_with_name:
                continue
            if i % 1000 == 0:
                print 'Search name', i

            most_important_loc = max(
                locations_with_name.itervalues(),
                key=lambda loc: loc['importance']
            )
            if name != most_important_loc['name']:
                # We will perform the search for this location only when we iterate across its
                # proper name.
                continue

            if most_important_loc['importance'] < .6 and any(
                loc['importance'] + .1 > most_important_loc['importance']
                for loc in locations_with_name.itervalues()
                if loc['country_code'] != most_important_loc['country_code']
            ):
                # Skip the search if we are not confident this name belongs to the most important
                # location
                continue

            result = search(name)
            if result is None:
                print 'Warning: could not fetch results for ', name
            if not result:
                continue

            found_names = result['alt_names']
            if not found_names:
                continue

            out.write('\t'.join([str(most_important_loc['id']), name] + found_names) + '\n')
            out.flush()

if __name__ == '__main__':
    try:
        run(sys.argv[1])
    except:
        type, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)
