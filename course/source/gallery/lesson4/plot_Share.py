"""
Share prices
============

We now use our function to calulate a covariance function for H&M share 
prices.

"""

##############################################################################
# 
#

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pylab import rcParams
matplotlib.font_manager.FontProperties(family='Helvetica',size=11)
rcParams['figure.figsize'] = 14/2.54, 14/2.54
import pandas as pd



def R_theoretical(a_vals,maxtau,sigma=1):
    R = np.zeros(maxtau)
    for tau in range(maxtau):
        R[tau] = np.power(-a_vals[0],tau)* (np.power(sigma,2)/(1-np.power(a_vals[0],2)))

    return R




def plotOverTime(ax, w):
    n=len(w)
    t=np.arange(n)
    ax.plot(t,w, '-',color='k')
    ax.set_xlabel('Time: t')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks(np.arange(0,n,step=n/5))
    ax.set_yticks(np.arange(-n,n+1,step=10))
    ax.set_xlim(0,n)
    ax.set_ylim(-2*np.sqrt(n),2*np.sqrt(n)) 

share_prices=pd.read_csv('../data/HandM.csv')
w = share_prices['Average price']
w=np.array(w.dropna())
fig,ax=plt.subplots(1)


w=w-np.mean(w)
plotOverTime(ax, w)
ax.set_ylim(-10,10) 
plt.show()

fig,ax=plt.subplots(1)
R=R_empirical(w,maxtau=200)
plotOverTime(ax, R)


plt.show()














