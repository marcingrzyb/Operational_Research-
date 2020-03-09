from scipy.optimize import linprog
import numpy

matrix=[
        [-2,8,2],
        [3,-1,0]
        ]

absmin=abs(numpy.min(matrix))
matrix=matrix+absmin
matrix1=-matrix.T
b=[-1,-1,-1]
c=[1,1]

res = linprog(c, matrix1, b).x

f = sum(res)
V = 1 / f

print("A")
print("Wartosc gry =", V - absmin)
print("Prawdopodobienstwa",[V*x for x in res])

c,b=b,c
res = linprog(c, matrix, b).x

f = sum(res)
V = 1 / f

print("B")
print("Wartosc gry =", V - absmin)
print("Prawdopodobienstwa",[V*x for x in res])



