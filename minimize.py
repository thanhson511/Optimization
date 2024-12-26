'''
This example solves the following linear programming problem:
__ Maximize: z = 3x + 2y
__ Subject to:
        x + 2y <= 4
        3x + y <= 5
        x >= 0
        y >= 0
''' 

import numpy as np
from scipy.optimize import minimize

# Objective function
def objective(x):
    """
    Calculates the value of the objective function to be minimized.

    Args:
      x: A list or array containing the values of the decision variables (x, y).

    Returns:
      The value of the objective function.
    """
    return -3*x[0] - 2*x[1]  # -3x - 2y

# Constraints
constraints = [
    {'type': 'ineq', 'fun': lambda x:  4 - (x[0] + 2*x[1])},  # x + 2y <= 4
    {'type': 'ineq', 'fun': lambda x:  5 - (3*x[0] + x[1])},  # 3x + y <= 5
    {'type': 'ineq', 'fun': lambda x:  x[0]},                # x >= 0
    {'type': 'ineq', 'fun': lambda x:  x[1]}                 # y >= 0
]
# Each constraint is a dictionary with 'type' and 'fun' keys.
# 'type': 'ineq' indicates an inequality constraint.
# 'fun': A lambda function that defines the constraint. It should return a non-negative value if the constraint is satisfied.

# Initial guess
x0 = [0, 0]  # Starting point for the optimization algorithm

# Solving the problem
result = minimize(objective, x0, constraints=constraints, bounds=[(0, None), (0, None)])
# minimize: Function from scipy.optimize to find the minimum of the objective function.
# objective: The objective function to be minimized.
# x0: The initial guess.
# constraints: The list of constraints.
# bounds: Specifies the bounds for each decision variable. (0, None) means the variable should be greater than or equal to 0.

# Print the results
if result.success:
    print(f"Optimal value (Z): {-result.fun}")  # Print the optimal value of the objective function (negated because we are maximizing)
    print(f"Optimal solution: x = {result.x[0]}, y = {result.x[1]}")  # Print the optimal values of x and y
else:
    print("No solution found")  # Print a message if no solution is found