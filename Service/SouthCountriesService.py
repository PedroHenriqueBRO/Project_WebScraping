from WebScrapingCountries.Repository.RepositorySouthCountries import RepositorySouthCountries
from WebScrapingCountries.Service.RequestsApiRestCountriesService import RequestsApiRestCountriesService
from WebScrapingCountries.Service.URLS.geturls import countriesSouthAmerica
class SouthCountriesService:
    def __init__(self):
        self.repo=RepositorySouthCountries()
        self.serviceApiRest=RequestsApiRestCountriesService(countriesSouthAmerica)
    def post(self):
        dados=self.serviceApiRest.get()
        for country in dados:
            nome=country['name']['common']
            area=country['area']
            populacao=country['population']
            self.repo.insert(nome,area, populacao)
    def get(self):
        print(self.repo.getall())
