import requests
class RequestsApiRestCountriesService:
    def __init__(self,url):
        self.__url=url
    def get(self):
        r=requests.get(self.__url)
        toJson=r.json()
        return toJson