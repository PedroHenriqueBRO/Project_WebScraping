from WebScrapingCountries.Repository.RepositoryEuropeCountries import RepositoryEuropeCountries
from WebScrapingCountries.Service.RequestsApiRestCountriesService import RequestsApiRestCountriesService
from WebScrapingCountries.Service.URLS.geturls import countriesEurope
class EuropeCountriesService:
    def __init__(self):
        self.repo=RepositoryEuropeCountries()
        self.serviceApiRest=RequestsApiRestCountriesService(countriesEurope)
    def post(self):
        dados=self.serviceApiRest.get()
        for country in dados:
            nome=country['name']['common']
            area=country['area']
            populacao=country['population']
            self.repo.insert(nome,area, populacao)
    def get(self):
        print(self.repo.getall())
