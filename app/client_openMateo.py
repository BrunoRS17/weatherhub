import requests
from schemas import GeoCondingResponse, Location, Weather


#Busca informações da cidade
def getLocation(city: str) -> Location:
    url = "https://geocoding-api.open-meteo.com/v1/search"
    headers = {"Accept": "application/json"}
    params = {"languagem": "pt", "count": 1, "name": city}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json() #Converte para dict

        return Location.model_validate(data.get("results")[0]) if data.get("results") else None


    except requests.exceptions.HTTPError as error_http:
        print(f"Erro na API: {error_http}")
        exit()

    except requests.exceptions.RequestException as erro_conexao:
        print(f"Falha de rede ou tempo esgotado: {erro_conexao}")
        exit()





#Busca informações de clima
def getWeather(city: str) -> Weather:

    location = getLocation(city)
    if (not location):
        return None

    url = "https://api.open-meteo.com/v1/forecast"
    headers = {"Accept": "application/json"}
    params = {
        "latitude": location.latitude,
        "longitude": location.longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m"
    }


    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return Weather.model_validate(data.get("current")) if data.get("current") else None
    
    
    except requests.exceptions.HTTPError as error_http:
        print(f"Erro na API: {error_http}")
        exit()

    except requests.exceptions.RequestException as erro_conexao:
        print(f"Falha de rede ou tempo esgotado: {erro_conexao}")
        exit()
