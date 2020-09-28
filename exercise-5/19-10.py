import numpy as np

# system constants in millimeters
d1 = 3.6 # distance from cornea to lens 1st surface
d2 = 3.6 # distance from 1st surface to 2nd surface of lens
Rf = 10
Rb = -6
Rc = 8
nA = 1.0 #1.33
nL = 1.45
nVC = 1.333 #1.0
s_object = 250

eye_unaccommodation = input("Is the eye unaccommodated? (yes/no)")
if eye_unaccommodation == "no" or eye_unaccommodation == "n" or eye_unaccommodation == "N":
    d1 = 3.2
    d2 = 4.0
    Rf = 6
    print("Assuming fully accommodated eye...")
elif eye_unaccommodation == "yes" or eye_unaccommodation == "y" or eye_unaccommodation == "Y":
    print("Using values for an unaccommodated eye...")
else:
    print("Unrecognized input. Assuming values for an unaccommodated eye...")

# RAY TRANSFER MATRICES
L1 = np.array([[1, d1],[0, 1]]) # translation matrix cornea to lens, inside VC medium
L2 = np.array([[1, d2],[0, 1]]) # translation matrix 1st lens surface to 2nd surface, inside lens medium
R1 = np.array([[1, 0],[(nA - nVC)/(Rc*nVC), nA/nVC]])  # refraction matrix air to Vitreous chamber (VC)
R2 = np.array([[1, 0],[(nVC - nL)/(Rf*nL), nVC/nL]])  # refraction matrix VC to lens
R3 = np.array([[1, 0],[(nL - nVC)/(Rb*nVC), nL/nVC]]) # refraction matrix lens to VC

# SYSTEM MATRIX
M = R3 @ L2 @ R2 @ L1 @ R1
print("\nM = ", M)
A = M[0,0]
B = M[0,1]
C = M[1,0]
D = M[1,1]

# CARDINAL POINTS AND IMAGE
r = (D - nA/nVC) / C     # distance from input plane to PP1
p = D / C               # distance from input plane to F1
q = -A / C              # distance from output plane to F2
s = (1 - A) / C         # distance from output plane to PP2
v = (D - 1) / C         # distance from input plane to nodal plane N1
w = (nA / nVC - A) / C   # distance from output plane to nodal plane N2
s_image = - (s_object * A + B) / (s_object * C + D) # distance from output plane to image
#si_from_PP2 = si - s    # distance from PP2 to image
#magnification = A + si * C  # maginification of image

print("\nCARDINAL POINTS:")
print("r =", r)
print("p =", p)
print("s =", s)
print("q =", q)
print("v =", v)
print("w =", w)
print("f1 =", p - r)
print("f2 =", q - s)
print("\nIMAGE POSITION FROM CORNEA:", s_image + 7.2)


input('Press ENTER to exit')
