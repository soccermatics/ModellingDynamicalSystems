"""
.. _morethanthesum:

More than the sum of its parts
==============================

FROM BOOK

The model
---------
 
In terms of differential equations, the rate of change of susceptible individuals is

.. math::
   :label: susc
 
   \\frac{dL}{dt} = \\underbrace{-b L F^2 }_{\mbox{L} + \mbox{2F} \\xrightarrow{b} \mbox{3F}}

and the rate of change of infectives is 

.. math::
   :label: infect
 
   \\frac{dF}{dt} = \\underbrace{-b L F^2 }_{\mbox{L} + \mbox{2F} \\xrightarrow{b} \mbox{3F}} - \\underbrace{c F }_{\mbox{F} \\xrightarrow{c} \mbox{R}} 

The constant :math:`b` is the rate of contact between people and :math:`c` is the rate of recovery.
We can also write down an equation for recovery as follows,

.. math::
   :label: recover
 
   \\frac{dR}{dt} = \\underbrace{c F }_{\mbox{F} \\xrightarrow{c} \mbox{R}} 

In this model :math:`L`, :math:`F` and :math:`R` are proportions of the population. Summing them up gives :math:`L+F+R=1`, since 
everyone in the popultaion is either susceptible, infective or recovered.

Let's now solve these equations numerically. We start by importing the libraries we need from Python.



"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pylab import rcParams
matplotlib.font_manager.FontProperties(family='Helvetica',size=11)
rcParams['figure.figsize'] = 14/2.54, 7/2.54
from scipy import integrate


b=8
c = 0.4

def dXdt(X, t=0):
   return np.array([  - b*X[0]*X[1]*X[1] ,           #LookingX[0] is L
                      + b*X[0]*X[1]*X[1]  - c*X[1] , #Found Food X[1] is F
                        c*X[1]])                     #Resting X[2] is R

def plotOverTime(ax,F,linetype):
    ax.plot(t, F  , linetype,color='k')
    ax.set_xlabel('Time: t')
    ax.set_ylabel('Found Food: F')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks(np.arange(0,20,step=2))
    ax.set_yticks(np.arange(0,1.01,step=0.5))
    ax.set_xlim(0,20)
    ax.set_ylim(0,1) 
    
t = np.linspace(0, 20,  1000)         # time
X0 = np.array([0.9, 0.1,0.0000])      # initially 10% have found food
X = integrate.odeint(dXdt, X0, t)     # uses a Python package to simulate the interactions
L, F, R = X.T
fig,ax=plt.subplots(1)
plotOverTime(ax,F,'-')
plt.show()

##############################################################################
# We can find
# the equilibria where the rate at which people become infected equals the 
# rate at which they recover by solving
# 
# .. math::
# 
#   \frac{dI}{dt} = b S I^2 - c I = 0  
#
# This occurs either when :math:`I=0` (no ants have found the food) or 
# when 
#
# .. math::
# 
#   S = \frac{c}{bI} 
# 


def plotPhasePlane(ax,L,F,linetype):
    ax.plot(L, F, linetype,color='k')
    ax.set_xlabel('Looking: S')
    ax.set_ylabel('Found Food: F')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks(np.arange(0,1.01,step=0.5))
    ax.set_yticks(np.arange(0,1.01,step=0.5))
    ax.set_ylim(-0.05,1)   
    ax.set_xlim(-0.05,1) 

def drawArrows(ax,dXdt):
    x = np.linspace(0.05, 1 ,6)
    y = np.linspace(0.05, 1, 6)
    X , Y  = np.meshgrid(x, y)
    dX, dY, dZ = dXdt([X, Y,1-X-Y]) 
    #Make in to unit vectors. 
    M = np.hypot(dX,dY)
    dX = dX/M
    dY = dY/M
    ax.quiver(X, Y, dX, dY, pivot='mid')


F_equilibrium = np.linspace(0, 1,  1000)               
L_equilibrium = c/(b*F_equilibrium)     

fig,ax=plt.subplots(1,2)
plotOverTime(ax[0],F,'-')
ax[1].plot(L_equilibrium,F_equilibrium,linestyle=':',color='k')
plotPhasePlane(ax[1],L,F,'-')
drawArrows(ax[1],dXdt)
plt.show()




##############################################################################
# Now lets make b smaller
#
#


b=3.5
c = 0.4

fig,ax=plt.subplots(1,2)

t = np.linspace(0, 20,  1000)         # time
X0 = np.array([0.9, 0.1,0.0000])      # initially 10% have found food
X = integrate.odeint(dXdt, X0, t)     # uses a Python package to simulate the interactions
L, F, R = X.T
plotOverTime(ax[0],F,'-')
plotPhasePlane(ax[1],L,F,'-')


t = np.linspace(0, 20,  1000)         # time
X0 = np.array([0.75, 0.25,0.0000])      # initially 25% have found food
X = integrate.odeint(dXdt, X0, t)     # uses a Python package to simulate the interactions
L, F, R = X.T
plotOverTime(ax[0],F,'--')
plotPhasePlane(ax[1],L,F,'--')

F_equilibrium = np.linspace(0, 1,  1000)               
L_equilibrium = c/(b*F_equilibrium)    
ax[1].plot(L_equilibrium,F_equilibrium,linestyle=':',color='k')
drawArrows(ax[1],dXdt)
 

plt.show()


##############################################################################
# And b smaller still
#
#


b=1
c = 0.4

fig,ax=plt.subplots(1,2)

t = np.linspace(0, 20,  1000)         # time
X0 = np.array([0.9, 0.1,0.0000])      # initially 10% have found food
X = integrate.odeint(dXdt, X0, t)     # uses a Python package to simulate the interactions
L, F, R = X.T
plotOverTime(ax[0],F,'-')
plotPhasePlane(ax[1],L,F,'-')


t = np.linspace(0, 20,  1000)         # time
X0 = np.array([0.75, 0.25,0.0000])      # initially 25% have found food
X = integrate.odeint(dXdt, X0, t)     # uses a Python package to simulate the interactions
L, F, R = X.T
plotOverTime(ax[0],F,'--')
plotPhasePlane(ax[1],L,F,'--')


t = np.linspace(0, 20,  1000)         # time
X0 = np.array([0.25, 0.75,0.0000])      # initially 25% have found food
X = integrate.odeint(dXdt, X0, t)     # uses a Python package to simulate the interactions
L, F, R = X.T
plotOverTime(ax[0],F,'-.')
plotPhasePlane(ax[1],L,F,'-.')

F_equilibrium = np.linspace(0, 1,  1000)               
L_equilibrium = c/(b*F_equilibrium)    
ax[1].plot(L_equilibrium,F_equilibrium,linestyle=':',color='k')
drawArrows(ax[1],dXdt)
 

plt.show()


