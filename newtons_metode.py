import numpy as np

def function(x):
    return np.cos(x) - x

def primed(x):
    return -(np.sin(x))-1

x = 3

difference = 1
error = 1e-5

while difference > error:
    x_n = x - (function(x)/primed(x))
    difference = np.abs(x_n-x)
    x = x_n
    print(x)

print('Estimated value for x:' , x)
