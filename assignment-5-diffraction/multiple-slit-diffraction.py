#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:48:44 2020

@author: brage
"""
import numpy as np
import matplotlib.pyplot as plt

# SYSTEM CONSTANTS
DP = 1000                           # data points
wl = 532                            # wavelength in nanometers
k = 2*np.pi/wl                      # wave vector
theta0 = np.linspace(-3, 3, DP) * np.pi / 180      # angle after slit
L = 5 * 10**9                       # distance to observation screen in nm
N = [1,2,5,8]                       # number of slits

b = 34 * 10**3                      # slit width
a = 6*b#68 * 10**3                      # slit separation

# INTENSITY CALCULATION
beta = 0.5*k*b*np.sin(theta0)
alpha = 0.5*k*a*np.sin(theta0)

intensity = []
for n in N:
    intensity.append( (np.sin(beta)/beta)**2 * (np.sin(n*alpha)/np.sin(alpha))**2 )
for i in range(len(N)):
    intensity[i] = intensity[i] / np.max(intensity[i]) #normalize

# FIGURE
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(theta0*180/np.pi, intensity[0])
axs[0, 0].set_title('1 slit:')
axs[0, 1].plot(theta0*180/np.pi, intensity[1])
axs[0, 1].set_title('2 slits:')
axs[1, 0].plot(theta0*180/np.pi, intensity[2])
axs[1, 0].set_title('5 slits:')
axs[1, 1].plot(theta0*180/np.pi, intensity[3])
axs[1, 1].set_title('8 slits:')

for ax in axs.flat:
    ax.set(xlabel=r'$\theta$ [deg]', ylabel='Intensity [arb.unit]')
    ax.label_outer()
plt.show()
  
plt.plot(alpha/np.pi, intensity[1])
plt.xlabel(r'$\alpha/\pi$ [rad]')
plt.ylabel('Intensity [arb.unit]')
