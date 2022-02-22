import numpy as np
import matplotlib.pyplot as plt


def function(x) -> float:
    return np.exp(x)+x-5

a = -1
b =  3
x_vector = np.arange(a,b, 1e-3)
error = 1e-4
difference = 1

plt.grid()
function_v = np.vectorize(function)
plt.plot(x_vector, function_v(x_vector))

while error < difference*2:

    c = (a + b) / 2

    a_func = function(a)
    b_func = function(b)
    c_func = function(c)

    if a_func * c_func > 0:
        a = c
    else:
        b = c

    difference = np.abs(b_func - a_func)

c = (a + b) / 2

print('Root: ', c)
plt.plot(c, function(c), 'ro')
plt.show()

