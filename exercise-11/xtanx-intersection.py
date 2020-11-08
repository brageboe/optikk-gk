#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:20:06 2020

@author: brage
"""


import numpy as np

# finds intersection points where x = tan(x).
# relevant for finding secondary maxima in single-slit diffraction patterns.
# see book PPP figure 11.3

dp = 100000
accuracy = 0.001
x = np.linspace( 3.5*np.pi, 5.5*np.pi, dp)
tanx = np.tan(x)

for i in range(dp):
    if abs(x[i]/tanx[i] - 1) < accuracy:
        print(x[i] / np.pi)