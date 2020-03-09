from scipy.optimize import linprog
import numpy 
import math

c = [23, 17]
c=numpy.negative(c)

A =[[4, 3],
[1, 1]]

b = [190, 55]

max_fun = 0
max_params = (0,0)
init_bounds = ((0, None), (0,None))
def is_integer(value):
    return math.floor(value) == value

def solve_task(bounds_param):
    global max_fun
    global max_params
    optimalization = linprog(c, A, b, bounds = bounds_param)
    fun_res = abs(optimalization.fun)

    is_feasible = True
    if (any([(j in optimalization.message) == True for j in ['infeasible','failed']])):
        is_feasible = False
    if is_feasible:
        x = tuple([round(i,2) for i in optimalization.x])
        if (max_fun < fun_res and is_integer(x[0]) and is_integer(x[1])):
                max_fun = fun_res
                max_params = x
                return
        if (is_integer(x[0])):
            upper = math.ceil(x[1])
            lower = math.floor(x[1])
            solve_task((bounds_param[0],(0,lower)))
            solve_task((bounds_param[0],(upper,None)))
        else:
            upper = math.ceil(x[0])
            lower = math.floor(x[0])
            solve_task(((0,lower),bounds_param[1]))
            solve_task(((upper,None),bounds_param[1]))

solve_task(init_bounds)

print('Łańcuszki', int(max_params[0]))
print('Pierscionki', int(max_params[1]))