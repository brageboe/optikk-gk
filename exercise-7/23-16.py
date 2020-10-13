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

theta_critical = np.arcsin(1/1.5)           # critical angle for total internal reflection
N = 128                                     # number of data points
theta = np.linspace(theta_critical, np.pi/2, N) # angle of incidence
n1 = 1                                      # refractive index of ambient
n2 = 1.65                                   # refractive index of fresnel rhomb
n = n1 / n2                                 # relative refractive index

print("Critical angle = ", theta_critical * 180 / np.pi)

C1 = np.sqrt(np.sin(theta)**2 - n**2)
# Phase shift equations (23-38) and (23-39) in PPP
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

theta_apex = theta[idx] # the angle for which two internal reflections in a Fresnel rhomb produce a relative phase shift of pi/2 (i.e. circular pol.)
print("Apex angle for a Fresnel Rhomb with refractive index", n2, "is:", theta_apex * 180 / np.pi)

# 23-16 b)
# What is the phase difference between TE and TM (after BOTH reflections inside the rhomb) when the angle is 5% above/below the apex angle?
apex_deviated = [0.95 * theta_apex, 1.05 * theta_apex]

C2 = np.sqrt(np.sin(apex_deviated)**2 - n**2)
# multiply phase shifts by 2, due to two internal reflections inside rhomb:
phase_TM_deviated = -4 * np.arctan( C2 / (n**2 * np.cos(apex_deviated)) ) + np.pi
phase_TE_deviated = -4 * np.arctan( C2 / np.cos(apex_deviated) )
phase_difference_deviated = phase_TE_deviated - phase_TM_deviated
print("Phase difference between TM and TE modes after both internal reflections, when the apex angle is 5% below/above correct apex angle:", phase_difference_deviated / np.pi, "* pi.")
