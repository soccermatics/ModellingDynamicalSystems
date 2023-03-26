"""
Happy world
===========

**What we will learn:** Plotting data and looking for relationships.
Fitting straight lines to data. Understanding the slope and intercept of the line as parameters. 
Showing that the parameters are the best possible fit to the data.

**Good to know beforehand:** `Scatter diagrams <https://www.bbc.co.uk/bitesize/guides/znjv4wx/revision/1>`_ ; 
`Equation for a straight line <https://www.bbc.co.uk/bitesize/guides/zt8sgk7/revision/1>`_ ; 
`Differentiation <https://www.bbc.co.uk/bitesize/guides/zyj77ty/revision/1>`_

Plotting the data
-----------------

Every year since 2005, the World Happiness Report has analysed the results of the Gallup World Poll, 
which is carried out in 160 countries (covering 99% of the world’s population). 
The pollsters contact a random sample of people in each country and ask them over 
100 questions – about their income, their health and their family. These questions include the 
following question about happiness:::

All things considered, how satisfied are you with your life as a whole these days? Use a 0 to 10 scale, 
where 0 is dissatisfied and 10 is satisfied to give your answer.

People living in different countries give different answers. In the UK is 6.94, making the UK 17th in the world for happiness. 
The top ranked country – rather surprisingly given a national stereotype of people who are reserved and don’t express their 
feelings very much – is Finland, with a score of 7.82. In general, Scandinavian and Northern European countries are 
ranked highest. The USA is 16th (0.03 points ahead of the UK). China, with a score of 5.59 and at 72nd place, is 
roughly in the middle of the table of the countries surveyed. Other mid-ranked countries include Montenegro, Ecuador, 
Vietnam and Russia. Further down the table, we find many African – Uganda and Ethiopia placed 117th and 131st, 
respectively – and Middle Eastern countries – Iran is at 110 and Yemen at 132.  
The unhappiest country in the world in 2022 is Afghanistan, with an average happiness score of only 2.40.
"""

from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# Read in the data
happy = pd.read_csv("../data/HappinessData.csv",delimiter=';') 
happy.rename(columns = {'Social support':'SocialSupport'}, inplace = True) 
happy.rename(columns = {'Life Ladder': 'Happiness'}, inplace = True) 
happy.rename(columns = {'Perceptions of corruption':'Corruption'}, inplace = True) 
happy.rename(columns = {'Log GDP per capita': 'LogGDP'}, inplace = True) 
happy.rename(columns = {'Healthy life expectancy at birth': 'LifeExp'}, inplace = True) 
happy.rename(columns = {'Freedom to make life choices': 'Freedom'}, inplace = True) 

# We just look at data for 2018 and dsiplay in table.
df=happy.loc[happy['Year'] == 2018]
display(df[['Country name','LifeExp','Happiness']])

##############################################################################
# Plotting the data 
# -----------------
# The code below plots the average life expectancy of 
# each of these countries against their happiness (life ladder) scores. 


from pylab import rcParams
rcParams['figure.figsize'] = 14/2.54, 14/2.54
matplotlib.font_manager.FontProperties(family='Helvetica',size=11)


def plotData(df,x,y): 
    fig,ax=plt.subplots(num=1)
    ax.plot(x,y, data=df, linestyle='none', markersize=5, marker='o', color=[0.85, 0.85, 0.85])
    for country in ['United States','United Kingdom','Croatia','Benin','Finland','Yemen']:
        ci=np.where(df['Country name']==country)[0][0]
        ax.plot(  df.iloc[ci][x],df.iloc[ci][y], linestyle='none', markersize=7, marker='o', color='black')
        ax.text(  df.iloc[ci][x]+0.5,df.iloc[ci][y]+0.08,  country)
           
    ax.set_xticks(np.arange(30,90,step=5))
    ax.set_yticks(np.arange(11,step=1))
    ax.set_ylabel('Average Happiness (0-10)')
    ax.set_xlabel('Life Expectancy at Birth')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(47,78)
    ax.set_ylim(2.5,8.1) 
    return fig,ax

