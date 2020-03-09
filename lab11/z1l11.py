from cvxopt import matrix, solvers
Q = matrix([ [10.0, 2.0], [2.0, 1.0] ])
p = matrix([-10.0,-25.0])
G = matrix([[1.0,-1.0,-1.0,0.0],[2.0,-1.0,0.0,-1.0]])
h = matrix([10.0,-9.0,0.0,0.0])

sol=solvers.qp(Q, p, G, h)

print(sol['x'])

