import socket
resp = "S"
while (resp=="S"):
    url = input ("Digite URL: ")
    ip =socket.gethostbyname(url) # Função que recupera o IP do site
    print (f"O IP do site {url} é: {ip}")
    resp = input ("Deseja continuar? [s/n]").upper() 