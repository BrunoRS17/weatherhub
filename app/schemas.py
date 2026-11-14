# from typing import TypedDict
from pydantic import BaseModel


#Localização de uma cidade 
class Location(BaseModel):
    name: str
    latitude: float
    longitude: float
    country: str


# #Retorno da API
class GeoCondingResponse(BaseModel):
    results: list[Location]
