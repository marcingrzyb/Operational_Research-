import numpy
from scipy.optimize import linprog

def check(matrix,res,c):
    xs,ys=matrix.shape
    tmp=numpy.zeros(xs)
    tmp2=numpy.zeros(xs)
    for i in range(xs-1):
        for j in range(ys-1):
            tmp[i]+=res[j]*matrix[i][j]
    for i in range (len(tmp)):
        if(tmp[i]<c[i]):
            tmp2[i]=0
        else:
            tmp2[i]=1
    return(tmp2)

matrix=[
        [0.5,0.4,0.4,0.2],
        [0.4,0.2,0,0.5]]
c=[10,14,8,11]
b=[2000,2800]

matrix1=numpy.negative(matrix).T
b1=numpy.transpose(b)
c1=numpy.negative(c).T
res = linprog(b1, A_ub=matrix1, b_ub=c1,options={"disp": True}).x
print(res)
checked=check(matrix1,res,c1)
print('1=slabo spelnione nierownosci',checked)

indices = [i for i, x in enumerate(checked) if x == 0]
matrix=numpy.transpose(matrix)
matrixDEL=numpy.delete(matrix,indices,0)
matrixDEL=matrixDEL.T

print(numpy.linalg.lstsq(matrixDEL,numpy.transpose(b),rcond=None))