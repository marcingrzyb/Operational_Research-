import numpy as np
from scipy.optimize import linear_sum_assignment

cost = np.array([[0.8, 0.8, 0.8, 0.6, 0.6, 0.6],
		[2, 2, 2, 1.5, 1.5, 1.5],
		[0.7, 0.7, 0.7, 0.6, 0.6, 0.6],
		[0.4, 0.4, 0.4, 0.2, 0.2, 0.2],
		[0.2, 0.2, 0.2, 0.4, 0.4, 0.4],
		[0.3, 0.3, 0.3, 0.5, 0.5, 0.5]])

x,y = linear_sum_assignment(cost)
print("\n ")
for i in range(0, len(y)):
    if(y[i]>2):
        print("zadanie ",i+1, "powinien wykonać pracowanik: ",2)
    else:
        print("zadanie ",i+1, "powinien wykonać pracowanik: ",1)
    
print(cost[x, y].sum())    