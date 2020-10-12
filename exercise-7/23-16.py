#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:51:48 2020

@author: brage
"""
# PHASE DIFFERENCE PLOTS FOR FRESNEL RHOMB
# * Finds Apex angle(s)
# * Plots phase shifts for both TE and TM
# * Plots phase difference between TE and TM together with a line (default -3pi/4)
#   - change picheck to a different multiple of pi/2 to something more suitable depending on your rhomb
#   

import numpy as np
import matplotlib.pyplot as plt

theta_critical = np.arcsin(1/1.5)
N = 128
theta = np.linspace(theta_critical, np.pi/2, N)
n1 = 1
n2 = 1.65
n = n1 / n2

print("Critical angle = ", theta_critical * 180 / np.pi)
C1 = np.sqrt(np.sin(theta)**2 - n**2) 

# equations (23-38) and (23-39) in PPP
phase_TM = -2 * np.arctan( C1 / (n**2 * np.cos(theta)) ) + np.pi
phase_TE = -2 * np.arctan( C1 / np.cos(theta) )

# FIGURE: TE and TM phase shifts
figure = plt.figure()
plt.plot(theta, phase_TM, 'g', label='TE')
plt.plot(theta, phase_TE, 'b', label='TM')
plt.xlabel(r"Incident angle $\theta$ [rad]")
plt.ylabel(r"Phase shift $\phi$ [rad]")
plt.title(r"Phase shift on reflection, for AOI above critical angle $\theta > \theta_c$")
plt.legend()
plt.show()

phase_difference = phase_TE - phase_TM
picheck = - np.linspace(np.pi * 0.75, np.pi * 0.75, N)

# FIGURE: phase difference TE-TM
figure = plt.figure()
plt.plot(theta, phase_difference, label=r'$\Delta\phi = \phi_{TE} - \phi_{TM}$' )
plt.plot(theta, picheck, label=r'$-3\pi/4$')
idx = np.argwhere(np.diff(np.sign(picheck - phase_difference))).flatten()
plt.plot(theta[idx], picheck[idx], 'ro')
plt.xlabel(r"Incident angle $\theta$ [rad]")
plt.ylabel(r"Phase shift $\phi$ [rad]")
plt.legend()
plt.show()

theta_apex = theta[idx]
print("Apex angle(s) for a Fresnel Rhomb with refractive index", n2, "is: ", theta_apex * 180 / np.pi)

# 23-16 b)
# What is the phase difference between TE and TM (after both reflections inside the rhomb) when the angle is 5% above/below the apex angle?