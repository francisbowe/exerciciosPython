from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes")

latitude = float(input("Digite a latitude..: "))
longitude = float(input("Digite a longitude.: "))

resultado = str(geolocator.reverse(f"{latitude}, {longitude}")).split(",")

if resultado[0]!= 'None':
    print ("Endereco completo..: ", resultado)
    print ("Dados 1............: ", resultado [0])
    print ("Dados 2............: ", resultado [1])
    print ("Dados 3............: ", resultado [2])