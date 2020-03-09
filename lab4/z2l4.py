#Marcin Grzyb
import numpy
A = numpy.array([[1, 2/3, 2,  5/2, 5/3, 5], 
                       [3/2, 1, 3, 10/3, 3, 9], 
                       [1/2, 1/3, 1, 4/3, 7/8, 5/2], 
                       [2/5, 3/10, 3/4, 1, 5/6, 12/5], 
                       [3/5, 1/3, 8/7, 6/5, 1, 3], 
                       [1/5, 1/9, 2/5, 5/12, 1/3, 1]])       

B = numpy.array([[1, 2/5, 3,  7/3, 1/2, 1], 
                       [5/2, 1, 4/7, 5/8, 1/3, 3], 
                       [1/3, 7/4, 1, 1/2, 2, 1/2], 
                       [3/7, 8/5, 2, 1, 4, 2], 
                       [2, 3, 1/2, 1/4, 1, 1/2], 
                       [1, 1/3, 2, 1/2, 2, 1]])       

C = numpy.array([[1, 17/4, 17/20, 8/5, 23/6, 8/3], 
                       [4/17, 1, 1/5, 2/5, 9/10, 2/3], 
                       [20/17, 5, 1, 21/10, 51/10, 10/3], 
                       [5/8, 5/2, 10/21, 1, 5/2, 11/6], 
                       [6/23, 10/9, 10/51, 2/5, 1, 19/30], 
                       [3/8, 3/2, 3/10, 6/11, 30/19, 1]])


def koczkodaj(matrix):
    indx=[]
    for i in range(numpy.size(matrix,1)):
        for j in range(numpy.size(matrix,1)):
            for k in range(numpy.size(matrix,1)):
                indx.append(min(abs(1-(matrix.item(i,k)*matrix.item(k,j)/matrix.item(i,j))),1-(matrix.item(i,j)/(matrix.item(i,k)*matrix.item(k,j)))))
    return(max(indx))

def checker(matrix,k,x_size):
    if(koczkodaj(matrix)<(1-((1+(4*(x_size-1)*(x_size-k-2))**(1/2))/(2*(x_size-1))))):
        return("wynik pewny:")
    else:
        return("wynik niepewny:")

def checkPos(matrix,positions):
    x_size, y_size = matrix.shape
    numknown=positions.size
    new=numpy.empty((numknown,y_size,))
    for i in range(numknown):
        new[i]=matrix[positions[i]]
    matrix=numpy.delete(matrix,positions,axis=0)
    tmp=numpy.concatenate((matrix,new), axis=0)
    new2=numpy.empty((y_size,numknown,))
    for i in range(numknown):
        new2[:,i]=tmp[:,positions[i]]
    tmp=numpy.delete(tmp,positions,axis=1)
    tmp=numpy.concatenate((tmp,new2),axis=1)
    return tmp

def geometric(matrix,knownVec,positions):
    numknown=knownVec.size
    x_size, y_size = matrix.shape
    print(checker(matrix,numknown,x_size))
    b=numpy.empty((y_size-numknown,1,))
    for i in range(y_size-numknown):
        b[i]=numpy.log10(numpy.prod(matrix[i,:])*numpy.prod(knownVec))
    a=numpy.empty((x_size-numknown,y_size-numknown))
    for i in range(x_size-numknown):
        for j in range(y_size-numknown):
            if(i==j):
                a[i][j]=x_size-1
            else:
                a[i][j]=-1
    solved=numpy.linalg.solve(a,b)
    Wsizex,Wsizey=solved.shape
    W=numpy.empty((Wsizex,1,))
    for i in range(Wsizex):
        W[i]=10**solved[i]
    W=W.flatten()
    for i in range(numknown):
        W=numpy.insert(W,positions[i],knownVec[i])
    return W
        

#print(C)
#print(checkPos(C,numpy.array([1,3])))
    
print("Ranking macierzy A z użyciem sredniej geometrycznej:")
print(geometric(A,numpy.array([3,1]),numpy.array([4,5]))) #pozycje podane -1

print("Ranking macierzy B z użyciem sredniej geometrycznej:")
print(geometric(B,numpy.array([2,1/2,1]),numpy.array([3,4,5]))) #pozycje podane -1

print("Ranking macierzy C z użyciem sredniej geometrycznej:")
print(geometric(checkPos(C,numpy.array([1,3])),numpy.array([2,5]),numpy.array([1,3]))) #pozycje podane -1

#
#Ranking macierzy A z użyciem sredniej geometrycznej:
#wynik pewny:
#[ 5.35311934  8.36693726  2.7275953   2.31136976  3.          1.        ]
#Ranking macierzy B z użyciem sredniej geometrycznej:
#wynik niepewny:
#[ 1.00002314  0.92779574  0.76996298  2.          0.5         1.        ]
#Ranking macierzy C z użyciem sredniej geometrycznej:
#wynik pewny:
#[  8.18670835   2.          10.11347353   5.           2.04604087
#   3.00786814]
