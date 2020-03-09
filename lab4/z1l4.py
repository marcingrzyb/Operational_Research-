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

def arithmetic(matrix,knownVec,positions):
    numknown=knownVec.size
    x_size, y_size = matrix.shape
    print(checker(matrix,numknown,x_size))
    new=numpy.empty((x_size-numknown,y_size,))
    newb=numpy.empty((numknown,y_size,))
    for i in range(x_size-numknown):
        new[i]=matrix[i]
    newx_size, newy_size = new.shape
    newb=new[:,newy_size-numknown:newy_size]
    new=numpy.delete(new,numpy.s_[newy_size-numknown:newy_size],axis=1)
    newx_size, newy_size = new.shape
    for i in range(newx_size):
        for j in range(newy_size):
            if(i!=j):
                new[i][j]=new.item(i,j)*(-1/(x_size-1))

    newb=newb.dot(knownVec)
    newb=newb*(1/(x_size-1))
    W=numpy.linalg.solve(new,newb)
    for i in range(numknown):
        W=numpy.insert(W,positions[i],knownVec[i])
    return W
print("Ranking macierzy A z użyciem sredniej arytmetycznej:")
print(arithmetic(A,numpy.array([3,1]),numpy.array([4,5]))) #pozycje podane -1

print("Ranking macierzy B z użyciem sredniej arytmetycznej:")
print(arithmetic(B,numpy.array([2,1/2,1]),numpy.array([3,4,5]))) #pozycje podane -1

print("Ranking macierzy C z użyciem sredniej arytmetycznej:")
print(arithmetic(checkPos(C,numpy.array([1,3])),numpy.array([2,5]),numpy.array([1,3]))) #pozycje podane -1


#Ranking macierzy A z użyciem sredniej arytmetycznej:
#wynik pewny:
#[ 5.3832862   8.41331945  2.7447984   2.32718182  3.          1.        ]
#Ranking macierzy B z użyciem sredniej arytmetycznej:
#wynik niepewny:
#[ 2.19106271  2.13823058  1.39445155  2.          0.5         1.        ]
#Ranking macierzy C z użyciem sredniej arytmetycznej:
#wynik pewny:
#[  8.20540492   2.          10.13524961   5.           2.05217026
#   3.01702866]