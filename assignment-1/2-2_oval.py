import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Oval:
xOval = np.arange(20., 30., 0.1)
yOval = np.sqrt( ((-70 + np.sqrt(675*xOval + 900)) / 2.5)**2 - xOval**2 )

# Circle:
radius = 10
alpha = np.arange(0., np.pi/2, 0.1)
xCircle = 30 - radius*np.cos(alpha)
yCircle = radius*np.sin(alpha)

# plot limiters
xmin = 0
xmax = 30

# figure
plt.plot(xOval, yOval, 'g', xOval, -yOval, 'g')
plt.plot(xCircle, yCircle, 'b', xCircle, -yCircle, 'b')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([xmin-1, xmax+1])
plt.ylim([-radius-1,radius+1])
plt.scatter(0,0, color='k')
plt.scatter(30,0, color='k')

# legend
oval = mpatches.Patch(color='g', label='Oval')
circle = mpatches.Patch(color='b', label='Circle')
plt.legend(handles=[oval, circle])


