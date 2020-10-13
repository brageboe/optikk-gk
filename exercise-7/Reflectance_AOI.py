#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:07:38 2020

@author: brage
"""
# Simple calculation of Fresnel reflectances for different angle of incidences.

import numpy as np

theta = np.radians([0.0, 10.0, 45.0, 90.0]) 

n = 1.33

C1 = np.sqrt(n**2 - np.sin(theta)**2)

Rp = ( (-n**2 * np.cos(theta) + C1) / (n**2 * np.cos(theta) + C1) )**2

Rs = ( (np.cos(theta) - C1) / (np.cos(theta) + C1) )**2

print("Rp =", Rp * 100)
print("Rs =", Rs * 100)
