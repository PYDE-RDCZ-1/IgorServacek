#A

import numpy as np

matrix1 = np.array([[1,2,3],
                    [4,5,6],
                    [6,7,8]])

matrix2 = np.array([[9,8,7],
                    [4,5,6],
                    [4,5,5]])

result = np.dot(matrix1, matrix2)
print(result)


# B
def determinant(matica):
    vysl = np.linalg.det(matica)
#    print(float(vysl))
    return vysl


def transponovanie(matice):
    vysl =  np.transpose(matice)
    return vysl


def nasobenie(matice1, matice2):
    vysl = np.dot(matice1, matice2)
    return vysl


determinant(matrix1)
print("determinanit:")
print(determinant(matrix1))
print("transpozicia:")
print(transponovanie((matrix1)))
print("násobenie")
print(nasobenie(matrix1, matrix2))