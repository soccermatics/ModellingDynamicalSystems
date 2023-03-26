"""
.. _chaosbutterfly:

The butterfly effect
====================

FROM THE BOOK

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pylab import rcParams
matplotlib.font_manager.FontProperties(family='Helvetica',size=11)

from scipy import integrate
from mpl_toolkits import mplot3d


##############################################################################
# The Lorenz equations
# --------------------
#
# The differential equations propsed by Lorenz are
#
# .. math::
#
#       \\frac{dX}{dt} &= s(Y-X) \\
#       \\frac{dY}{dt} &= rX - Y - XZ \\
#       \\frac{dZ}{dt} &= XY - bZ 
#    
# There are three parameter values, which are set to $s=10$, $r=28$ 
# and $b=8/3$ to create the butterfly (th Lorenz attractor). 
#
# Let's first define a function which gives the derivatives at each point

def lorenz(XYZ,t=0):
    
    
    dXdt = s*(XYZ[1] - XYZ[0])                  # X 
    dYdt = r*XYZ[0] - XYZ[1] - XYZ[0]*XYZ[2]    # Y 
    dZdt = XYZ[0]*XYZ[1] - b*XYZ[2]             # Z 
    
    return np.array([dXdt, dYdt, dZdt])


# Parameter values
s=10
r=28
b=8/3

##############################################################################
# Now we solve the equations numerically

endtime=300
dt = 0.01 

t = np.linspace(0,endtime, int(endtime/dt))               # time
XYZ0 = np.array([0.3, 1.2, 5.05])          # initial conditions
XYZ = integrate.odeint(lorenz, XYZ0, t)

start=int(200/dt)
finish=int(start+40/dt)

rcParams['figure.figsize'] = 14/2.54, 14/2.54
ax=plt.subplot(projection='3d')
ax.set_xticks(np.arange(-20,21,step=10))
ax.set_yticks(np.arange(-20,21,step=10))
ax.set_zticks(np.arange(0,40,step=10))
ax.yaxis.labelpad=10
#ax.plot( [mean1, mean1], [-1, 10], linestyle='dashed', color='black')
#ax.text(-20,-20,50,'(a)') 
ax.plot3D(XYZ[start:finish,0], XYZ[start:finish,1], XYZ[start:finish,2], lw=1,color='k')
ax.set_xlabel("Strength of breeze ($X$)")
ax.set_ylabel("Temperature difference \n between currents ($Y$)")
ax.set_zlabel("Land/air temperature \n distortion ($Z$) ")

# Get rid of colored axes planes
# First remove fill
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Now set color to white (or whatever is "invisible")
ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')

ax.set_xlim(-21,21)
ax.set_zlim(0,40) 
ax.set_ylim(-21,21)


plt.show()



##############################################################################
# Plot through time



rcParams['figure.figsize'] = 14/2.54, 7/2.54

finish=int(start+20/dt)

fig,ax=plt.subplots(num=1)
ax.plot(XYZ[start:finish,0], color='black')
ax.plot(XYZ[start:finish,1], color='green')
ax.plot(XYZ[start:finish,2], color='red')
plt.show()
fig.savefig('lorenz_z.pdf', dpi=None, bbox_inches="tight")


from scipy.signal import argrelextrema


##############################################################################
# Find local maxima.

rcParams['figure.figsize'] = 14/2.54, 7/2.54

# for local maxima
zm= XYZ[:,2]
maxz=argrelextrema(zm, np.greater)
zm=zm[maxz]

zm=zm[20:]
fig,ax=plt.subplots(num=1)
ax.plot(np.arange(len(zm)),zm, color='black')
fig.savefig('lorenz_max.pdf', dpi=None, bbox_inches="tight")

matplotlib.font_manager.FontProperties(family='Helvetica',size=11)

ax.set_ylabel('Maximum value of $Z$')
ax.set_xlabel('Iteration round the butterfly')
ax.set_ylim((27,52))
ax.set_xlim((0,50))
ax.set_xticks(range(0,60,10))
ax.set_yticks(range(30,60,10))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()



##############################################################################
# Now make a map of maxima from one time to the next

rcParams['figure.figsize'] = 4/2.54, 4/2.54
fig,ax=plt.subplots(num=1)
ax.plot(zm[:-1],zm[1:],linestyle='none',marker='.',color='k')
ax.text(29,48,'(c)')
ax.set_ylabel('Next Maximum of $Z$')
ax.set_xlabel('Previous Maximum of $Z$')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks(np.arange(20,51,step=10))
ax.set_yticks(np.arange(20,51,step=10))
ax.set_xlim(27,52)
ax.set_ylim(27,52) 
fig.savefig('lorenz_map.pdf', dpi=None, bbox_inches="tight")


