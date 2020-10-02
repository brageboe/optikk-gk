import numpy as np
import matplotlib.pyplot as pp
# omega = 1

pi = np.pi
t = [0, pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4, 2*pi]

# B
Ex = 2*np.sin(t)
Ey = np.cos(t)

print("Ex =", Ex)
print("Ey =", Ey)

O = [0,0] #origin

pp.arrow(0,0, Ex, Ey)
