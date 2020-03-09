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

def normalize(matrix): #normalizacja macierzy
    matrixa=numpy.zeros(shape=(numpy.size(matrix,1),numpy.size(matrix,1)))
    for i in range(numpy.size(matrix,1)):
        colsum=numpy.sum(matrix[:,i])
        for j in range(numpy.size(matrix,1)):
            matrixa[j,i]=matrix.item((j,i))/colsum

    return matrixa

def eigen(matrix): #obliczanie wektora własnego(przyblizenie)
    vec=numpy.zeros((numpy.size(matrix,1),1))
    for i in range(numpy.size(matrix,1)):
        vec[i]=numpy.sum(matrix[i,:])/numpy.size(matrix,1)
    return vec

v1=eigen(normalize(matrix1))
v2=eigen(normalize(matrix2))
v3=eigen(normalize(matrix3))
v4=eigen(normalize(matrix4))
v5=eigen(normalize(matrix5))
v6=eigen(normalize(matrix6))
v7=eigen(normalize(matrix7))
v8=eigen(normalize(matrix8))
vC=eigen(normalize(matrixC))

print("wektory własne")
print(v1,v2,v3,v4,v5,v6,v7,v8,vC)

result=numpy.concatenate([v1,v2,v3,v4,v5,v6,v7,v8]).reshape(8,3).transpose().dot(vC)

print("wynik:")
print(result)