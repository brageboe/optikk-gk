#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:02:30 2020

@author: brage

RAY-TRANSFER MATRIX 
for two thin lenses separated by distance d 
"""
import numpy as np

d = 75
f1 = 150
f2 = -150
so = 500

M = np.matrix([[1 - d / f1, d], [(d - f1 - f2) / (f1 * f2), 1 - d / f2]])
# detM should be 1, since input and output media have same refractive indices
detM = np.linalg.det(M) 

A = M[0,0]
B = M[0,1]
C = M[1,0]
D = M[1,1]

p = D / C   # F1 relative to input plane
q = - A / C # F2 relative to output plane

r = (D - 1) / C # principle plane 1 (PP1) relative to input plane. Positive sign to right of outputplane
s = (1 - A) / C # PP2 relative to output plane. Positive sign to left of outputplane

f1 = p - r  # F1 relative to PP1
f2 = q - s  # F2 relative to PP2

v = (D - 1) / C # nodal plane 1 (N1) relative to input plane
w = (1 - A) / C # N2 relative to output plane

#f_eq = - 1 / C
si = - (A * so + B) / (C * so + D) # image point
M_T = A + C * si # transversal magnification

print("p =", p)
print("q = ", q)
print("r =", r)
print("s = ", s)
print("f1 =", f1)
print("f2 =", f2)
print("v =", v)
print("w =", w, "\n")
print("For so =", so, ", then si =", si)
print("Transversal magnification M_T = ", M_T)

