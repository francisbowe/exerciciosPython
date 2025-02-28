import json
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]
print("Titulo: " ,data['title'])
print("URL: ", data['url'])
print("Duração: ", data['duration'])
print("Numero de visualizações: ", data['stats_number_of_plays'])
