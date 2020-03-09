import numpy as np
from scipy.optimize import linear_sum_assignment

cost = np.array([[5,7,8,7], [6,4,7,6], [7,5,6,5], [4,3,5,9]])

x, y = linear_sum_assignment(cost)

for i in range(len(y)):
    print("warsztat ", i+1, "powinien naprawiać samochody marki: ", y[i]+1)

print(cost[x, y].sum())  
