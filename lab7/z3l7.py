from scipy.optimize import linprog
import numpy

#gracz1:1,gracz2:1 -> 2
#gracz1:1,gracz2:2->3
#gracz1:2,gracz2:1->3
#gracz1:2,gracz2:2->4

matrix=[
        [0,2,-3,0],
        [-2,0,0,3],
        [3,0,0,-4],
        [0,-3,4,0]
        ]
b = [-1, -1, -1, -1]
c = [1, 1, 1, 1]

absmin=abs(numpy.min(matrix))
matrix=matrix+absmin

matrix1=-matrix.T


res = linprog(c, matrix1, b,).x

f = sum(res)
V = 1 / f

print("A")
print("Wartosc gry =", V - absmin)
print("Prawdopodobienstwa",[V*x for x in res])




c = [-1*x for x in c]
b= [-1*x for x in b]


res = linprog(c, matrix, b).x
f = sum(res)
V = 1 / f

print("B")
print("Wartosc gry =", V - absmin)
print("Prawdopodobienstwa",[V*x for x in res])
