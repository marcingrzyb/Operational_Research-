from scipy.optimize import linprog

#5a+15b>=50
#20a+5b>=40
#15a+2b<=60
#8a+4b->min
#
c=[8,4]
A=[[-5,-15],[-20,-5],[15,2]]
b=[-50,-40,60]

x_bounds=[0,None]

res = linprog(c, A_ub=A, b_ub=b, bounds=(x_bounds, x_bounds),options={"disp": True})


