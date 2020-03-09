import numpy
from scipy.optimize import linprog
matrix=[
        [1,3,2,3,1],
        [4,6,5,7,1]]

c=[2,5,3,4,1]
b=[6,15]
matrix1=numpy.negative(matrix).T
b1=numpy.transpose(b)
c1=numpy.negative(c).T
res = linprog(b1, A_ub=matrix1, b_ub=c1).x
print(res)
