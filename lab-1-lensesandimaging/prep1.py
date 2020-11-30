#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:07:40 2020

@author: brage
"""

#object | lens 1 | distance | lens 1
#output: distance to image plane

import numpy as np

f = 100
d = 270
sO = 300

F = np.matrix([[1, 0], [-1/f, 1]])
D = np.matrix([[1, d], [0, 1]])
SO = np.matrix([[1, sO], [0, 1]])

M = F @ D @ F @ SO

# imaging condition A01 = 0, where A=(1 si; 0 1)*M
si = -M[0,1] / M[1,1]

print(si)