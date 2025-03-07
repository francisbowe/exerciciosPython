#Maninupnado objectos de 3 e 4 dimensoes com numpy
import numpy as np

#3D array
arr3d = np.array([[[1,2,3],
                   [4,5,6]],
                  [[7,8,9],
                   [10,11,12]]])
print(arr3d)
print(arr3d.shape)
print(arr3d.ndim)
print(arr3d[0,1,1])

#4D array
arr4d = np.array([[[[1,2,3],
                    [4,5,6]],
                   [[7,8,9],
                    [10,11,12]]],
                  [[[13,14,15],
                    [16,17,18]],
                   [[19,20,21],
                    [22,23,24]]]])
print(arr4d)
print(arr4d.shape)
print(arr4d.ndim)
print(arr4d[1,0,1,2])
#