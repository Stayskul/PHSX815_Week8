from scipy.optimize import minimize as min
import numpy as np
import matplotlib.pyplot as plt

#defining a 2D function (f(x,y)=z), which we what to minimize (any number of variables should work)
def f(x):
    x1, x2 = x #define the parameters
    return (x1-2)**2+(x2-4)**2 #the function
  
#a starting guess for location of minimum
x_start=np.array([1.3, 0.7])

#result of minimization using nelder-mead method
result=min(f, x_start, method='nelder-mead')

if result.success:
    print("the minimum is at:")
    print(result.x)
    print("the value at the minimum is:")
    print(f(result.x))

else:
    print("could not find minimum")
