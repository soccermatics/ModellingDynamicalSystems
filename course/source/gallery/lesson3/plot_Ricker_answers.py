"""
.. _logisticmap:

Ricker map
==========

**Now you should study a model yourself!** Download the page as a 
Python notebook and fill in the missing code according to the instructions.


The model
---------

The Ricker map is another discrete model of growth and regulatory feedback. 
It describes a variable :math:`x(k)` which changes over discrete times steps.
The variable might be, for example, size of an insect population.  

We write the model as 

.. math::
  
  x(k+1)) = r x(k)\exp(-x(k))

The parameter :math:`r` determines growth rate. Investigate the dynamics 
of this model. Find and plot values of :math:`r` where the population is stable, where 
it oscilLates with period 2, where it oscilLates with period 4 and where it oscilLates 
with period 3. 

"""


import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib
rcParams['figure.figsize'] = 12/2.54, 6/2.54
matplotlib.font_manager.FontProperties(family='Helvetica',size=11)

def logisticmap(x0,r,n):
    xs=np.zeros(n+1)
    xs[0]=x0
    for k in range(n):
        xs[k+1]= r*xs[k]*np.exp(-xs[k])
    return(xs)

def formatFigure(ax,n):
    ax.set_ylabel('Number: $k$')
    ax.set_xlabel('Step: $x(k)$')
    ax.set_ylim((0,10))
    ax.set_xlim((0,n))
    ax.set_xticks(np.arange(0,n+1,n/10))
    ax.set_yticks(np.arange(0,10.01,1))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

n=20
x0=0.2

##############################################################################
# Answer
# ------
#
# Stable is given by r=3

n=50

fig,ax=plt.subplots(num=1)
ax.plot(logisticmap(x0,3,n), color='black')
formatFigure(ax,n)
plt.show()


##############################################################################
# Periodic by r = 10

fig,ax=plt.subplots(num=1)
ax.plot(logisticmap(x0,10,n), color='black')
formatFigure(ax,n)
plt.show()


##############################################################################
# Period 4 by r =13

fig,ax=plt.subplots(num=1)
ax.plot(logisticmap(x0,13,n), color='black')
formatFigure(ax,n)
plt.show()


##############################################################################
# And period 3 by r=23

fig,ax=plt.subplots(num=1)
ax.plot(logisticmap(x0,23,n), color='black')
formatFigure(ax,n)
plt.show()


##############################################################################
# Cobweb diagrams
# --------------
#
# Make cobweb diagrams for the values you found.

n = 50 

r_vals=[3, 10, 13, 23]


rcParams['figure.figsize'] = 12/2.54, 12/2.54
fig,ax=plt.subplots(2,2)


for i,r in enumerate(r_vals):
    xs = logisticmap(0.1,r,50)
    xp = xs[0]
    ax[int(i/2)][np.mod(i,2)].plot([xp, xp],[0, xp],color='k',linewidth=0.5)
    for x in xs:
        ax[int(i/2)][np.mod(i,2)].plot([xp, xp],[xp, x],color='k',linewidth=0.5)
        ax[int(i/2)][np.mod(i,2)].plot([xp, x],[x, x],color='k',linewidth=0.5)
        xp = x
    
    xr=np.arange(0,20,0.001)
    fxr=r*xr*np.exp(-xr)
    ax[int(i/2)][np.mod(i,2)].plot([-0.5, 105.5],[-0.5, 105.5],linestyle=':',color='k',linewidth=1)
    ax[int(i/2)][np.mod(i,2)].plot(xr,fxr,color='r',linewidth=1)
    ax[int(i/2)][np.mod(i,2)].set_xlabel('Previous number: $x(k)$')
    ax[int(i/2)][np.mod(i,2)].set_ylabel('Next number: $x(k+1)$')
    ax[int(i/2)][np.mod(i,2)].spines['top'].set_visible(False)
    ax[int(i/2)][np.mod(i,2)].spines['right'].set_visible(False)
    ax[int(i/2)][np.mod(i,2)].set_xticks(np.arange(0,10.01,step=1))
    ax[int(i/2)][np.mod(i,2)].set_yticks(np.arange(0,10.01,step=1))
    ax[int(i/2)][np.mod(i,2)].set_xlim(0,10.01)
    ax[int(i/2)][np.mod(i,2)].set_ylim(0,10.01) 
    ax[int(i/2)][np.mod(i,2)].text(1.0,9.0,'r=%.1f'%r)
    
plt.show()



##############################################################################
# Sensitivity to initial conditions
# ---------------------------------
#
# Find a value of :math:`r` where the Ricker map exhibits sensitivity to initial values. 
# Show that even for an intitial difference of 0.0001 the resul of 20 iterations of the map
# gives a large difference.
# 

n=30
r=26

fig,ax=plt.subplots(num=1)
ax.plot(logisticmap(0.1000,r,n), color='black')
ax.plot(logisticmap(0.1001,r,n), color='red')
formatFigure(ax,n)
plt.show()
