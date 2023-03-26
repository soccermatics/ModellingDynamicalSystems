"""
.. _simHawkDove:

Hawk-dove dynamics
==================

The model
---------

On the previous page we saw that a model for the number of co-operators in the
Hawk-Dove game is.

.. math::
  :label: repeqsim

  \\frac{dx}{dt} = f(x) = \\frac{1}{4} x (1-x) (1 - 2x)

We start by importing the libraries we need.

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pylab import rcParams
matplotlib.font_manager.FontProperties(family='Helvetica',size=11)
rcParams['figure.figsize'] = 14/2.54, 12/2.54
from scipy import integrate


##############################################################################
# Now we define the model. This code creates a function 
# which we can use to simulate differential equation :eq:`repeqsim`. 

# Differential equation
def dXdt(X, t=0):
    # Replicator equation
    return np.array([ X[0]*(1-X[0])*(1-2*X[0])/4])                   


##############################################################################
# We solve the equations numerically and plot solution over time. 
#

def plotOverTime(ax,X):
    ax.plot(t, X, '-',color='k', label='Co-operators (x)')
    ax.plot(t, 1-X, ':',color='k', label='Defectors (x)')
    ax.legend(loc='best')
    ax.set_xlabel('Time: t')
    ax.set_ylabel('Population')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks(np.arange(0,31,step=5))
    ax.set_yticks(np.arange(0,1.01,step=0.5))
    ax.set_xlim(0,30)
    ax.set_ylim(0,1) 
    

t = np.linspace(0, 30,  1000)       # time
X0 = np.array([0.1])                # initially 10% are co-operators
X = integrate.odeint(dXdt, X0, t)   # uses a Python package to simulate the interactions
fig,ax=plt.subplots(num=1)
plotOverTime(ax,X)
plt.show()

##############################################################################
# Rate of change
# --------------
#
# In order to understand how the change in co-operators depends on the 
# current proportion of co-operators we plot equation eq:`repeqsim`
# as a function of :math:`x` as follows.

def plotChange(ax):
    xx=np.linspace(0, 30,  1000)  
    dx = np.array([dXdt([xi]) for xi in xx])
    
    ax.plot(xx ,dx, '-',color='k')
    ax.set_xlabel('Proportion co-operators: $x$')
    ax.set_ylabel('Change in co-operators: $dx/dt=f(x)$')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_yticks(np.arange(-0.05,0.051,step=0.02))
    ax.set_xticks(np.arange(0,1.01,step=0.2))
    ax.set_ylim(-0.05,0.05)   
    ax.set_xlim(0,1) 

def drawArrows(ax,dXdt):
    x = np.linspace(0.05, 1 ,6)
    y = [0]
    X , Y  = np.meshgrid(x, y)
    dX = dXdt(X) 
    dY =np.zeros(len(dX))
    ax.quiver(X, Y, dX, dY, pivot='mid', width=0.03)
    ax.plot([0,1],[0,0],'k:')

fig,ax=plt.subplots(num=1)
plotChange(ax)
drawArrows(ax,dXdt)
plt.show()

##############################################################################
# Steady states
# -------------
#
# The steady states are the points where :math:`f(x_*)=0`. We can find them 
# numerically using Python as follows.
# 

from scipy.optimize import fsolve
x_s=np.zeros(3)
x_initial=[0.1, 0.74, 0.9]
for i,x_i in enumerate(x_initial):
    x_s[i]=fsolve(dXdt, (x_i))
    print('Starting with value %.2f gives steady state %.2f'%(x_i,x_s[i]))
    
##############################################################################
# The solution we find depends on the starting position. Here
# we chose values we knew were nearby in order to be sure that we found them. 
#
# Stability
# ---------
#
# On the previous page, we saw that the derivative of :math:`f(x)` (equation :eq:`repeqsim`) 
# with respect to :math:`x` is
# 
# .. math:: 
#  
#   f'(x) = \frac{1}{4} \left((1-2x)^2 - 2x(1-x) \right)
#
#
# We can evaluate the steady states we found using this derivative to determine their stability.

def dfdx(x):
    # Replicator equation
    return 1/4*((1-2*x) - 2*x*(1-x))
 
for x in x_s:
    dfx=dfdx(x)
    if (dfx>0):
        print("Steady state %.2f is unstable (f'(x)= %.4f)"%(x,dfx))
    elif (dfx<0):
        print("Steady state %.2f is stable (f'(x)= %.4f)"%(x,dfx))
        
              
    


