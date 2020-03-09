#Marcin Grzyb Zadanie1
import numpy

matrix1 = numpy.matrix([[1, 1/7, 1/5], [7, 1, 3], [5, 1/3, 1]])
matrix2 = numpy.matrix([[1, 5, 9], [1/5, 1, 4], [1/9, 1/4, 1]])
matrix3 = numpy.matrix([[1, 4, 1/5], [1/4, 1, 1/9], [5, 9, 1]])
matrix4 = numpy.matrix([[1, 9, 4],[1/9, 1, 1/4], [1/4, 4, 1]])
matrix5 = numpy.matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
matrix6 = numpy.matrix([[1, 6, 4], [1/6, 1, 1/3], [1/4, 3, 1]])
matrix7 = numpy.matrix([[1,9,6], [1/9,1,1/3], [1/6,3,1]])
matrix8 = numpy.matrix([[1,1/2,1/2],[2,1,1],[2,1,1]])


matrixC = numpy.matrix([[1,4,7,5,8,6,6,2],
                        [1/4,1,5,3,7,6,6,1/3],
                        [1/7,1/5,1,1/3,5,3,3,1/5],
                        [1/5,1/3,3,1,6,3,4,1/2],
                        [1/8,1/7,1/5,1/6,1,1/3,1/4,1/7],
                        [1/6,1/6,1/3,1/3,3,1,1/2,1/5],
                        [1/6,1/6,1/3,1/4,4,2,1,1/5],
                        [1/2,3,5,2,7,5,5,1]])


def ranking(matrix):
    vec=numpy.zeros((numpy.size(matrix,1),1))
    for i in range(numpy.size(matrix,1)):
        item=1;
        for j in range(numpy.size(matrix,1)):
            item*=matrix.item(i,j)
        vec[i]=item**(1/numpy.size(matrix,1))
    return vec/vec.sum()
        
v1=ranking(matrix1)
v2=ranking(matrix2)
v3=ranking(matrix3)
v4=ranking(matrix4)
v5=ranking(matrix5)
v6=ranking(matrix6)
v7=ranking(matrix7)
v8=ranking(matrix8)
vC=ranking(matrixC)

R=numpy.concatenate([v1,v2,v3,v4,v5,v6,v7,v8]).reshape(8,3).transpose().dot(vC)
print("wynik")
print(R)
print("poprzednie wyniki")
print("[[ 0.35366345]\n[ 0.35900554]\n[ 0.28733101]]")