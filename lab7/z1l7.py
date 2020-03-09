from scipy.optimize import linprog

c=[-2, -1, -3]

A=[[1,1,1],[-1,-1,-1],[-1,-2,-1],[0,2,1]]
b=[30,-30,-10,20]
x_bounds=[0,None]

res = linprog(c, A_ub=A, b_ub=b, bounds=(x_bounds, x_bounds,x_bounds),options={"disp": True})