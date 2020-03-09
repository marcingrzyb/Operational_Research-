import numpy
cena=numpy.array([[1,1/2,2],[2,1,3],[1/2,1/3,1]])
paliwo=numpy.array([[1,3,1/5],[1/3,1,1/7],[5,7,1]])
bezpieczenstwo=numpy.array([[1,3,1/3],[1/3,1,1/5],[3,5,1]])
bagaz=numpy.array([[1,5,3],[1/5,1,1/2],[1/3,2,1]])
ilPas=numpy.array([[1,1,3],[1,1,3],[1/3,1/3,1]])

C=numpy.array([[1,1/2,2],[2,1,3],[1/2,1/3,1]])

koszt = numpy.matrix([[1,2],[1/2,1]])
pojemnosc = numpy.matrix([[1,1/3], [3,1]])

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
v2=eigen(normalize(paliwo))
v3=eigen(normalize(bezpieczenstwo))
v4=eigen(normalize(bagaz))
v5=eigen(normalize(ilPas))

v6=eigen(normalize(koszt))
v7=eigen(normalize(pojemnosc))

vC=eigen(normalize(C))

kosztFinal=v1*v6[0]+v2*v6[1]

pojemnoscFinal=v4*v7[0]+v5*v7[1]




print("wektory własne")
print(v1,v2,v3,v4,v5,v6,v7,vC)

result=numpy.concatenate([kosztFinal,v3,pojemnoscFinal]).reshape(3,3).transpose().dot(vC)
print("wynik")
print(result)