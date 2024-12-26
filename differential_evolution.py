import numpy as np  # Import the NumPy library for numerical operations
from scipy.optimize import differential_evolution  # Import the differential_evolution function from SciPy

def objective(x):  # Define the objective function to be minimized
    a, b, c, d = x  # Unpack the input array x into individual variables
    return a*d*(a+b+c) + c**2 - b  # Calculate and return the objective function value

def constraint1(x):  # Define the first constraint function
    return x[0]*x[1]*x[2]*x[3] - 25.0  # Calculate and return the value of the first constraint

def constraint2(x):  # Define the second constraint function
    return 40 - sum(xi**2 for xi in x)  # Calculate and return the value of the second constraint

bounds = [(1.0, 5.0)] * 4  # Define the bounds for each variable (1.0 <= a, b, c, d <= 5.0)

constraint_1 = {'type': 'ineq', 'fun': constraint1}  # Define the first constraint as an inequality constraint
constraint_2 = {'type': 'eq', 'fun': constraint2}  # Define the second constraint as an equality constraint

constraints = (constraint_1, constraint_2)  # Create a tuple of constraints

result = differential_evolution(  # Call the differential_evolution function to perform optimization
    func=objective,  # Pass the objective function
    bounds=bounds,  # Pass the bounds for the variables
    strategy='best1bin',  # Specify the differential evolution strategy
    maxiter=1000,  # Set the maximum number of iterations
    popsize=15,  # Set the population size
    tol=1e-7,  # Set the tolerance for convergence
    mutation=(0.5, 1),  # Set the mutation rate
    recombination=0.7,  # Set the recombination rate
    seed=None,  # Set the random seed (None for no seed)
    callback=None,  # Set the callback function (None for no callback)
    disp=True,  # Enable displaying the optimization progress
    polish=True,  # Enable polishing the final solution using a local optimizer
    init='latinhypercube'  # Specify the initialization method for the population
)

print(result)  # Print the optimization result object
print("Optimal solution:", result.x)  # Print the optimal solution
print("Objective function value:", result.fun)  # Print the objective function value at the optimal solution
print("Success:", result.success)  # Print whether the optimization was successful
print("Message:", result.message)  # Print the termination message from the optimizer
print("Number of iterations:", result.nit)  # Print the number of iterations performed
print("Number of function evaluations:", result.nfev)  # Print the number of function evaluations