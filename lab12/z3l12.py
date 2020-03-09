import numpy as np
from scipy.optimize import linear_sum_assignment

cost = np.array([[5.6, 3.2, 4.4, 4.7, 0],
		[6, 3.5, 4.6, 4.5, 0],
		[0, 4, 5, 4.8, 0],
		[0, 3.8, 4.7, 4.8, 0],
		[4.8, 4, 4.5, 4.2, 0]])

costFixed=cost*-1

x,y = linear_sum_assignment(costFixed)


print("\nlokata nr 5= brak przypsianej lokaty")
for i in range(len(y)):
    print("bank numer: ", i+1, "lokata numer: ", y[i]+1)
print(cost[x, y].sum())