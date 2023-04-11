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



  Assume that :math:`\gamma=1/7` and :math:`\beta=1/5`. Write code to draw a
  graph of :math:`I(t)` as a function of time (:math:`t`) for the cases in which
  (on average) a person is exposed for 1, 5 and respectively 9 days before they are infected.
  Assume that :math:`S(0)=999/1000`, :math:`E(0)=0`
  and :math:`I(0)=1/1000`. 
"""

# Parameter values
beta = 1/2
gamma = 1/7
delta =

# Differential equation
def dXdt(X, t=0):
    # Growth rate 
    return np.array([  ])                      



def plotEpidemicOverTime(ax,S,I,R):

    #Add code here.
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
# Explain your answer.



| Hälsomyndigheten bestämmer att införa restriktioner först när 1% av
  befolkning är infekterad. Med restriktioner är :math:`\beta=1/15` men
  utan restriktioner är :math:`\beta=1/5`. Undersök konsekvenser av
  detta beslut för olika värden på :math:`\delta`, dvs simulera
  spridning först under antagandet att :math:`\beta=1/5` och när
  :math:`I(0)=0.01` ändra smittsamheten till :math:`\beta=1/15`. Skissa
  :math:`R(t)` för olika :math:`\delta`-värden och beskriv hur
  :math:`\delta` påverkar utfallet.
| **Tips:** Använd

::

   ind = find(I>=0.01);
   onepercent=ind(1);

för att hitta tidpunkten, :math:`t`, då :math:`I(t)=0.01`.
