import geonamesdata

class GeonamesCache:

    def get_continents(self):
        return geonamesdata.continents

    def get_countries(self):
        return geonamesdata.countries

    def get_us_states(self):
        return geonamesdata.us_states

if __name__ == '__main__':
    print GeonamesCache().get_continents()
