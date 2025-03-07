import numpy as np

arr1 = np.array([10, 21, 32, 43, 48, 15, 76, 13])

print(arr1)
print(arr1[1:4])
indice = [1,0,5,3,6]
print(arr1[indice])
mask = (arr1 % 2==0)
print(arr1[mask])

#funcoes numpy, exite varios
arr2 = np.array([1,23,4,90,12,34,24])

print(np.arange(0,50,5))
print(np.shape(arr2))
print(np.size(arr2))
print(np.max(arr2))
print(np.min(arr2))
print(np.mean(arr2))

#criando uma matriz
arr2 = np.array([[1,2,3], [4,5,6]])
#criando lista de lista
lista = [[1,2,3], [4,5,6],[3,4,5]]
#funcao matrix cria uma matriz de uma lista de lista
matriz = np.matrix(lista)
print(matriz)
print(matriz.size)
print(matriz.shape)