from WebScrapingCountries.Service.EuropeCountriesService import EuropeCountriesService
from WebScrapingCountries.Service.SouthCountriesService import SouthCountriesService

servsc = None
serveu = None

try:
    servsc = SouthCountriesService()
    servsc.repo.createtable()
    serveu = EuropeCountriesService()
    serveu.repo.createtable()
    serveu.post()
    servsc.post()
    servsc.get()
    serveu.get()
except Exception as a:
    print(f"Erro: {a}")
finally:
    if servsc is not None:
        servsc.repo.close()
    if serveu is not None:
        serveu.repo.close()
