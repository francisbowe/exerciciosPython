import json

# Criando um dicionario
dict_guido = {
    "nome": "Guido van Rossum",
    "linguagem": "Python",
    "similar": ["c", "Modula-3", "lisp"],
    "users": 1000000
}

# Transformando o dicionario em um JSON
json_guido = json.dumps(dict_guido)
#criando um arquivo json
with open('guido.json', 'w') as file:
    file.write(json.dumps(json_guido))

# Lendo o arquivo JSON
with open('guido.json', 'r') as file:
    text = file.read()
    data = json.loads(text)
    print(data)