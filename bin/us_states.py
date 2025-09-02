#!/usr/bin/env python
import json
import re
from pathlib import Path

import httpx
from bs4 import BeautifulSoup

GEONAME_ID_POS = 3


def extract_us_states_data():
    """
    Downloads HTML from GeoNames US administrative divisions page
    and extracts state information into a dictionary structure.
    """

    # Download the HTML content
    url = 'http://www.geonames.org/US/administrative-division-united-states.html'

    try:
        response = httpx.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        html_content = response.text
    except httpx.RequestError as e:
        print(f'Error downloading the page: {e}')
        return {}

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table with id 'subdivtable1'
    table = soup.find('table', id='subdivtable1')
    if not table:
        print("Table with id 'subdivtable1' not found")
        return {}

    # Dictionary to store the results
    states_data = {}

    # Find all table rows
    rows = table.find_all('tr')

    for row in rows:
        # Find span with id containing "isoSpan" for the state code
        iso_span = row.find('span', id=re.compile(r'.*isoSpan.*'))
        if iso_span and iso_span.get_text(strip=True):
            code = iso_span.get_text(strip=True)

            # Find span with id containing "fipsSpan" for FIPS code
            fips_span = row.find('span', id=re.compile(r'.*fipsSpan.*'))
            fips = fips_span.get_text(strip=True) if fips_span else ""

            # Find span with id containing "nameSpan" and get the link inside it
            name_span = row.find('span', id=re.compile(r'.*nameSpan.*'))
            if name_span:
                link = name_span.find('a')
                if link and link.get('href'):
                    href = link.get('href')
                    name = link.get_text(strip=True)

                    # Extract geoname ID from href (assuming format like "/path/path/ID/name")
                    href_parts = href.split('/')
                    if len(href_parts) > GEONAME_ID_POS:
                        try:
                            geoname_id = int(href_parts[GEONAME_ID_POS])

                            # Create the data structure matching the JavaScript output
                            states_data[code] = {
                                'code': code,
                                'name': name,
                                'fips': fips,
                                'geonameid': geoname_id
                            }

                        except (ValueError, IndexError):
                            # Skip if geoname ID extraction fails
                            continue

    return states_data


if __name__ == '__main__':
    states_data = extract_us_states_data()
    if states_data:
        print(f'Total states extracted: {len(states_data)}')
        Path('geonamescache/data/us_states.json').write_text(json.dumps(states_data))
    else:
        print('No data extracted. Please check the URL and HTML structure.')
