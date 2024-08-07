from typing import Dict

from geonamescache.types import USState, USStateCode

us_states: Dict[USStateCode, USState] = {
    'AK': {'code': 'AK', 'name': 'Alaska', 'fips': '02', 'geonameid': 5879092},
    'AL': {'code': 'AL', 'name': 'Alabama', 'fips': '01', 'geonameid': 4829764},
    'AR': {'code': 'AR', 'name': 'Arkansas', 'fips': '05', 'geonameid': 4099753},
    'AZ': {'code': 'AZ', 'name': 'Arizona', 'fips': '04', 'geonameid': 5551752},
    'CA': {'code': 'CA', 'name': 'California', 'fips': '06', 'geonameid': 5332921},
    'CO': {'code': 'CO', 'name': 'Colorado', 'fips': '08', 'geonameid': 5417618},
    'CT': {'code': 'CT', 'name': 'Connecticut', 'fips': '09', 'geonameid': 4831725},
    'DC': {'code': 'DC', 'name': 'District of Columbia', 'fips': '11', 'geonameid': 4138106},
    'DE': {'code': 'DE', 'name': 'Delaware', 'fips': '10', 'geonameid': 4142224},
    'FL': {'code': 'FL', 'name': 'Florida', 'fips': '12', 'geonameid': 4155751},
    'GA': {'code': 'GA', 'name': 'Georgia', 'fips': '13', 'geonameid': 4197000},
    'HI': {'code': 'HI', 'name': 'Hawaii', 'fips': '15', 'geonameid': 5855797},
    'IA': {'code': 'IA', 'name': 'Iowa', 'fips': '19', 'geonameid': 4862182},
    'ID': {'code': 'ID', 'name': 'Idaho', 'fips': '16', 'geonameid': 5596512},
    'IL': {'code': 'IL', 'name': 'Illinois', 'fips': '17', 'geonameid': 4896861},
    'IN': {'code': 'IN', 'name': 'Indiana', 'fips': '18', 'geonameid': 4921868},
    'KS': {'code': 'KS', 'name': 'Kansas', 'fips': '20', 'geonameid': 4273857},
    'KY': {'code': 'KY', 'name': 'Kentucky', 'fips': '21', 'geonameid': 6254925},
    'LA': {'code': 'LA', 'name': 'Louisiana', 'fips': '22', 'geonameid': 4331987},
    'MA': {'code': 'MA', 'name': 'Massachusetts', 'fips': '25', 'geonameid': 6254926},
    'MD': {'code': 'MD', 'name': 'Maryland', 'fips': '24', 'geonameid': 4361885},
    'ME': {'code': 'ME', 'name': 'Maine', 'fips': '23', 'geonameid': 4971068},
    'MI': {'code': 'MI', 'name': 'Michigan', 'fips': '26', 'geonameid': 5001836},
    'MN': {'code': 'MN', 'name': 'Minnesota', 'fips': '27', 'geonameid': 5037779},
    'MO': {'code': 'MO', 'name': 'Missouri', 'fips': '29', 'geonameid': 4398678},
    'MS': {'code': 'MS', 'name': 'Mississippi', 'fips': '28', 'geonameid': 4436296},
    'MT': {'code': 'MT', 'name': 'Montana', 'fips': '30', 'geonameid': 5667009},
    'NC': {'code': 'NC', 'name': 'North Carolina', 'fips': '37', 'geonameid': 4482348},
    'ND': {'code': 'ND', 'name': 'North Dakota', 'fips': '38', 'geonameid': 5690763},
    'NE': {'code': 'NE', 'name': 'Nebraska', 'fips': '31', 'geonameid': 5073708},
    'NH': {'code': 'NH', 'name': 'New Hampshire', 'fips': '33', 'geonameid': 5090174},
    'NJ': {'code': 'NJ', 'name': 'New Jersey', 'fips': '34', 'geonameid': 5101760},
    'NM': {'code': 'NM', 'name': 'New Mexico', 'fips': '35', 'geonameid': 5481136},
    'NV': {'code': 'NV', 'name': 'Nevada', 'fips': '32', 'geonameid': 5509151},
    'NY': {'code': 'NY', 'name': 'New York', 'fips': '36', 'geonameid': 5128638},
    'OH': {'code': 'OH', 'name': 'Ohio', 'fips': '39', 'geonameid': 5165418},
    'OK': {'code': 'OK', 'name': 'Oklahoma', 'fips': '40', 'geonameid': 4544379},
    'OR': {'code': 'OR', 'name': 'Oregon', 'fips': '41', 'geonameid': 5744337},
    'PA': {'code': 'PA', 'name': 'Pennsylvania', 'fips': '42', 'geonameid': 6254927},
    'RI': {'code': 'RI', 'name': 'Rhode Island', 'fips': '44', 'geonameid': 5224323},
    'SC': {'code': 'SC', 'name': 'South Carolina', 'fips': '45', 'geonameid': 4597040},
    'SD': {'code': 'SD', 'name': 'South Dakota', 'fips': '46', 'geonameid': 5769223},
    'TN': {'code': 'TN', 'name': 'Tennessee', 'fips': '47', 'geonameid': 4662168},
    'TX': {'code': 'TX', 'name': 'Texas', 'fips': '48', 'geonameid': 4736286},
    'UT': {'code': 'UT', 'name': 'Utah', 'fips': '49', 'geonameid': 5549030},
    'VA': {'code': 'VA', 'name': 'Virginia', 'fips': '51', 'geonameid': 6254928},
    'VT': {'code': 'VT', 'name': 'Vermont', 'fips': '50', 'geonameid': 5242283},
    'WA': {'code': 'WA', 'name': 'Washington', 'fips': '53', 'geonameid': 5815135},
    'WI': {'code': 'WI', 'name': 'Wisconsin', 'fips': '55', 'geonameid': 5279468},
    'WV': {'code': 'WV', 'name': 'West Virginia', 'fips': '54', 'geonameid': 4826850},
    'WY': {'code': 'WY', 'name': 'Wyoming', 'fips': '56', 'geonameid': 5843591}
}
