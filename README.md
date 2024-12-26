# OPTIMIZATION USING SLSQP

This code demonstrates the use of the Sequential Least Squares Programming (SLSQP) optimization algorithm to solve a constrained optimization problem.

## Problem Statement

Minimize the objective function:

ad(a+b+c)+c


Subject to the following constraints:

abcd >= 25
1 <= a, b, c, d <= 5
a^2 + b^2 + c^2 + d^2 = 40


Starting point:

x_0 = (1, 5, 5, 1)


## Code Overview

The code uses the `scipy.optimize` library to implement the SLSQP algorithm. 

* **`objective(x)`:** Defines the objective function to be minimized.
* **`constraint1(x)`:** Defines the inequality constraint `abcd >= 25`.
* **`constraint2(x)`:** Defines the equality constraint `a^2 + b^2 + c^2 + d^2 = 40`.
* **`x0`:** Sets the initial guess for the solution.
* **`bounds`:** Defines the bounds for the variables.
* **`cons`:**  A list of dictionaries defining the constraints.
* **`sol = min(...)`:** Calls the `minimize` function with the SLSQP method and specified constraints.
* **`print(sol)`:** Prints the optimization result object.
* **`print(sol.x)`:** Prints the optimal values of the variables.
* **`print(sol.fun)`:** Prints the optimal value of the objective function.
* **`print(sol.success)`:** Prints a boolean indicating whether the optimization was successful.
* **`print(sol.message)`:** Prints a message describing the optimization result.
* **`print(sol.nit)`:** Prints the number of iterations performed.
* **`print(sol.status)`:** Prints an integer indicating the termination status of the optimization.

## How to Run

1. Make sure you have the `scipy` library installed. If not, you can install it using `pip install scipy`.
2. Save the code as a Python file (e.g., `optimization.py`).
3. Run the code from your terminal using `python optimization.py`.

## Output

The code will print the current date, the initial objective function value, and the optimization results, including the optimal solution, function value, success status, and other information.

## Note

This code provides a basic example of using SLSQP for optimization. You can modify the objective function, constraints, and bounds to solve different optimization problems.
