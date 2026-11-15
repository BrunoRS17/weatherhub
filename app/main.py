from client_openMateo import getLocation, getWeather


#Buscar cidade
def searchCity():
    city = input("Digite o nome da cidade: ")
    city_found = getLocation(city)

    #Exibindo dados da cidade
    print(f"\n{city_found.name} - {city_found.country}")
    print(f"Latitude: {city_found.latitude}°")
    print(f"Longitude: {city_found.longitude}°")





#Consultar clima atual
def consultWeather():
    city = input("Digite o nome da cidade: ")
    weather = getWeather(city)

    print(f"\n{city} - Clima Atual")
    print(f"Temperatura: {weather.temperature_2m} °C")
    print(f"Sensação Térmica: {weather.apparent_temperature} °C")
    print(f"Umidade: {weather.relative_humidity_2m}%")
    print(f"Velocidade do Vento: {weather.wind_speed_10m} km/h")







#Início do projeto
def menu():
    print("\n===WeatherHub===")
    print("1. Buscar Cidade")
    print("2. Consultar clima atual")
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
        case 0:
            print("Até mais...\n")
            exit()

        case _:
            print("Opção inválida")
            menu()




def main():
    menu()

main()