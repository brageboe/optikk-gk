import numpy as np

# system constants
t = 2 #5
R = 10 #40
nA = 1.0 #1.33
nL = 1.60
nW = 1.33 #1.0
y0 = 5
s0 = 60

# RAY TRANSFER MATRICES
L = np.array([[1, t],[0, 1]])   # translation matrix inside lens
R1 = np.array([[1, 0],[(nA - nL)/(R*nL), nA/nL]])  # refraction matrix 1st surface
R2 = np.array([[1, 0],[(nL - nW)/(-R*nW), nL/nW]]) # refraction matrix 2nd surface

# SYSTEM MATRIX
M = R2 @ L @ R1
print("M = ", M)
A = M[0,0]
B = M[0,1]
C = M[1,0]
D = M[1,1]

# CARDINAL POINTS AND IMAGE
r = (D - nA/nW) / C     # distance from input plane to PP1
p = D / C               # distance from input plane to F1
q = -A / C              # distance from output plane to F2
s = (1 - A) / C         # distance from output plane to PP2
v = (D - 1) / C         # distance from input plane to nodal plane N1
w = (nA / nW - A) / C   # distance from output plane to nodal plane N2
si = - (s0 * A + B) / (s0 * C + D) # distance from output plane to image
si_from_PP2 = si - s    # distance from PP2 to image
magnification = A + si * C  # maginification of image

print("CARDINAL POINTS:")
print("r =", r)
print("p =", p)
print("s =", s)
print("q =", q)
print("v =", v)
print("w =", w)
print("f1 =", p - r)
print("f2 =", q - s)
print("IMAGE POSIITON AND SIZE:")
print("Image point distance from PP2 =", si_from_PP2)
print("Height of image =", magnification * y0)
print("[All distances measured in cm]")
