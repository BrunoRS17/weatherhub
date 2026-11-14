import requests
from schemas import GeoCondingResponse, Location

def getLocation(city: str) -> Location:
    url = "https://geocoding-api.open-meteo.com/v1/search"
    headers = {"Accept": "application/json"}
    params = {"languagem": "pt", "count": 1, "name": city}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json() #Converte para dict

        return Location.model_validate(data["results"][0])


    except requests.exceptions.HTTPError as error_http:
        print(f"Erro na API: {error_http}")

    except requests.exceptions.RequestException as erro_conexao:
        print(f"Falha de rede ou tempo esgotado: {erro_conexao}")



