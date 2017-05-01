from unidecode import unidecode


class ResolutionTypes(object):

    OTHER = 'OTHER'
    COUNTRY = 'COUNTRY'
    ADMIN_1 = 'ADMIN_1'
    ADMIN_2 = 'ADMIN_2'
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
        name.split('(')[0].strip(),
    ]
