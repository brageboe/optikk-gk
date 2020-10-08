#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:34:03 2020

@author: brage
"""

# COPY OF 4-24_ani.py FROM EXERCISE 6

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import matplotlib.patches as patches


# Calculate Fields
time = np.linspace(0, 2*np.pi, 32) # the product \omega * time, really

subexercise = input("Choose sub exercise (a,b,c):")
if subexercise == 'a':
    Ex = np.cos(time - np.pi/4)
    Ey = np.cos(time + np.pi/4)
elif subexercise == 'b':
    Ex = np.cos(time - np.pi/4)
    Ey = - 2 * np.sin(time)
elif subexercise == 'c':
    Ex = 0.5 * np.cos(time)
    Ey = - np.sin(time + np.pi/2)


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
patch = patches.Arrow(0, 0, Ex[0], Ey[0], width=0.5)

def init():
    ax.add_patch(patch)
    return patch,

def animate(t):
    ax.patches.pop()
    patch = plt.Arrow(0, 0, Ex[t], Ey[t], width=0.5)
    ax.add_patch(patch)

    
    return patch, 
    

anim = ani.FuncAnimation(fig, animate, frames=32,
                               init_func=init, 
                               interval=100,
                               )

plt.show()
