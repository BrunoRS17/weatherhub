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


#Clima de uma localização
class Weather(BaseModel):
    temperature_2m: float
    relative_humidity_2m: float
    apparent_temperature: float
    wind_speed_10m: float


#Previsão dos próximos dias
class DailyForecast(BaseModel):
    time: list[str]
    temperature_2m_max: list[float]
    temperature_2m_min: list[float]
    wind_speed_10m_max: list[float]
    precipitation_sum: list[float]
    precipitation_probability_max: list[float]
