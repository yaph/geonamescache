import re
from unidecode import unidecode


class ResolutionTypes(object):

    COUNTRY = 'COUNTRY'
    ADMIN_1 = 'ADMIN_LEVEL_1'
    ADMIN_2 = 'ADMIN_LEVEL_2'
    CITY = 'CITY'


def standardize_loc_name(name):
    if name is None:
        return
    if not isinstance(name, unicode):
        name = unicode(name, 'utf8')
    return unidecode(name).title()


def get_alt_punc_names(name):
    return [
        name.replace("'", ""),
        name.replace("-", " "),
        re.sub(r'^St ', 'St. ', name, flags=re.IGNORECASE),
        re.sub(r'^Saint ', 'St. ', name, flags=re.IGNORECASE),
        name.split('(')[0].strip(),
        name.split(',')[0].strip(),
    ]
