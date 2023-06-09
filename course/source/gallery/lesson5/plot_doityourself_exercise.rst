
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "gallery/lesson5/plot_doityourself_exercise.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_gallery_lesson5_plot_doityourself_exercise.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_gallery_lesson5_plot_doityourself_exercise.py:


Do it yourself
==============

Fitting a single variable model to GDP
--------------------------------------

The plot below should show change in GDP for the four countries. The code below is wrong. Complete it by filling in the correct code
below. (You can generate the data file needed using the code on page :ref:`World Bank Data<download>`)

.. GENERATED FROM PYTHON SOURCE LINES 13-50

.. code-block:: default

    #Import libraries
    #Plotting 
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import sklearn.linear_model as skl_lm

    df = pd.read_csv('../data/CM_GDP.csv')

    countries=['SWE','USA','CHN','UGA']
    country_colour_dict= {
      "USA": "blue",
      "CHN": "red",
      "SWE": "yellow",
      "UGA": "black",
      "AFG": "green"
    }

    fig,ax=plt.subplots(num=1)
    for country in countries:
        df_country=df.loc[df['Country'] == country]

        years=np.array(df_country['Year']).astype('int32')
        ax.plot(years,years,linestyle='none', color =country_colour_dict[country], markersize=3, marker='o',label=country)
    ax.legend()
    ax.set_xticks(np.arange(1960,2030,step=10))
    ax.set_yticks(np.arange(5,14,step=1))
    ax.set_ylabel('log GDP per person')
    ax.set_xlabel('Year (k)')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(1960,2030)
    ax.set_ylim(4,13) 

    plt.show()





.. image-sg:: /gallery/lesson5/images/sphx_glr_plot_doityourself_exercise_001.png
   :alt: plot doityourself exercise
   :srcset: /gallery/lesson5/images/sphx_glr_plot_doityourself_exercise_001.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 51-63

Single variable
---------------

Fit a linear regression model

.. math::


  y(k) = G(k+1) - G(k) = a + b_0 G(k) + b_1 G(k)^2 + \epsilon, \qquad \epsilon \sim \mathcal{N}(0, \sigma^2)

to describe the change in log(GDP) from one year to the next. Write the code to do this below.


.. GENERATED FROM PYTHON SOURCE LINES 69-71

This code can be used to make a plot of the change in GDP as a function of GDP.


.. GENERATED FROM PYTHON SOURCE LINES 71-89

.. code-block:: default


    G = np.arange(0,14,0.1)
    dG = 0 + 0 * G + 0*G**2 

    fig,ax=plt.subplots(num=1)
    ax.plot(df['GDP'],df['Diff GDP'],linestyle='none', markersize=1,color='grey',marker='.')
    ax.plot(G,dG,linewidth=2)
    ax.plot([0 ,200],[0, 0],linestyle=':',color='black')
    ax.set_yticks(np.arange(-5,0.5,step=1))
    ax.set_xticks(np.arange(4,14,step=1))
    ax.set_ylabel('$G(k+1)-G(k)$')
    ax.set_xlabel('log GDP: $G(k)$')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(4,14) 
    ax.set_ylim(-0.5,0.5) 
    plt.show()




.. image-sg:: /gallery/lesson5/images/sphx_glr_plot_doityourself_exercise_002.png
   :alt: plot doityourself exercise
   :srcset: /gallery/lesson5/images/sphx_glr_plot_doityourself_exercise_002.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 90-92

Predict future evoltion of GDP
Add code to make this prediction

.. GENERATED FROM PYTHON SOURCE LINES 92-121

.. code-block:: default


    fig,ax=plt.subplots(num=1)
    for country in countries:
        df_country=df.loc[df['Country'] == country]

        years=np.array(df_country['Year']).astype('int32')
        ax.plot(years,df_country['GDP'],linestyle='none', color =country_colour_dict[country], markersize=3, marker='o',label=country)
  
        numyears=20
        future_GDP=np.zeros(numyears)
        future_GDP[0]=df_country['GDP'][-1:]
    
    
        for t in range(numyears-1):
            future_GDP[t+1]=future_GDP[t] 

        ax.plot(int(df_country['Year'][-1:])+np.arange(numyears),future_GDP, color =country_colour_dict[country],linestyle='-',label=country)
    ax.legend()
    ax.set_xticks(np.arange(1960,2045,step=10))
    ax.set_yticks(np.arange(4,14,step=1))
    ax.set_ylabel('log GDP')
    ax.set_xlabel('Year (k)')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(1960,2040)
    ax.set_ylim(4,14)   
    plt.show()





.. image-sg:: /gallery/lesson5/images/sphx_glr_plot_doityourself_exercise_003.png
   :alt: plot doityourself exercise
   :srcset: /gallery/lesson5/images/sphx_glr_plot_doityourself_exercise_003.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 122-129

Two variables
-------------

Fill in the code below to simulate the model we fitted on page `twovariable`_ 
to make predictions of how child mortality and GDP will chnage over the next 30 years.

The co-efficients in your simulated model must be the same as the ones you found when fitting the model.

.. GENERATED FROM PYTHON SOURCE LINES 129-158

.. code-block:: default




    fig,ax=plt.subplots(num=1)
    for country in countries:
        df_country=df.loc[df['Country'] == country]
        ax.plot(df_country['GDP'], df_country['Child Mortality'],linestyle='none', markersize=3, color =country_colour_dict[country],  marker='o',label=country)
       
        numyears=20
        future_CM=np.zeros(numyears)
        future_CM[0]=df_country['Child Mortality'][-1:]
        future_GDP=np.zeros(numyears)
        future_GDP[0]=df_country['GDP'][-1:]
    
        ax.legend()
    
        for t in range(numyears-1):
            future_CM[t+1]=future_CM[t]
            future_GDP[t+1]=future_GDP[t]
        
        ax.plot(future_GDP,future_CM, color =country_colour_dict[country],linestyle='-',label=country)

    ax.set_xticks(np.arange(5,12,step=1))
    ax.set_yticks(np.arange(0,200,step=25))
    ax.set_ylabel('Child Mortality (per 1000)')
    ax.set_xlabel('log(GDP)')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(0,201) 
    ax.set_xlim(5,11.5)   


.. image-sg:: /gallery/lesson5/images/sphx_glr_plot_doityourself_exercise_004.png
   :alt: plot doityourself exercise
   :srcset: /gallery/lesson5/images/sphx_glr_plot_doityourself_exercise_004.png
   :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 .. code-block:: none


    (5.0, 11.5)




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.393 seconds)


.. _sphx_glr_download_gallery_lesson5_plot_doityourself_exercise.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example


    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: plot_doityourself_exercise.py <plot_doityourself_exercise.py>`

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: plot_doityourself_exercise.ipynb <plot_doityourself_exercise.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
