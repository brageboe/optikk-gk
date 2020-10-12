#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:34:03 2020

@author: brage
"""

# 4-24 FROM PPP BOOK, PAGE 112
#
# ### ELECTRIC FIELD POLARIZATION ###
# Plots showing the evolution of the electric field vector at the plane z=0
# over one complete cycle. 
#
# 
# E = Ex sin(kz - wt + \phi_0x) + Ey sin(kz - wt + \phi_0y)
#
# each sub-exercise has different values for Ex, Ey, \phi_0x, \phi_0y

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import matplotlib.patches as patches


# Calculate Fields
time = np.linspace(0, 2*np.pi, 32) # assuming omega = 1

subexercise = input("Choose sub exercise (a,b,c,d,e):")
if subexercise == 'a':
    Ex = 2*np.sin(time)
    Ey = np.sin(time)
elif subexercise == 'b':
    Ex = 2*np.sin(time)
    Ey = np.cos(time)
elif subexercise == 'c':
    Ex = 2*np.sin(time)
    Ey = -np.cos(time)
elif subexercise == 'd':
    Ex = 2*np.sin(time + np.pi/4)
    Ey = np.cos(time - np.pi/4)   
elif subexercise == 'e':
    Ex = 2*np.sin(time)
    Ey = np.sin(time - np.pi/4)

# FIGURE #
# Create figure
fig = plt.figure()
ax = fig.gca()
#ax.grid(True, which='both', axis='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# Axes labels and limiters
ax.set_xlabel('Ex')
ax.set_ylabel('Ey')
ax.set_ylim(min(Ey), max(Ey))
ax.set_xlim(min(Ex), max(Ex))
ax.set_aspect('equal', adjustable='box')

# Plot red-dotted outline
plt.plot(Ex, Ey, 'r:')

# Animate arrows
patch = patches.Arrow(0, 0, Ex[0], Ey[0])

def init():
    ax.add_patch(patch)
    return patch,

def animate(t):
    ax.patches.pop()
    patch = plt.Arrow(0, 0, Ex[t], Ey[t])
    ax.add_patch(patch)

    
    return patch, 
    

anim = ani.FuncAnimation(fig, animate, frames=32,
                               init_func=init, 
                               interval=100,
                               )

plt.show()
