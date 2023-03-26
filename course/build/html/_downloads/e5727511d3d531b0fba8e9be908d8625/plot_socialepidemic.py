"""
.. _socialepidemic:

The Social Epidemic
===================

FROM BOOK

The SIR model
-------------
  
In terms of differential equations, the rate of change of susceptible individuals is

.. math::
   :label: susc
 
   \\frac{dS}{dt} = \\underbrace{-b S I }_{\mbox{I} + \mbox{S} \\xrightarrow{b} 2 \mbox{I}}

and the rate of change of infectives is 

.. math::
   :label: infect
 
   \\frac{dI}{dt} = \\underbrace{b S I }_{\mbox{I} + \mbox{S} \\xrightarrow{b} 2 \mbox{I}} - \\underbrace{c I }_{\mbox{I} \\xrightarrow{c} \mbox{R}} 

The constant :math:`b` is the rate of contact between people and :math:`c` is the rate of recovery.
We can also write down an equation for recovery as follows,

.. math::
   :label: recover
 
   \\frac{dR}{dt} = \\underbrace{c I }_{\mbox{I} \\xrightarrow{c} \mbox{R}} 

In this model :math:`S`, :math:`I` and :math:`R` are proportions of the population. Summing them up gives :math:`S+I+R=1`, since 
everyone in the popultaion is either susceptible, infective or recovered.

Let's now solve these equations numerically. We start by importing the libraries we need from Python.

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pylab import rcParams
matplotlib.font_manager.FontProperties(family='Helvetica',size=11)
rcParams['figure.figsize'] = 9/2.54, 9/2.54
from scipy import integrate


##############################################################################
# Now we define the model. This code creates a function 
# which we can use to simulate differential equations :eq:`susc` and :eq:`infect`. 
# We also define the parameter values. You can change these to see how
# changes to the paramaters leads to changes in the outcome of the model. 


# Parameter values
b = 3.5
c = 1

# Differential equation
def dXdt(X, t=0):
    # Growth rate of fox and rabbit populations.
    return np.array([  - b*X[0]*X[1] ,      #Susceptible X[0] is S
                      b*X[0]*X[1]   - c*X[1],      #Infectives X[1] is I
                      c*X[1]])                     #Recovered X[2] is R


##############################################################################
# We solve the equations numerically and plot solution over time. 

def plotEpidemicOverTime(ax,S,I,R):

    ax.plot(t, S, '-',color='k', label='Suceptible (S)')
    ax.plot(t, I  , '--',color='k', label='Infectives (I)')
    ax.plot(t, R  , '--',color='k', label='Recovered (R)')
    ax.legend(loc='best')
    ax.set_xlabel('Time: t')
    ax.set_ylabel('Population')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks(np.arange(0,20,step=2))
    ax.set_yticks(np.arange(0,1.01,step=0.5))
    ax.set_xlim(0,20)
    ax.set_ylim(0,1) 
    

t = np.linspace(0, 20,  1000)               # time
X0 = np.array([0.9999, 0.0001,0.0000])      # initially 99.99% are uninfected
X = integrate.odeint(dXdt, X0, t)           # uses a Python package to simulate the interactions
S, I, R = X.T
fig,ax=plt.subplots(num=1)
plotEpidemicOverTime(ax,S,I,R)
plt.show()

##############################################################################
# As with the  :ref:`precator prey model<rabbitsandfoxes>` we can find
# the equilibria where the rate at which people become infected equals the 
# rate at which they recover by solving
# 
# .. math::
# 
#   \\frac{dI}{dt} = b S I - c I =0  
#
# This occurs either when :math:`I=0` (no-one has the disease) or 
# when :math:`S=c/b`. We can now plot these equilibrium on the phase plane
# 

def plotPhasePlane(ax,S,I):
    ax.plot(S, I, '-',color='k')
    ax.set_xlabel('Susceptibles: S')
    ax.set_ylabel('Infectives: I')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks(np.arange(0,1.01,step=0.5))
    ax.set_yticks(np.arange(0,1.01,step=0.5))
    ax.set_ylim(0,1)   
    ax.set_xlim(0,1) 

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

fig,ax=plt.subplots(num=1)
ax.plot([c/b,c/b],[-100,100],linestyle=':',color='k')
plotPhasePlane(ax,S,I)
drawArrows(ax,dXdt)
plt.show()


##############################################################################
#
# Social recovery
# ---------------
#
# FROM BOOK
#
# 
# In terms of differential equations, the rate of change of susceptible individuals remains the same as before
# .. math::
#    :label: susc
#
#    \\frac{dS}{dt} = \\underbrace{-b S I }_{\mbox{I} + \mbox{S} \\xrightarrow{b} 2 \mbox{I}}
#
# but the rate of change of infectives is now
#
# .. math::
#    :label: infect
# 
#    \\frac{dI}{dt} = \\underbrace{b S I }_{\mbox{I} + \mbox{S} \\xrightarrow{b} 2 \mbox{I}} - \\underbrace{c I }_{\mbox{I} \\xrightarrow{c} \mbox{R}} - \\underbrace{d I R }_{\mbox{I} + \mbox{R}  \\xrightarrow{d} 2 \mbox{R}} 
#
# The constant :math:`b` is the rate of contact between people and :math:`c` is the rate of contact between infectives and recovered individuals.
# We can also write down an equation for recovery as follows,
#
# .. math::
#    :label: recover
# 
#    \\frac{dR}{dt} = \\underbrace{c I }_{\mbox{I} \\xrightarrow{c} \mbox{R}} + \\underbrace{d I R }_{\mbox{I} + \mbox{R}  \\xrightarrow{d} 2 \mbox{R}} 
#
# In Python these equations are written as follows.

# Parameter values
b = 3.5
c = 1
d = 1

# Differential equation
def dXdt(X, t=0):
    # Growth rate of fox and rabbit populations.
    return np.array([  - b*X[0]*X[1] ,      #Susceptible X[0] is S
                      b*X[0]*X[1]   - c*X[1] - d*X[1]*X[2],      #Infectives X[1] is I
                      c*X[1] + d*X[1]*X[2]])                     #Recovered X[2] is R

t = np.linspace(0, 20,  1000)               # time
X0 = np.array([0.9999, 0.0001,0.0000])      # initially 99.99% are uninfected
X = integrate.odeint(dXdt, X0, t)           # uses a Python package to simulate the interactions
S, I, R = X.T
fig,ax=plt.subplots(num=1)
plotEpidemicOverTime(ax,S,I,R)
plt.show()


##############################################################################
# Again, we can find the equilibria where the rate at which people become infected equals the 
# rate at which they recover by solving
# 
# .. math::
# 
#    \\frac{dI}{dt} = b S I - c I - d I (1- S -I) =0  
#
# This occurs either when :math:`I=0` (no-one has the disease) or 
#
# when 
#
# .. math::
# 
#    b S I = c I + d I - d S I - dI^2 
#
#
# or, equivalently,
#
# .. math::
# 
#    (b + d) SI = (c+d) I  - d I^2
#
# or
# .. math::
# 
#    S = \\frac{c+d}{b+d} - \\frac{d}{b+d} I
#
# We can now plot these equilibrium on the phase plane
# 

I_equilibrium = np.linspace(0, 1,  1000)               
S_equilibrium = (c+d)/(b+d) - (d/(b+d))*I_equilibrium     

fig,ax=plt.subplots(num=1)
ax.plot(S_equilibrium,I_equilibrium,linestyle=':',color='k')
plotPhasePlane(ax,S,I)

X0 = np.array([0.6999, 0.0001,0.3])      # initially 99.99% are uninfected
X = integrate.odeint(dXdt, X0, t)           # uses a Python package to simulate the interactions
S, I, R = X.T
plotPhasePlane(ax,S,I)

drawArrows(ax,dXdt)

plt.show()


##############################################################################
#
# Examples
# --------
#
# Applause
# Other examples