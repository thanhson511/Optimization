'''
Objective:

Minimize the function:

f(a, b, c, d) = a * d * (a + b + c) + c^2 - b * d + sin(a * b)

Subject to the constraints:

a * b * c * d >= 25
a^2 + b^2 + c^2 + d^2 = 40
Bounds:

Where the values of a, b, c, and d are within the range:

1 <= a, b, c, d <= 5
In essence, the code aims to find the values of a, b, c, and d that minimize the objective function f(a, b, c, d) while satisfying the given constraints. 
It employs the dual annealing optimization algorithm, combined with the COBYLA local search method, to achieve this.
'''

import numpy as np  # Import the NumPy library for numerical operations, especially for the sine function
from scipy.optimize import dual_annealing  # Import the dual_annealing function from SciPy for optimization

def objective(x):  # Define the objective function to be minimized
    a, b, c, d = x  # Unpack the input array x into individual variables a, b, c, and d
    return a*d*(a+b+c) + c**2 - b*d + np.sin(a*b)  # Calculate and return the objective function value

def constraint1(x):  # Define the first constraint function
    return x[0]*x[1]*x[2]*x[3] - 25.0  # Calculate and return the value of the first constraint (a*b*c*d >= 25)

def constraint2(x):  # Define the second constraint function
    return 40 - sum(xi**2 for xi in x)  # Calculate and return the value of the second constraint (a^2 + b^2 + c^2 + d^2 = 40)

bounds = [(1.0, 5.0)] * 4  # Define the bounds for each variable (1.0 <= a, b, c, d <= 5.0)

def combined_constraints(x):  # Define a function to combine both constraints
    return [constraint1(x), abs(constraint2(x))]  # Return a list containing both constraint values, with the second constraint's absolute value taken to ensure it's treated as an inequality

result = dual_annealing(  # Call the dual_annealing function to perform optimization
    func=objective,  # Pass the objective function to be minimized
    bounds=bounds,  # Pass the bounds for the variables
    x0=None,  # Starting point for optimization (None means random starting point)
    maxiter=1000,  # Set the maximum number of iterations
    initial_temp=5230.0,  # Set the initial temperature for the annealing process
    restart_temp_ratio=2e-5,  # Set the ratio for restarting the annealing process if it gets stuck
    visit=2.62,  # Control parameter for visiting different regions of the search space
    accept=-5.0,  # Control parameter for accepting new solutions
    maxfun=10000000.0,  # Set the maximum number of function evaluations
    seed=None,  # Set the random seed (None for no seed)
    no_local_search=False,  # Enable local search to refine the solution
    callback=None,  # Set the callback function (None for no callback)
    minimizer_kwargs={'method': 'COBYLA', 'constraints': {'type': 'ineq', 'fun': combined_constraints}}  # Use the COBYLA method for local search with the combined constraints as inequality constraints
)

print(result)  # Print the optimization result object
print("Optimal solution:", result.x)  # Print the optimal solution found
print("Objective function value:", result.fun)  # Print the objective function value at the optimal solution
print("Success:", result.success)  # Print whether the optimization was successful
print("Message:", result.message)  # Print the termination message from the optimizer
print("Number of function evaluations:", result.nfev)  # Print the number of times the objective function was evaluated
print("Number of iterations:", result.nit)  # Print the number of iterations performed