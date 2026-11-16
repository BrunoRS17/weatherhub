from client_openMateo import getLocation, getWeather, getDailyForecast
from utils import askCity


#Buscar cidade
def searchCity():
    city = askCity()
    city_found = getLocation(city)

    if (not city_found):
        print(f"\nCidade {city} não foi encontrada - tente novamente")
        
    else:
        #Exibindo dados da cidade
        print(f"\n{city_found.name} - {city_found.country}")
        print(f"Latitude: {city_found.latitude}°")
        print(f"Longitude: {city_found.longitude}°")





#Consultar clima atual
def consultWeather():
    city = askCity()
    weather = getWeather(city)

    if (not weather):
        print(f"\nClima da cidade {city} não encontrado")


    else:
        print(f"\n{city} - Clima Atual")
        print(f"Temperatura: {weather.temperature_2m} °C")
        print(f"Sensação Térmica: {weather.apparent_temperature} °C")
        print(f"Umidade: {weather.relative_humidity_2m}%")
        print(f"Velocidade do Vento: {weather.wind_speed_10m} km/h")



def dailyForecast():
    city = askCity()
    daily = getDailyForecast(city)

    if not daily:
        print(f"Previsão do tempo para a cidade {city} não encontrada")

    else:
        print(f"\n{city} - Próximos 7 dias")
        for i in range(len(daily.time)):
            print(f"\n{daily.time[i]}")
            print(f"Temperatura Máxima: {daily.temperature_2m_max[i]} °C")
            print(f"Temperatura Miníma: {daily.temperature_2m_min[i]} °C")
            print(f"Precipitação Acumulada: {daily.precipitation_sum[i]}mm")
            print(f"Probabilidade de Precipitação: {daily.precipitation_probability_max[i]}%")
            print(f"Velocidade Máxima de Vento: {daily.wind_speed_10m_max[i]} km/h")




#Início do projeto
def menu():
    print("\n===WeatherHub===")
    print("1. Buscar Cidade")
    print("2. Consultar clima atual")
    print("3. Previsão dos próximos 7 dias")
    print("0. Sair")
    option = input()

    #Tenta realizar a conversão para um número inteiro
    try:
        option = int(option)

    except ValueError:
        print ("O valor informado deve ser um número inteiro - tente novamente\n")
        menu()


    print("\n")
    match option:
        case 1:
            searchCity()
            menu()
        case 2:
            consultWeather()
            menu()
        case 3:
            dailyForecast()
            menu()
        case 0:
            print("Até mais...\n")
            exit()

        case _:
            print("Opção inválida")
            menu()




def main():
    menu()

main()