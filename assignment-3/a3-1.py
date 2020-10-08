#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:16:41 2020

@author: brage
"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch): #https://stackoverflow.com/questions/22867620/putting-arrowheads-on-vectors-in-matplotlibs-3d-plot
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


k_unit = [np.sqrt(5) / 3, 2 / 3, 0]
E0_unit = [-2 / 3, np.sqrt(5) / 3, 0]
B0_unit = [0, 0 , 1]

############
## FIGURE ##
############

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.grid(True, which='both', axis='both') # unnecessary?

kplot = Arrow3D([0, k_unit[0]], [0, k_unit[1]], [0, k_unit[2]], mutation_scale=20, 
                lw=3, arrowstyle="-|>", color="r", label="k_unit")
E0plot = Arrow3D([0, E0_unit[0]], [0, E0_unit[1]], [0, E0_unit[2]], mutation_scale=20, 
                lw=3, arrowstyle="-|>", color="b", label="E0_unit")
B0plot = Arrow3D([0, B0_unit[0]], [0, B0_unit[1]], [0, B0_unit[2]], mutation_scale=20, 
                lw=3, arrowstyle="-|>", color="g", label="B0_unit")

ax.add_artist(kplot)
ax.add_artist(E0plot)
ax.add_artist(B0plot)


ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_xlim(np.min([0, k_unit[0], E0_unit[0]]), np.max([0, k_unit[0], E0_unit[0]]))
ax.set_ylim(np.min([0, k_unit[1], E0_unit[1]]), np.max([0, k_unit[1], E0_unit[1]]))
fig.legend(handles=[kplot, E0plot, B0plot])

plt.draw()
plt.show()