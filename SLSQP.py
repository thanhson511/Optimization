# OPTIMIZATION USING SLSQP
# Sequential Least Squares Programming optimization algorithm (SLSQP)
######################################################################
# min   ad(a+b+c)+c
# s.t:  abcd >= 25
#       1 <= a,b,c,d <= 5
#       a^2 + b^2 + c^2 + d^2 = 40
#
# Start_Point:   x_0 = (1,5,5,1)
######################################################################


# Import the datetime library
from datetime import date                              
# Get the current date and Print the formatted date
print('Today is', date.today().strftime("%d/%m/%Y"),'\n')   


import numpy as np
from scipy.optimize import minimize as min

def objective(x):
  a = x[0]
  b = x[1]
  c = x[2]
  d = x[3]
  return a*d*(a+b+c)+c

def constraint1(x):
  return x[0]*x[1]*x[2]*x[3]-25.0

def constraint2(x):
  sum_sq = 40
  for i in range(4):
    sum_sq = sum_sq - x[i]**2
  return  sum_sq

x0 = [1,5,5,1]
print(objective(x0))


bound = (1.0,5.0)
mybounds = (bound,bound,bound,bound)

con1 = {'type':'ineq','fun':constraint1}
con2 = {'type':'eq','fun':constraint2}

cons = [con1,con2]

# Sequential Least Squares Programming optimization algorithm (SLSQP)
sol = min(objective,x0,method='SLSQP',bounds=mybounds,constraints=cons)

# export to screen
print(sol)
print(sol.x)
print(sol.fun)
print(sol.success)
print(sol.message)
print(sol.nit)
print(sol.status)
