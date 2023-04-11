"""
.. _epidemic:

The SEIR model
=============
  
In the SEIR model, there is an additional class for people exposed (but not yet infective). The equations 
are now,

  .. math::

     \begin{aligned}
     \frac{dS}{dt} & = - \beta S I \\
     \frac{dE}{dt} & = \beta S I - \delta E\\
     \frac{dI}{dt} & = \delta E -  \gamma I \\
     \frac{dR}{dt} & =  \gamma I 
     \end{aligned}

Simulating the model
--------------------

  Assume that :math:`\gamma=1/7` and :math:`\beta=1/5`. Write code to draw a
  graph of :math:`I(t)` as a function of time (:math:`t`) for the cases in which
  (on average) a person is exposed for 1, 5 and respectively 9 days before they are infected.
  Assume that :math:`S(0)=999/1000`, :math:`E(0)=0`
  and :math:`I(0)=1/1000`. 
"""


import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib
rcParams['figure.figsize'] = 12/2.54, 6/2.54
matplotlib.font_manager.FontProperties(family='Helvetica',size=11)
from scipy import integrate

# Parameter values
beta = 1/2
gamma = 1/7
# Set delta here

# Differential equation
def dXdt(X, t=0):
    # Set up the equations here
    return np.array([  ])                      



def plotEpidemicOverTime(ax,S,I,R):

    #Add your code here.
    ax.legend(loc='best')
    ax.set_xlabel('Time: t')
    ax.set_ylabel('Population')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks(np.arange(0,100,step=10))
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
# Does :math:`\delta` have a large effect on the final number of people infected? 
# Add a text box and explain your answer below.





############################################################################## 
# Simulating the model
# --------------------
#
# The helath authority decide to introduce restrictions when 1% of the population
# are infected. With restrictions :math:`\beta=1/15` and without them :math:`\beta=1/5`. 
# Investigate the consequences of that decision for various values of :math:`\delta`, i.e. 
# simulate the spread,with :math:`\beta=1/5` until :math:`I(t)=0.01` and then with :math:`\beta=1/15` for 
# varying :math:`\delta`. Make plots of :math:`R(t)` for different :math:`\delta` values and describe (in words) how
# :math:`\delta` affects the outcome.
#
# *Hint*: The following command will help you find then :math:`I(t) \geq 0.01`

I = np.array([0.001, 0.0025, 0.005, 0.01, 0.02, 0.05])
ind = np.nonzero(I>=0.01);
onepercent=ind[0];
print('Infectives became 1 percent at time %d'% onepercent)


