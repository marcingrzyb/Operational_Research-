from scipy.optimize import linprog
import numpy

A = [[1,2,-500],[1,1,-350],[-2,-1,600],[1,2,0],[-1,-2,0]]
b = [0,0,0,1,-1]
c = [3,4,0]
c=numpy.negative(c)

res = linprog(c, A, b,options = {"disp": True}).x
print(res)
 
x1 = res[0]/res[2]
print("A:", x1)
 
x2 = res[1]/res[2]
print("B:", x2)