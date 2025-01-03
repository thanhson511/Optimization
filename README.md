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


# Linear Programming Optimization with minimize function

This code demonstrates how to solve a linear programming problem using the `minimize` function from the `scipy.optimize` library in Python.

## Problem Statement

The code solves the following linear programming problem:

**Maximize:** 
  ```
  Z = 3x + 2y 
  ```

**Subject to:**
  ```
  x + 2y <= 4
  3x + y <= 5
  x >= 0
  y >= 0
  ```

## Code Overview

* **`objective(x)`:** Defines the objective function to be maximized. Note that it's defined as `-3*x[0] - 2*x[1]` because `scipy.optimize.minimize` is a minimization function. By negating the objective function, we effectively maximize it.
* **`constraints`:**  A list of dictionaries defining the constraints. Each constraint is defined with a `type` ('ineq' for inequality) and a `fun` (a lambda function representing the constraint).
* **`x0`:** Sets the initial guess for the solution.
* **`bounds`:** Defines the bounds for the variables `x` and `y`. In this case, both are constrained to be greater than or equal to 0.
* **`result = minimize(...)`:** Calls the `minimize` function with the objective function, initial guess, constraints, and bounds.
* **`print(result)`:** Prints the optimization result, including the optimal solution and objective function value.

## How to Run

1. Make sure you have the `scipy` library installed. If not, you can install it using `pip install scipy`.
2. Save the code as a Python file (e.g., `linear_programming.py`).
3. Run the code from your terminal using `python linear_programming.py`.

## Output

The code will print the optimal solution and the optimal value of the objective function.

## Note

This code provides a basic example of solving a linear programming problem using SciPy. You can modify the objective function, constraints, and bounds to solve different linear programming problems. 




# Constrained Optimization with Differential Evolution

This code demonstrates the use of the `scipy.optimize.differential_evolution` function to solve a constrained optimization problem.

## Problem Description

The objective is to minimize the following function:

```
f(a, b, c, d) = a*d*(a + b + c) + c**2 - b
```

subject to the following constraints:

```
a * b * c * d >= 25
a**2 + b**2 + c**2 + d**2 <= 40
```

where `1 <= a, b, c, d <= 5`.

## Solution Approach

The code uses the differential evolution algorithm to find the optimal solution. The algorithm parameters are as follows:

* `strategy`: 'best1bin'
* `maxiter`: 1000
* `popsize`: 15
* `tol`: 1e-7
* `mutation`: (0.5, 1)
* `recombination`: 0.7
* `init`: 'latinhypercube'
* `polish`: True

## Usage

1.  **Install Dependencies:** Make sure you have NumPy and SciPy installed.

2.  **Run the Code:** Simply execute the Python script. The output will display the optimization results, including:
    * Optimal solution (`x`)
    * Objective function value (`fun`)
    * Success status (`success`)
    * Message (`message`)
    * Number of iterations (`nit`)
    * Number of function evaluations (`nfev`)

## Output

The code will print the optimization result object and various attributes including the optimal solution, objective function value, success status, and performance information.

## Note

The objective function and constraints can be modified to solve different optimization problems. The differential evolution parameters can also be adjusted to fine-tune the optimization process.





# Constrained Optimization with Dual Annealing

This code demonstrates the use of the `scipy.optimize.dual_annealing` function to solve a constrained optimization problem.

## Problem Description

The objective is to minimize the following function:

```
f(a, b, c, d) = a*d*(a + b + c) + c**2 - b*d + sin(a*b) 
```

subject to the following constraints:

```
a * b * c * d >= 25
a**2 + b**2 + c**2 + d**2 = 40 
```

where `1 <= a, b, c, d <= 5`.

## Solution Approach

The code uses the dual annealing algorithm to find the optimal solution. This algorithm is particularly suitable for problems with many local minima. The `COBYLA` method is used as the local minimizer.

## Usage

1.  **Install Dependencies:** Make sure you have NumPy and SciPy installed. You can install them using pip:
    ```bash
    pip install numpy scipy
    ```
2.  **Run the Code:** Simply execute the Python script. The output will display the optimization results, including:
    * Optimal solution (`x`)
    * Objective function value (`fun`)
    * Success status (`success`)
    * Message (`message`)
    * Number of function evaluations (`nfev`)
    * Number of iterations (`nit`)

## Output

The code will print the optimization result object and various attributes including the optimal solution, objective function value, success status, and performance information.

## Note

The objective function and constraints can be modified to solve different optimization problems. The dual annealing parameters can also be adjusted to fine-tune the optimization process. For example, you can experiment with different values for `initial_temp`, `restart_temp_ratio`, and `visit`.
