#apresentando total de voos internacionais

with  open ("economic-indicators.csv", "r") as boston:
    total_voos = 0
    maior = 0
    total_passageiros = 0
    maior_media_diaria = 0
    ano_usuario = input("Qual ano deseja pesquisar")
    for line in boston.readlines()[1:-1 ]:
        lista = line.split (",")
        total_voos = total_voos + float(lista[3])
        if float(lista[2])>float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]
        if ano_usuario == lista [0]:
            total_passageiros = total_passageiros + float(lista[2])
            if float(lista[5])>float(maior_media_diaria):
                maior_media_diaria = lista[5]
                mes_media_diaria = lista[1]
    print ("O total de voos internacionais: %d" % total_voos)
    print ("O ano com mais voos internacionais: %s/%s com %s voos" % (ano, mes, maior))
    print ("O total de passageiros no ano %s : %d" % (ano_usuario,total_passageiros))
    print ("A mes com a maior media diária de passageiros: %s/%s com %s passageiros" % (mes_media_diaria, ano_usuario, maior_media_diaria))