"""
.. _doublingmap:

El Farol
========
"""

import numpy as np

##############################################################################
# Alex story
# ---------------
#
# In Alex story we take the attendance at the bar the previous week, :math:´x_t'
# double it. If ´2x_t \leq 50' then the number of visitors the next week is 
#
# .. math::
#   
#   x_{t+1} =2x_t
#
# On the other hand, if :math:´2x_t > 50' then the number of visitors next week is
#
# .. math::
#   
#   x_{t+1} = 2(100 - x_t)
# 
# Let's implement this in Python 

import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib
rcParams['figure.figsize'] = 12/2.54, 6/2.54
matplotlib.font_manager.FontProperties(family='Helvetica',size=11)


def tentmap(x0,n):
    xs=np.zeros(n+1)
    xs[0]=x0
    for k in range(n):
        xs[k+1]= 2* min(xs[k],100-xs[k])
    return(xs)

x0=20
print('One iteration:' )
print(tentmap(x0,1))
print('Two iterations:' )
print(tentmap(x0,2))
print('Three iterations:' )
print(tentmap(x0,3))

##############################################################################
# 
# If we keep iterating, we get

print('Eleven iterations:' )
print(tentmap(x0,11))


##############################################################################
# Chocolate cake
# --------------
#
# In Richard chocolate cake story we 
# 


print('Starting with 13:' )
print(tentmap(13,7))
print('Starting with 14:' )
print(tentmap(14,7))


##############################################################################
#
# Let's make the difference only 0.1
# 

def formatFigure(ax,n):
    ax.set_ylabel('Number')
    ax.set_xlabel('Step')
    ax.set_ylim((0,100))
    ax.set_xlim((0,n))
    ax.set_xticks(range(0,n+1,2))
    ax.set_yticks(range(0,101,20))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

n=20

fig,ax=plt.subplots(num=1)
ax.plot(tentmap(14.1,n), color='black')
ax.plot(tentmap(14.2,n), color='black',linestyle=':')
formatFigure(ax,n)
plt.show()


##############################################################################
#
# And now let's make the difference only 0.001
#
n=30

fig,ax=plt.subplots(num=1)
ax.plot(tentmap(14.001,n), color='black')
ax.plot(tentmap(14.002,n), color='black',linestyle=':')
formatFigure(ax,n)
plt.show()




##############################################################################
# Cobweb diagrams
# --------------
#

n = 50 

xs = tentmap(14.1,50)
xp = xs[1]

rcParams['figure.figsize'] = 12/2.54, 12/2.54
fig,ax=plt.subplots(num=1)

for x in xs[2:]:
    
    ax.plot([xp, xp],[xp, x],color='k',linewidth=0.5)
    ax.plot([xp, x],[x, x],color='k',linewidth=0.5)
    xp = x


ax.plot([-0.5, 105.5],[-0.5, 105.5],linestyle=':',color='k',linewidth=1)
ax.plot([100, 50],[0, 100],color='k',linewidth=1)
ax.plot([0, 100/2],[0, 100],color='k',linewidth=1)
ax.set_xlabel('Previous number')
ax.set_ylabel('Next number')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks(np.arange(0,101,step=20))
ax.set_yticks(np.arange(0,101,step=20))
ax.set_xlim(0,101)
ax.set_ylim(0,101) 
plt.show()

