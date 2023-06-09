
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "gallery/lesson1/plot_staghuntsim_exercise.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_gallery_lesson1_plot_staghuntsim_exercise.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_gallery_lesson1_plot_staghuntsim_exercise.py:


.. _simHawkDove:

The stag hunt
=============

**Now you should study a model yourself!** Download the page as a 
Python notebook and fill in the missing code according to the instructions.


The model
---------

The stag hunt is modelled using the following payoff matrix. The dilemna is whether 
an individual should go hunting for a stag together with the group 
(which involves getting up early and driving to a desolate meeting place 
where your partner may of may not be wating for you) or hunt alone 
(which allows you to have a lie-in but means you only catch a rabbit). 
The payoffs are as follows:

=================== ============= ==============
individual/partner  Group (C)      Self (D)
=================== ============= ==============
Group (C)           1             :math:`S=-1/4`
Self (D)            :math:`T=1/2` 0
=================== ============= ==============

Write a replicator equation for this model. Start by finding the fitness of C and D. 
Then work out the average fitness.From there you can write down the replicator equation.

.. math::
  :label: stagsim

  \frac{dx}{dt} = f(x) = ....

Use it to define the equation below.

.. GENERATED FROM PYTHON SOURCE LINES 39-54

.. code-block:: default


    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib
    from pylab import rcParams
    matplotlib.font_manager.FontProperties(family='Helvetica',size=11)
    rcParams['figure.figsize'] = 14/2.54, 12/2.54
    from scipy import integrate 

    # Differential equation
    def dXdt(X, t=0):
        # Replicator equation - This is just a place holder for now 
        return np.array([X[0]])                   









.. GENERATED FROM PYTHON SOURCE LINES 55-65

Simulation
----------
Now solve the equations numerically and plot solution over time.
Investigate how the initial numbers of co-operators 
affects whether co-operation increases or 
decreases in the population.

Make two different plots using the *plotOverTime* function: 
one in which eventually everyone co-operates, another in which 
eventually everyone defects.

.. GENERATED FROM PYTHON SOURCE LINES 65-80

.. code-block:: default


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
    








.. GENERATED FROM PYTHON SOURCE LINES 81-87

Rate of change
--------------

In order to understand how the change in co-operators depends on the 
current proportion of co-operators we plot equation eq:`repeqsim`
as a function of :math:`x` as follows.

.. GENERATED FROM PYTHON SOURCE LINES 87-116

.. code-block:: default


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




.. image-sg:: /gallery/lesson1/images/sphx_glr_plot_staghuntsim_exercise_001.png
   :alt: plot staghuntsim exercise
   :srcset: /gallery/lesson1/images/sphx_glr_plot_staghuntsim_exercise_001.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 117-123

Steady states
-------------

The steady states are the points where :math:`f(x_*)=0`. Find them
numerically using Python as follows.


.. GENERATED FROM PYTHON SOURCE LINES 123-131

.. code-block:: default


    from scipy.optimize import fsolve
    x_s=np.zeros(3)
    x_initial=[0,0,0]
    for i,x_i in enumerate(x_initial):
        x_s[i]=fsolve(dXdt, (x_i))
        print('Starting with value %.2f gives steady state %.2f'%(x_i,x_s[i]))
    




.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    Starting with value 0.00 gives steady state 0.00
    Starting with value 0.00 gives steady state 0.00
    Starting with value 0.00 gives steady state 0.00




.. GENERATED FROM PYTHON SOURCE LINES 132-147

The solution we find depends on the starting position. Here
we chose values we knew were nearby in order to be sure that we found them. 

Stability
---------

Find the derivative of :math:`f(x)` (equation :eq:`repeqsim`) 
and use it to evaluate stability of the steady states.

.. math:: 

  f'(x) = .....


We can evaluate the steady states we found using this derivative to determine their stability.

.. GENERATED FROM PYTHON SOURCE LINES 147-163

.. code-block:: default


    def dfdx(x):
        # Replicator equation - place holder just now
        return 1
 
    for x in x_s:
        dfx=dfdx(x)
        if (dfx>0):
            print("Steady state %.2f is unstable (f'(x)= %.4f)"%(x,dfx))
        elif (dfx<0):
            print("Steady state %.2f is stable (f'(x)= %.4f)"%(x,dfx))
        
              
    






.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    Steady state 0.00 is unstable (f'(x)= 1.0000)
    Steady state 0.00 is unstable (f'(x)= 1.0000)
    Steady state 0.00 is unstable (f'(x)= 1.0000)





.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.098 seconds)


.. _sphx_glr_download_gallery_lesson1_plot_staghuntsim_exercise.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example


    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: plot_staghuntsim_exercise.py <plot_staghuntsim_exercise.py>`

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: plot_staghuntsim_exercise.ipynb <plot_staghuntsim_exercise.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
