#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:46:10 2020

@author: brage
"""
## SLAB WAVEGUIDE
# A waveguide simplified as a thin-film model
#
#   n_2
#  --------------------------------
#   n_1      wave--->       b
#  --------------------------------
#   n_2
#
# where n_1 > n_2 to ensure total internal reflection
# b = height of n_1 region 

import numpy as np
import matplotlib.pyplot as plt
import sys

P = 10000                                       # data points

# system constants
wl = 1.55                                      # wavelength, micrometers
n_1 = 1.7                                       # inner material refractive index
n_2 = 1.4                                       # outer material refractive index
rhs_modes = 4                                   # number of modes to plot of right-hand-side mode relation eq

# system variables
bwl = np.arange(.25, 2.0, .25)                  # b / wl
print(bwl)
N = np.linspace(n_2 * 1.0001, n_1 * 0.999, P)   # avoid divide by zero
beta = 2 * np.pi * N / wl                       # propagation constant

### MODE DISPERSION CALCULATION ###
MD_lhs = []                                     # left hand side of mode dispersion equation
for i in bwl:                                   # calculate for various b/wl
    MD_lhs.append(np.sqrt(n_1**2 - N**2) * 2 * np.pi * i)
MD_rhs = 2 * np.arctan(np.sqrt((N**2 - n_2**2) / (n_1**2 - N**2))) # right hand side, valid for any multiplum of pi, but atm we are looking for single mode m=0

plt.figure()
for i in range(rhs_modes):
    plt.plot(N, MD_rhs + i * np.pi, '#1f77b4')
for i in range(len(bwl)):
    plt.plot(N, MD_lhs[i], '#ff7f0e')
plt.grid(True)
plt.xlabel(r"$N$")
plt.ylabel(r"phase [rad]")
plt.title(r"Mode dispersion (TE) for $n_1=$" + str(n_1) + " $n_2=$"+ str(n_2) + " $\lambda=$"+ str(wl))
plt.show()

print("(Mode dispersion MD_lhs has indices 0 -", len(MD_lhs) - 1, " for every value of b/wl)")
lhs_index = int(input("Choose which MD_lhs (red curves) to find intersect points: "))
idx = np.argwhere(np.diff(np.sign(MD_lhs[lhs_index] - MD_rhs))).flatten()

print("\nMD_rhs", idx," = ", MD_rhs[idx])
print("MD_lhs[", lhs_index, "]" ,idx, " = ", MD_lhs[lhs_index][idx])
print("N",idx," = ", float(N[idx]))
print("b = ", float(bwl[lhs_index] * wl), "um")


### Ey FIELD COMPONENT CALCULATION ###
# Use an N and b found from the mode calculation
N = float(N[idx])                                   # set the new effective refractive index
b = float(bwl[lhs_index] * wl)                      # set the new slab thickness
K = np.sqrt(n_1**2 - N**2) * 2 * np.pi / wl         # diff. eq. solution wave prop. constants
gamma = np.sqrt(N**2 - n_2**2) * 2 * np.pi / wl     # diff. eq. solution wave prop. constants
A = 1                                             # diff. eq. solution constant
B = A                                               # diff. eq. solution constant
C = gamma * A / K                                   # diff. eq. solution constant
D = A * (K * np.sin(K * b) / gamma - np.cos(K * b)) # diff. eq. solution constant

print("\nDifferential equation solution constants:")
print("K =", K, "; gamma =", gamma, "\nA = B =", A, "; C =", C, "; D =", D)

x = np.linspace(-4*b, 4*b, P)       # x position
E_y = []
for i in x:
    #print(i, " ", type(i))
    if i < 0:
        E_y.append(A*np.exp(gamma*i))
    elif i >= 0 and i <= b:
        E_y.append(B*np.cos(K*i) + C*np.sin(K*i))
    elif i > b:
        E_y.append(D*np.exp(-gamma*(i - b)))
    else:
        print("Invalid x value when attempting to calculate E_y: x =", i)
        sys.exit("Exiting program.")

xlimit = [-max(E_y), max(E_y)]
plt.figure()
plt.plot(E_y, x)
plt.plot(xlimit, [0, 0], 'k', linewidth=0.5)
plt.plot(xlimit, [b, b], 'k', linewidth=0.5)
plt.grid(True)
plt.xlim(xlimit)
plt.xlabel(r"$E_y$ [a.u]")
plt.ylabel(r"$x$ [$\mu$m]")
plt.title(r"$N = $" + str(round(N, 4)) + " b = " + str(b))
plt.show()
      
      
      
      
      
      
      