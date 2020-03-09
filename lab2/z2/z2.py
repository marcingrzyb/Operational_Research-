import numpy
C = numpy.array([
[1,5,3,4],
[1/5,1,4,1],
[1/3,1/4,1,2],
[1/4,1,1/2,1]
])

cena=numpy.array([[1,1/2,2,4],[2,1,3,5],[1/2,1/3,1,2],[1/4,1/5,1/2,1]])
wyzywienie=numpy.array([[1,1,5,3],[1,1,5,3],[1/5,1/5,1,1/3],[1/3,1/3,3,1]])
parking=numpy.array([[1,1/3,1,1/3],[3,1,3,1],[1,1/3,1,1/3],[3,1,3,1]])
odleglosc=numpy.array([[1,3,1/5,1/7],[1/3,1,1/7,1/9],[5,7,1,1/3],[7,9,3,1]])

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


v1=eigen(normalize(cena))
v2=eigen(normalize(wyzywienie))
v3=eigen(normalize(parking))
v4=eigen(normalize(odleglosc))
vC=eigen(normalize(C))

print("wektory własne")
print(v1,v2,v3,v4,vC)
result=numpy.concatenate([v1,v2,v3,v4]).reshape(4,4).transpose().dot(vC)
print("wynik:")
print(result)