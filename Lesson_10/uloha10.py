# Úloha 10
#
import igy_modul as ig
print("Aritmetické operácie:")
print("9 + 25 = ", ig.add(9,25))
print("9 - 25 = ", ig.sub(9,25))
print("9 / 25 = ", ig.div(9,25))
print("9 * 25 = ", ig.mult(9,25))
print("*****************")
print("Výpis matíc")
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


B = [[0, -1, 0],
     [11, 55, 100],
     [25, 5, 1]]
print("matica A:", A)
print("matica B:", B)
print("Operácie s maticami:")
print(" A + B = ",ig.matrix_addition(A, B))
print(" A - B = ",ig.matrix_subtraction(A, B))
print(" A * B = ",ig.matrix_multiplication(A, B))

print("9 / 3 = ", ig.div(9, 3) )
print("9 / 0 = ", ig.div(9, 0) )