fig,ax=plotData(df,'LifeExp','Happiness')

plt.show()

##############################################################################
# Each circle in the plot is a country. 
# The x-axis shows the life expectancy in the country and 
# the y-axis shows the average ranking of life-satisfaction, 
# on the 0 to 10 scale. In general, the higher the life expectancy of a country, 
# the higher the happiness there. 
#
# Drawing a line through the data 
# -------------------------------
# 
# One way to quantify this relationship is to draw a straight line
# through the points, showing how happiness increases with life expectancy. 
# For example, imagine that for every 12 extra years which people live in a 
# country they are one point happier. The equation for happiness in this case 
# would then look like this,
#
# .. math::
#    
#    \mbox{Happiness} = \frac{\mbox{Life Expectancy}}{12}
#
# For example, if the average life expectancy in the country 
# is 60 then the equation above predicts the happiness to be 60/12=5. 
# If the life expectancy is 78 then average happiness will be 78/12=6.5. 

# We can draw this equation in the form of a straight line going 
# through the cloud of country points, as shown below.

fig,ax=plotData(df,'LifeExp','Happiness')

# Setup parameters 
# a is the lines intercept
# b is the slope of the line
# and calculate a line
m=1/12
Life_Expectancy=np.arange(0.5,100,step=0.01)
Happiness= m*Life_Expectancy

ax.plot(Life_Expectancy, Happiness, linestyle='-', color='black')
df=df.assign(Predicted=np.array(m*df['LifeExp']))
for country in ['United States','United Kingdom','Croatia','Benin','Finland','Yemen']:
    ci=np.where(df['Country name']==country)[0][0]
    ax.plot(  [df.iloc[ci]['LifeExp'],df.iloc[ci]['LifeExp']] ,[ df.iloc[ci]['Happiness'],df.iloc[ci]['Predicted']] ,linestyle=':', color='black')
 
plt.show()

##############################################################################
# Try changing the slope and the intercept of the line above by 
# changing the values 0 and 1/12 in the code above and replotting the line.
# See if you can find a line that lies closer to the data points.
#
# Each of the dotted lines show how far the prected line – which predicts that happiness is one 
# twelfth of life expectancy – is from the data for each of the six highlighted countries.
# For example, the USA has a happiness score of 6.88 and an 
# average life expectancy of 68.3. The first equation (figure 2b) predicts 
#
# .. math::
#    
#    \mbox{Predicted USA Happiness} = \frac{\mbox{USA Life Expectancy}}{12} = \frac{\mbox{68.3}}{12} =  5.69
#
# Which means that the squared distance between the prediction and reality is 
#
# .. math::
#    
#  (6.88 - 5.69)^2 = 1.412
#
# The table below shows the predicted value and the squared distance between 
# prediction and reality for each country. We then sum these squared distances 
# to get an overall measure of how far our predictions our from reality. This is done below.

df=df.assign(SquaredDistance=np.power((df['Predicted'] - df['Happiness']),2))
display(df[['Country name','Happiness','Predicted','SquaredDistance']])
             
Model_Sum_Of_Squares = np.sum(df['SquaredDistance'])

print('The model sum of squares is %.4f' % Model_Sum_Of_Squares)

##############################################################################
# The question is whether this line is the ‘best’ line? You can test to see if you get a line
# which is closer to the data, by changing a and b above and seeing if the sum of squares gets smaller.
# 

