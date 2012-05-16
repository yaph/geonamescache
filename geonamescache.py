import geonamesdata

class GeonamesCache:
    def get_continents(self):
        return geonamesdata.continents

if __name__ == '__main__':
    print GeonamesCache().get_continents()
