#Marcin Grzyb Zadanie2
import numpy

A = numpy.matrix([
    [1, 7, 3],
    [1/7, 1, 2],
    [1/3, 1/2, 1]
])
B = numpy.matrix([
    [1, 1/5, 7, 1],
    [5, 1, 1/2, 2],
    [1/7, 2, 1, 3],
    [1, 1/2, 1/3, 1]
])
C = numpy.matrix([
    [1, 2, 5, 1, 7],
    [1/2, 1, 3, 1/2, 5],
    [1/5, 1/3, 1, 1/5, 2],
    [1, 2, 5, 1, 7],
    [1/7, 1/5, 1/2, 1/7, 1]
])


def ranking(matrix):
    vec=numpy.zeros((numpy.size(matrix,1),1))
    for i in range(numpy.size(matrix,1)):
        item=1;
        for j in range(numpy.size(matrix,1)):
            item*=matrix.item(i,j)
        vec[i]=item**(1/numpy.size(matrix,1))
    return vec/vec.sum()
        
def saaty(matrix):
    w, v = numpy.linalg.eig(matrix)
    lambdaMax = numpy.max(w)
    n = (numpy.size(matrix,1))
    return (lambdaMax-n)/(n-1)

def geom(matrix):
    rankingloc=ranking(matrix)
    item=0
    for i in range(numpy.size(matrix,1)):
        for j in range(i+1,numpy.size(matrix,1)):
           item+=(numpy.log10(matrix.item(i,j)*(rankingloc.item(j)/rankingloc.item(i)))**2)
    return 2*item/((numpy.size(matrix,1)-1)*(numpy.size(matrix,1)-2))

def kocz(matrix):
    indx=[]
    for i in range(numpy.size(matrix,1)):
        for j in range(numpy.size(matrix,1)):
            for k in range(numpy.size(matrix,1)):
                indx.append(min(abs(1-(matrix.item(i,k)*matrix.item(k,j)/matrix.item(i,j))),1-(matrix.item(i,j)/(matrix.item(i,k)*matrix.item(k,j)))))
    return(max(indx))


print("Saaty")
print("A",saaty(A))
print("B",saaty(B))
print("C",saaty(C))

print("Geometryczny")
print("A",geom(A))
print("B",geom(B))
print("C",geom(C))

print("Koczkodaja")
print("A",kocz(A))
print("B",kocz(B))
print("C",kocz(C))
    
    