##############################################################################
# Finding the best fit line 
# -------------------------
# Let’s start by formulating this problem mathematically. 
# For each country :math:`i`, 
# we have two values: the life satisfaction, which I will call :math:`y_i` 
# and life expectancy, which I will call :math:`x_i` . For example, 
# when :math:`i=`USA then :math:`x_i=6.88` and :math:`y_i=68.3`. 
#
# Now, let’s denote the slope of the line as :math:`m` (in the plot above
# :math:`m=1/12`) and repeat the caluclation we made above but with letters instead 
# of numbers. First we note that 
#
# .. math::
#    
#  \hat{y_i} = m \cdot x_i = 1/12 \cdot 6.88
#
# The little "hat" in :math:`\hat{y_i}` denotes that it is a prediction 
# (rather than the measured value itself, which is :math:`y_i`). 
# The squared distance between the prediction and outcome is written as
#
# .. math::
# 
#  ( y_i - m \cdot x_i)^2 
# 
# I want to emphasise here that all I am doing is rewriting the same calculation I
# did above with numbers, but now with the letters. The reason for doing this is that 
# our aim is to find an equation for the value of :math:`m` which minimises the sum of square 
# distances.
#
# The next step is to write out the sum
#
# .. math::
#
#  ( y_1 - m \cdot x_1)^2 +  ( y_2 - m \cdot x_2)^2  + ... + ( y_{136} - m \cdot x_{136})^2  
#
# The above equation is can be written in shorthand form as
#
# .. math::
#
#  \sum_i^n ( y_i - m \cdot x_i)^2 
#
# where :math:`n=136` is the number of countries. 
#
# We want to find the value of :math:`m` which minimises this sum of squares. But how do we do this?


##############################################################################
# A diversion in to differentiation
# ---------------------------------
# This part of the webpage assumes you have studied differentiation 
# and you understand that the derivative is about finding an equation
# for the slope of a curve. When the derivative is zero, the slope is zero.
#
# To refresh your memory, imagine you are asked to find the value 
# of :math:`m` which minimises the 
# function :math:`(4-2m)^2`. To solve this problem, you can first multiply out 
# the brackets to get
#
# .. math::
#
#  (4-2m)^2 = 16 - 16m + 4m^2 
#
# You can then take a derivative in order to calculate the slope of the function, 
# as follows.
#
# .. math::
#
#  \frac{d}{dm} 16 - 16m + 4m^2= - 16 + 8m
#
# We then solve this equal to zero, 
# because the function is a minimum when it has slope zero.
#
# .. math::
#
#   - 16 + 8m = 0 \Rightarrow 8m = 16 \Rightarrow m = 2
# 
# Problem solved. 
#
# Although  the algebra is more complicated, we can use exactly the same logic to solve the problem 
# above, of finding the value of :math:`m` which minimises this sum of squares. We first
# take the derivative 
#
#
# .. math::
#
#  \frac{d}{dm} \left( ( y_1 - m \cdot x_1)^2 +  ( y_2 - m \cdot x_2)^2  + ... + ( y_{136} - m \cdot x_{136})^2  \right)
#
#  = - 2 x_1 y_1 + 2 x_1^2 m  - 2 x_2 y_2 + 2 x_2^2 m  +  ... - 2 x_{136} y_{136} + 2 x_{136}^2 m  
#
# Again, although this particular step involves alot of algebra, notice that we are doing exactly the same as in the example above.
# Another thing that can confuse students (when I teach this in statistics) is that we differentiate with respect to :math:`m`. 
# In school, we often use the letter :math:`x` for the variable name and :math:`m` for a constant. Here it is the other way round. 
# The data :math:`x_i` and :math:`y_i` are constants (measurements from countries) and  :math:`m` is the variable we differentiate for.
#
# We now write the sum above in shorthand as
#
# .. math::
#
#  \sum_i^n 2 x_i y_i - \sum_i^n 2 \cdot x_i^2 m
#
# and we solve equal to zero (to find the point at which it is mimized, and the slope is zero) to get
#
# .. math::
#
#  \sum_i^n 2 x_i y_i - \sum_i^n 2 \cdot x_i)^2 m = 0 \Rightarrow \sum_i^n 2 x_i y_i = \sum_i^n 2 \cdot x_i^2 m \Rightarrow \sum_i^n x_i y_i = \sum_i^n x_i^2
#
# Moving the :math:`m` to the left hand side gives
#
# .. math::
#
#  m = \frac{\sum_i^n x_i y_i}{\sum_i^n x_i^2}
# 
# Lets now use our newly found equation to calculate the line that best fits the data.

