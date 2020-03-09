import numpy

A=numpy.matrix([[1,2/3,2,5/2,5/3,5],
 [3/2, 1, 3, 10/3, 3, 9],
 [1/2, 1/3, 1, 4/3, 7/8, 5/2], 
 [2/5, 3/10, 3/4, 1, 5/6, 12/5], 
 [3/5,1/3,8/7,6/5 ,1 ,3],
 [1/5, 1/9, 2/5, 5/12, 1/3, 1]])
B=numpy.matrix([[1,2/5,3,7/3,1/2,1,2],
                [5/2,1,4/7,1,1,3,2/3],
                [1/3,7/4,1,1/2,2,1/2,1],
                [3/7,1,2,1,4,2,6],
                [2,1,1/2,1/4,1,1/2,3/4],
                [1,1/3,2,1/2,2,1,5/8],
                [1/2,3/2,1,1/6,4/3,8/5,1]])

C=numpy.matrix([[1,2/3,2/15,1,8,12/5,1,1/2],
                [3/2,1,1,2,1,2/3,1/6,1],
                [15/2,1,1,5/2,7/8,2,1,1/5],
                [1,1/2,2/5,1,4/3,1,2/7,1],
                [1/8,1,8/7,3/4,1,1/5,2/7,1],
                [5/12,3/2,1/2,1,5,1,3,2],
                [1,6,1,7/2,7/2,1/3,1,3/11],
                [2,1,5,1,1,1/2,11/3,1]])

D=numpy.matrix([[0,1,1,-1,-1,1,-1],
                [-1,0,0,1,1,-1,0],
                [-1,0,0,0,1,1,-1],
                [1,-1,0,0,1,0,1],
                [1,0,-1,-1,0,1,-1],
                [-1,1,-1,1,-1,0,0],
                [1,0,1,-1,1,0,0]])

E=numpy.matrix([[0,1,0,0,-1],
                [-1,0,0,0,1],
                [0,0,0,1,0],
                [0,0,-1,0,0],
                [1,-1,0,0,0]])

F=numpy.matrix([[0,-1,1,-1,1,-1,1,-1,1],
                [1,0,1,1,1,-1,-1,-1,-1],
                [-1,-1,0,-1,1,-1,1,1,1],
                [1,-1,1,0,-1,1,-1,1,-1],
                [-1,-1,-1,1,0,-1,1,1,1],
                [1,1,1,-1,1,0,-1,-1,-1],
                [-1,1,-1,1,-1,1,0,1,-1],
                [1,1,-1,-1,-1,1,-1,0,1],
                [-1,1,-1,1,-1,1,1,-1,0]])


def changeToTournament(matrix):
    x_size, y_size = matrix.shape
    new=numpy.empty((x_size,y_size,))
    for i in range(x_size):
        for j in range(y_size):
            if(matrix.item(i,j)>1):
                new[i][j]=1
            elif(matrix.item(i,j)==1):
                new[i][j]=0
            else:
                new[i][j]=-1
    return new

def checkOvrTournament(matrix):
    x_size, y_size = matrix.shape
    checkedBool=True
    for i in range(x_size):
        for j in range(y_size):
            if(matrix.item(i,j)!=(-1*matrix.item(j,i))):
                checkedBool=False
    if(checkedBool==False):
        return("nie jest uogólniona turniejowa.")
    else:
        return("jest uogólniona turniejowa."+checkDrawPossibility(matrix))

def checkDrawPossibility(matrix):
    x_size, y_size = matrix.shape
    checkedBool=False
    for i in range(x_size):
        for j in range(y_size):
            if(i!=j):
                if(matrix.item(i,j)==0):
                    checkedBool=True
    if(checkedBool==False):
        return(" Macierz nie dopuszcza remisow.Jej indeksy Kendalla(uogólniony oraz klasyczny)to: "+str(ovrKendallIndex(matrix))+" "+str(kendallIndex(matrix)))
    else:
        return(" Macierz dopuszcza remisy.Jej indeks Kendalla(uogólniony)to:"+str(ovrKendallIndex(matrix)))

def kendallIndex(matrix):
    x_size, y_size = matrix.shape
    triadsC=0
    for i in range(x_size):
        for j in range(i+1,x_size):
            for k in range(j+1,x_size):
                if(matrix.item(i,j)==matrix.item(j,k)==matrix.item(k,i)):
                    triadsC+=1
    if(x_size%2!=0):
        I=(x_size**3-x_size)/24
    else:
        I=(x_size**3-4*x_size)/24
    return(1-(abs(triadsC/I)))
    
def ovrKendallIndex(matrix):
    x_size, y_size = matrix.shape
    triadsC=0
    for i in range(x_size):
        for j in range(i+1,x_size):
            for k in range(j+1,x_size):
                if(matrix.item(i,j)==matrix.item(j,k)==0 and matrix.item(k,i)!=0) or(matrix.item(i,j)==matrix.item(k,i)==0 and matrix.item(j,k)!=0)or(matrix.item(j,k)==matrix.item(k,i)==0 and matrix.item(i,j)!=0):
                    triadsC+=1
                elif(matrix.item(i,j)==matrix.item(j,k)!=0 and matrix.item(k,i)==0) or(matrix.item(i,j)==matrix.item(k,i)!=0 and matrix.item(j,k)==0)or(matrix.item(j,k)==matrix.item(k,i)!=0 and matrix.item(i,j)==0):
                    triadsC+=1
                elif(matrix.item(i,j)==matrix.item(j,k)==matrix.item(k,i)!=0):
                    triadsC+=1
    if x_size % 4 == 0:
        y = (13 * x_size**3 - 24 * x_size * x_size - 16 * x_size) / 96
    elif x_size % 4 == 1:
        y = (13 * x_size**3 - 24 * x_size * x_size - 19 * x_size + 30) / 96
    elif x_size % 4 == 2:
        y = (13 * x_size**3 - 24 * x_size * x_size - 4 * x_size) / 96
    else:
        y = (13 * x_size**3 - 24 * x_size * x_size - 19 * x_size + 18) / 96
    return(1-(abs(triadsC)/y))



aTour=changeToTournament(A)
bTour=changeToTournament(B)
cTour=changeToTournament(C)
print("Macierz A ",checkOvrTournament(aTour))
print("Macierz B ",checkOvrTournament(bTour))
print("Macierz C ",checkOvrTournament(cTour))
print("Macierz D ",checkOvrTournament(D))
print("Macierz E ",checkOvrTournament(E))
print("Macierz F ",checkOvrTournament(F))

