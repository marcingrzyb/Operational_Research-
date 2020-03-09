import numpy
A = numpy.array([
	[20, -150, -250],
	[150, -80, -100],
	[250, 100, 40]])

def minmax(matrix):
    x_size, y_size = matrix.shape
    mins=[]
    maxes=[]
    for i in range(x_size):
        mins.append((min(matrix[i]),i+1))
        maxes.append((max(matrix[:,i]),i+1))
    return ("A", max(mins)[1], "B", min(maxes )[1])

print(minmax(A))

#('A', 3, 'B', 3)