df=df.assign(SquaredLifEExp=np.power(df['LifeExp'],2))
df=df.assign(HappinessLifEExp=df['LifeExp'] * df['Happiness'])

m_best = np.sum(df['HappinessLifEExp'])/np.sum(df['SquaredLifEExp'])
print('The best fitting line has slope m = %.4f' % m_best)

##############################################################################
# Our intial guess of :math:`m = 1/12 = 0.0833` wasn't so far away from the best fitting value. 
# But this new slope is slightly closer to the data. We can now plot this and recalculate the model sum of squares
# 

Life_Expectancy=np.arange(0.5,100,step=0.01)
Happiness= m_best*Life_Expectancy

fig,ax=plotData(df,'LifeExp','Happiness')
ax.plot(Life_Expectancy, Happiness, linestyle='-', color='black')
df=df.assign(Predicted=np.array(m_best*df['LifeExp']))
for country in ['United States','United Kingdom','Croatia','Benin','Finland','Yemen']:
    ci=np.where(df['Country name']==country)[0][0]
    ax.plot(  [df.iloc[ci]['LifeExp'],df.iloc[ci]['LifeExp']] ,[ df.iloc[ci]['Happiness'],df.iloc[ci]['Predicted']] ,linestyle=':', color='black')
 
plt.show()

df=df.assign(SquaredDistance=np.power((df['Predicted'] - df['Happiness']),2))
             
Model_Sum_Of_Squares = np.sum(df['SquaredDistance'])             
print('The model sum of squares is %.4f' % Model_Sum_Of_Squares)

##############################################################################
# Again, this sum of squares is slightly smaller than the value we got above 
# for :math:`m = 1/12` 
#


##############################################################################
# Including the Intercept
# -----------------------
#
# Let's start by shifting the data so that it has a mean (average) of zero.
# To do this we simply take away the mean value from both life expectancy and 
# from happiness. Then replot the data 

df=df.assign(ShiftedLifeExp=df['LifeExp'] - np.mean(df['LifeExp']))
df=df.assign(ShiftedHappiness=df['Happiness'] - np.mean(df['Happiness']))

fig,ax=plotData(df,'ShiftedLifeExp','ShiftedHappiness')
ax.set_ylabel('Happiness (corrected for Mean Happiness)')
ax.set_xlabel('Life Expectancy (corrected for Mean Life Expectancy) ')
ax.set_xticks(np.arange(-30,30,step=5))
ax.set_yticks(np.arange(-5,5,step=1))
ax.set_xlim(-20,15)
ax.set_ylim(-3,3) 
plt.show()

##############################################################################
# This graph shows us that, for example, Yemen is almost -2.5 points below the world 
# average for happiness and has a life expectency 8 years shorter than the average over
# all countries in the world. The United States life expectancy is around 3.5 years longer than 
# the average and the citizens of the USA are about 1.3 points happier than average.
# It is worth noting that the correction is for country averages and does not account for the size of the 
# populations of these various countries. It does though give us a new way 
# of seeing between country differences.
# 
#
# Let's now try to find the best fit line which goes through these data points.

df=df.assign(SquaredLifEExp=np.power(df['ShiftedLifeExp'],2))
df=df.assign(HappinessLifEExp=df['ShiftedLifeExp'] * df['ShiftedHappiness'])

m_best = np.sum(df['HappinessLifEExp'])/np.sum(df['SquaredLifEExp'])
print('The best fitting line has slope m = %.4f' % m_best)

Life_Expectancy=np.arange(-50,50,step=0.01)
Happiness= m_best*Life_Expectancy

