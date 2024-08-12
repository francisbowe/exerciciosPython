
with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão facil criar um arquivo...")

with open("teste.txt", "a") as arquivo:
    arquivo.write("\nNovo conteúdo...")