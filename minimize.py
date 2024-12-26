import numpy as np
from scipy.optimize import minimize

# Objective function
def objective(x):
    return -3*x[0] - 2*x[1]

# Constraints
constraints = [
    {'type': 'ineq', 'fun': lambda x:  4 - (x[0] + 2*x[1])},  # x + 2y <= 4
    {'type': 'ineq', 'fun': lambda x:  5 - (3*x[0] + x[1])},  # 3x + y <= 5
    {'type': 'ineq', 'fun': lambda x:  x[0]},                # x >= 0
    {'type': 'ineq', 'fun': lambda x:  x[1]}                 # y >= 0
]

# Initial guess
x0 = [0, 0]

# Solving the problem
result = minimize(objective, x0, constraints=constraints, bounds=[(0, None), (0, None)])

# Print the results
if result.success:
    print(f"Optimal value (Z): {-result.fun}")
    print(f"Optimal solution: x = {result.x[0]}, y = {result.x[1]}")
else:
    print("No solution found")
