import scipy.optimize as spo
import numpy as np
import matplotlib.pyplot as plt

#defining the function, which we what to minimize
def f(x):
    y=x**3-9*x+18
    return y

#a starting guess for location of minimum
x_start=2.0

#result of minimization
result=spo.minimize(f, x_start)

if result.success:
    print("the minimum is at:")
    print(result.x)
    print("the value at the minimum is:")
    print(f(result.x))

else:
    print("could not find minimum")
