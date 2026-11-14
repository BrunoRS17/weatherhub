from client_openMateo import getLocation


#Buscar cidade
def searchCity():
    city = input("Digite o nome da cidade: ")
    city_found = getLocation(city)

    #Exibindo dados da cidade
    print(f"\n{city_found.name} - {city_found.country}")
    print(f"Latitude: {city_found.latitude}°")
    print(f"Longitude: {city_found.longitude}°")

    #Retorno para o menu
    print("\n")
    menu()


#Início do projeto
def menu():
    print("\n===WeatherHub===")
    print("1. Buscar Cidade")
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
        case 0:
            print("Até mais...\n")

        case _:
            print("Opção inválida")
            menu()




def main():
    menu()

main()