"""
World Bank Data
===============

In this notebook we will model world development, inspired by the
presentations of `Hans Rosling on 200 years that changed the
world <https://https://www.gapminder.org/videos/200-years-that-changed-the-world/>`_.

We will go through the steps of downloading data from an Application
Programming Interface (API), plotting it, fitting a linear regression
model (with non-linear terms) and then using a model to make future
predictions.

First we use the World Bank API in order to download the data.
"""

#Import libraries
#Plotting 
import matplotlib as mpl
import matplotlib.pyplot as plt
#Dataframes (panda) and math opperations (numpy)
import pandas as pd
import numpy as np
#World bank data interface
import world_bank_data as wb
#Import machine learning tools (for linear regression)
import sklearn.linear_model as skl_lm
import itertools
import math
    
# Default plotting options.
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False


##############################################################################
# Now we download the data set, indexed with the country code.
#
# The data is downloaded from here `here <https://databank.worldbank.org/home>`_.

gdp_percapita = wb.get_series('NY.GNP.PCAP.CD', id_or_value='id', simplify_index=True)
gdp_percapita
childmortality = wb.get_series('SH.DYN.MORT', id_or_value='id', simplify_index=True)
childmortality

##############################################################################
# Now we reorganise the data so it is in a dataframe (like an Excel
# spreadsheet) with columns Year, Country, Child Mortality (per 10,000
# births) (:math:`C(k)`), log Gross Domestic Product per person
# (:math:`G(k)`) and change in these two variables — :math:`C(k+1)-C(k)`
# and :math:`G(k+1)-G(k)` — over time :math:`k`.
#
# (This can take one minute or so to run)

cm=childmortality.to_frame()
gdp=gdp_percapita.to_frame()

df = pd.DataFrame(columns=('Year', 'Country','Child Mortality','GDP','Diff CM','Diff GDP'))
countries = cm.index
this_country=''
this_cm=0
this_gdp=0
j=0

for i,c in enumerate(countries):
    

    prev_cm=this_cm
    prev_gdp=this_gdp
    prev_country=this_country
        
    #Update for this year.
    this_year=c[1]
    this_cm=cm.iloc[i]['SH.DYN.MORT']
    this_gdp=np.log(gdp.iloc[i]['NY.GNP.PCAP.CD'])
    this_country=c[0]
    
    if (prev_country==this_country):
        #Update differences and put in matrix
        diff_cm=this_cm-prev_cm
        diff_gdp=this_gdp-prev_gdp
        if not(np.isnan(diff_cm) or np.isnan(diff_gdp)):
            df.loc[j] = [this_year,this_country,this_cm,this_gdp,diff_cm,diff_gdp]
            j=j+1

df.head()
#df.to_csv('../data/CM_GDP.csv') 

##############################################################################
# By uncommenting the line above you save the data set to a directory called
# data. 