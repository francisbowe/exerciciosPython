#manipulando arquivo com Numpy
import os
import numpy as np
#matplotlib e uma biblioteca para criar graficos
import matplotlib.pyplot as plt

#carregando o arquivi

filename = os.path.join('economic-indicators.csv')
with open('economic-indicators.csv', 'r') as file:
	for _ in range(10):
		print(file.readline().strip())

#carregando um dataset para dentro de um array
arr1 = np.loadtxt(filename, delimiter= ',', usecols= (0,1,2,3), skiprows=1)
#print(arr1)

#carregando apenas duas variaveis (colunas) do arquivo
var1, var2 = np.loadtxt(filename, delimiter=',', usecols=(3,1), skiprows=1, unpack=True)
#criando grafico para facilitar enteder a relacao  entre duas variaveis
plt.plot(var1, var2, 'o', markersize= 6, color='blue')
plt.show()