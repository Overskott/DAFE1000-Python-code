import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # Getting input form user and checking if integer is given
    while True:
        try:
            a = float(input("Please provide the real part: "))
        except (TypeError, ValueError):
            print("Error: Input must be of float type.")
        else:
            break

    while True:
        try:
            b = float(input("Please provide the imaginary part: "))
        except (TypeError, ValueError):
            print("Error: Input must be of float type.")
        else:
            break

    while True:
        try:
            n = int(input("Please provide the number of roots: "))
        except (TypeError, ValueError):
            print("Error: Input must be of integer type.")
        else:
            break

    # Calculate r-value
    r = np.sqrt(a**2 + b**2)

    #Calculate theta-value and checking quadrant (numpy.arctan returns values in (pi/2, -<pi/2))
    if a == 0: # Handling division by zero
        theta = 0
    elif a < 0:
        theta = np.arctan(b/a) + np.pi
    else:
        theta = np.arctan(b/a)

    # finding roots and plotting them
    for k in range(0, n):
        z = r**(1/n)*np.exp(1j*(theta + 2*np.pi*k)/n)
        plt.plot(z.real, z.imag, 'rx')

    # Show plot with grid
    plt.grid()
    plt.show()




