"""
The art of a good argument
==========================

Here we...


The way we determine whether Charlie will start shouting is using 
the following table.


"""

import numpy as np
import pandas as pd

Charlie_shout =np.array([[0.1, 0.5],[0.7,0.95]])
Charlie_rules = pd.DataFrame(data= Charlie_shout,index=['Aisha calm', 'Aisha shouting'], columns=['Charlie calm', 'Charlie shoting'])
print('Probability of Charlie shouting:')
print(Charlie_rules)

Aisha_shout =np.array([[0.1, 0.7],[0.5,0.95]])
Aisha_rules = pd.DataFrame(data= Aisha_shout,index=['Aisha calm', 'Aisha shouting'], columns=['Charlie calm', 'Charlie shoting'])
print('Probability of Aisha shouting:')
print(Aisha_rules)

###################################################################
#
# Initially, neither of them are shouting

#Number of time steps
T = 25

Charlie=[0]
Aisha=[0]




###################################################################
#
# Now we loop over 25 steps of discussion according to the rules above. 
#


def argument(T,Charlie_rules,Aisha_rules,print_out=1):
    for i in range(T):

        Prob_Charlie = Charlie_rules.iloc[Charlie[i]][Aisha[i]]
        if np.random.rand()<Prob_Charlie:
            describe_Charlie = 'Charlie shouts. '
            Charlie.append(1)
        else:
            describe_Charlie = "Charlie doesn't shout. "
            Charlie.append(0)
                    
        Prob_Aisha = Aisha_rules.iloc[Charlie[i]][Aisha[i]]
        if np.random.rand()<Prob_Aisha:
            describe_Aisha = 'Aisha shouts.'
            Aisha.append(1)
        else:
            describe_Aisha = "Aisha doesn't shout."
            Aisha.append(0)
            
        if print_out:
            print('Time step %d:' % (i+1) + describe_Charlie +describe_Aisha)
    
    return Aisha,Charlie

Aisha,Charlie = argument(T,Charlie_rules,Aisha_rules)
        
###################################################################
#
# We can also represent the steps in the environment as a binary string.
#
print("Charlie's shouting as a string of zeros (clam) and ones (shouting):")
print(' '.join(map(str, Charlie)))
print("Aisha's shouting as a string of zeros (clam) and ones (shouting):")
print(' '.join(map(str, Aisha)))


###################################################################
#
# WNow we can make them argue lots of times!
#

for j in range(5):
    
    Charlie=[0]
    Aisha=[0]
    print('Argument %d' % (j+1))
    print('----------')
    Aisha,Charlie = argument(T,Charlie_rules,Aisha_rules,0)
    print("Charlie's shouting as a string of zeros (clam) and ones (shouting):")
    print(' '.join(map(str, Charlie)))
    print("Aisha's shouting as a string of zeros (clam) and ones (shouting):")
    print(' '.join(map(str, Aisha)))
    print('\n')



###################################################################
#
# Let's update Charlie's rules.
#

Charlie_shout =np.array([[0.1, 0.1],[0.1,0.95]])
Charlie_rules = pd.DataFrame(data= Charlie_shout,index=['Aisha calm', 'Aisha shouting'], columns=['Charlie calm', 'Charlie shoting'])
print('Probability of Charlie shouting:')
print(Charlie_rules)


###################################################################
#
# Now let's look at five arguments
#


for j in range(5):
    
    Charlie=[0]
    Aisha=[0]
    print('Argument %d' % (j+1))
    print('----------')
    Aisha,Charlie = argument(T,Charlie_rules,Aisha_rules,0)
    print("Charlie's shouting as a string of zeros (clam) and ones (shouting):")
    print(' '.join(map(str, Charlie)))
    print("Aisha's shouting as a string of zeros (clam) and ones (shouting):")
    print(' '.join(map(str, Aisha)))
    print('\n')



