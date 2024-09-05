
from geopy.geocoders import Nominatim
from fucoes.funcoes_Json import ler_arquivo, gravar_arquivo

geolocator = Nominatim(user_agent="wazeyes")
dicionario=ler_arquivo("entrada.json")
lista=dicionario["endereco"]
endereco=lista[0] + "," + lista[1] + " " + lista[2] + " " + lista[3]
location = geolocator.geocode(endereco)
if location:
    saida = {"coordenadas": (location.latitude, location.longitude)}
    gravar_arquivo(saida, "saida.json")
    print("Coordenadas gravadas com sucesso.")
else:
    print(f"Não foi possível encontrar o endereço: {endereco}")