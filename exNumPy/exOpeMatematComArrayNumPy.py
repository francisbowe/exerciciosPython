#operacoes matematicas com Arrays NumPy
import numpy as np

#criando um array
arr1 = np.array([10, 21, 32, 43, 48, 15, 76, 13])
print(arr1)
#Soma de todos os elementos array
print(np.sum(arr1))
#Produto de todos os elementos array
print(np.prod(arr1))
#criando dois array
arr2 = np.array([1,2,3,4,5,6,7,8])
arr3 = np.array([2,47,0,14,35,6,7,18])
#Soma de dois arrays
arr4 =np.add(arr2, arr3)
print(arr4)
#criando duas matrizes
matriz1 = np.array([[1,2,3], [4,5,6]])
matriz2 = np.array([[7,8,9], [10,11,12], [13,14,15]])
print(np.shape(matriz1))
print(np.shape(matriz2))
#Multiplicacao de duas matrizes
matriz3 = np.dot(matriz1, matriz2)
print(matriz3)
print(np.shape(matriz3))