fig,ax=plotData(df,'ShiftedLifeExp','ShiftedHappiness')
ax.plot(Life_Expectancy, Happiness, linestyle='-', color='black')
ax.set_ylabel('Happiness (corrected for Mean Happiness)')
ax.set_xlabel('Life Expectancy (corrected for Mean Life Expectancy) ')
ax.set_xticks(np.arange(-30,30,step=5))
ax.set_yticks(np.arange(-5,5,step=1))
ax.set_xlim(-20,15)
ax.set_ylim(-3,3) 

plt.show()


##############################################################################
# This line appears to fit better than the one we fitted earlier! It seems 
# to lie closer to the points and better capture the relationship in the data.
# To test whether this is indeed the case we can calculate the sum of squares
# between this new line and the shifted data. This is as follows

df=df.assign(Predicted=np.array(m_best*df['ShiftedLifeExp']))       
df=df.assign(SquaredDistance=np.power((df['Predicted'] - df['ShiftedHappiness']),2))
            
Model_Sum_Of_Squares = np.sum(df['SquaredDistance'])             
print('The model sum of squares is %.4f' % Model_Sum_Of_Squares)

##############################################################################
# This new line through the data is better! It has a smaller sum of squares. 
# 
# The mean values are calculated as follows
#
# .. math::
#
#  \bar{x} = \frac{1}{n} \sum_i^n x_i \mbox{ and }  \bar{y} = \frac{1}{n} \sum_i^n y_i 
#
# 
# Using this notation, the equation for the line through the data is
#
# .. math::
#
#  \hat{y_i} - \bar{y} = m  (\hat{x_i} - \bar{x})
#
# Just to remind you about the notation. The predicted value has a hat over it, while the mean values
# have a bar over them. We can rearrange this equation to get 
#
# .. math::
#
#  \hat{y_i}  = m \hat{x_i} + (\bar{y} - m\bar{x})
#
# Notice that this is an equation for a straight line, so we can write
#
# .. math::
#
#  \hat{y_i}  = m \hat{x_i} + k  \mbox{ where } k = \bar{y} - m\bar{x}
#
# Let's apply this to data and plot the line again

k_best = np.mean(df['Happiness']) - m_best*np.mean(df['LifeExp'])

Life_Expectancy=np.arange(0.5,100,step=0.01)
Happiness= m_best*Life_Expectancy + k_best

fig,ax=plotData(df,'LifeExp','Happiness')
ax.plot(Life_Expectancy, Happiness, linestyle='-', color='black')
df=df.assign(Predicted=np.array(m_best*df['LifeExp']+k_best))
for country in ['United States','United Kingdom','Croatia','Benin','Finland','Yemen']:
    ci=np.where(df['Country name']==country)[0][0]
    ax.plot(  [df.iloc[ci]['LifeExp'],df.iloc[ci]['LifeExp']] ,[ df.iloc[ci]['Happiness'],df.iloc[ci]['Predicted']] ,linestyle=':', color='black')
 
plt.show()

print('The slope of the line is m = %.4f and the intercept is k = %.4f' % (m_best,k_best))
print('An increase in life expectancy of %.4f years is associated with one extra point of happiness' % (1/m_best))

    
df=df.assign(SquaredDistance=np.power((df['Predicted'] - df['Happiness']),2))          
Model_Sum_Of_Squares = np.sum(df['SquaredDistance'])             
print('The model sum of squares is still %.4f' % Model_Sum_Of_Squares)


##############################################################################
# Now we have it. By shifting back to the original co-ordinates we
# can find the best fitting line through the data. Notice that the sum of squares is unaffected by
# shifting the line back again, since the distances from the points to the line are unaffected. 
#
# We can say (roughly speaking) that for every 8 years of life expectancy
# country citizens are about 1 point happier on a scale of 0 to 10. It isn't 
# the whole truth, but it isn't entirely misleading either. 




##############################################################################
# Maximum likelihood
# ------------------
# 
# In section . We have found that the values of parameters :math:`k` and :math:`m` that
# minimise the square distance to the line, but are these the maximum likelihood estimates?
#
# See `here <https://www.math.arizona.edu/~jwatkins/n-mle.pdf>`_



