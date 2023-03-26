"""
All of the life
===============


"""

import numpy as np
from termcolor import colored
from time import sleep
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 12/2.54, 2/2.54

##############################################################################
# This code is adapted from an implentation by Romain Fontaine (Copyright 2018)
#
# First we set up functions which allow us to run sellular automata.

def show_grid(ax,grid):
        ax.imshow(grid, cmap=plt.get_cmap('Blues'), interpolation='nearest')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.set_ylim(0,N)
        ax.set_xlim(0,N)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('equal')
        
	
def iterate(new_grid):
	for i in range(N):
		for j in range(N):
			new_grid[i,j]=new_value(i, j)
	return new_grid, grid
 

##############################################################################
# Game Of Life
# ------------
#
# Now we set up the cellular automata 
#

def new_value(i, j):
	
    neighbours = grid[i, (j-1)%N] + grid[i, (j+1)%N] + grid[(i-1)%N, j] + grid[(i+1)%N, j] +grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]
    
    # Apply rules
    if grid[i, j]  == 1:
        if (neighbours < 2) | (neighbours > 3):
            return 0
    else:
        if neighbours == 3:
            return 1
    return grid[i, j]


#############################################################################
#
# Now we set up the initial shape the model printing out every step
#


def initialize():
    init_pattern = ["111",
			"001",
			"010"]
    for i, line in enumerate(init_pattern):
	    for j, char in enumerate(line):
		    grid[i+int(N/2)-2, j+int(N/2)-2] = int(char)

N=8
STEPS = 10

grid = np.zeros((N, N), dtype="int")
new_grid = np.zeros((N, N), dtype="int")
initialize()

#############################################################################
#
# Now simulate
#


fig,axs=plt.subplots(1,STEPS)
for step in range(STEPS):
    grid, new_grid = iterate(new_grid) # Iterate & swap the two grids
    show_grid(axs[step],new_grid)
    
plt.show()




# CODE FOR ANIMATING
# set up animation
#    fig, ax = plt.subplots()
#    img = ax.imshow(grid, interpolation='nearest')
#    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
#                                  frames = 10,
#                                  interval=updateInterval,
#                                  save_count=50)
# 
#    # # of frames?
#    # set output file
#    if args.movfile:
#        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

##############################################################################
# Langton's Loop
# --------------
#
# Now we set up the cellular automata 
#

N = 120
STEPS = 800

def initialize():
	init_pattern = ["02222222200000",
			"21701401420000",
			"20222222020000",
			"27200002120000",
			"21200002120000",
			"20200002120000",
			"27200002120000",
			"21222222122222",
			"20710710711111",
			"02222222222222"]
	for i, line in enumerate(init_pattern):
		for j, char in enumerate(line):
			grid[i+int(N/2)-5, j+int(N/2)-15] = int(char)

##############################################################################
# And set up the rules and a function which applies them.

rules = { # format: "CNESW":"C"
	"00000":"0","00001":"2","00002":"0","00003":"0","00005":"0","00006":"3","00007":"1","00011":"2","00012":"2","00013":"2","00021":"2",
	"00022":"0","00023":"0","00026":"2","00027":"2","00032":"0","00052":"5","00062":"2","00072":"2","00102":"2","00112":"0",
	"00202":"0","00203":"0","00205":"0","00212":"5","00222":"0","00232":"2","00522":"2","01232":"1","01242":"1","01252":"5",
	"01262":"1","01272":"1","01275":"1","01422":"1","01432":"1","01442":"1","01472":"1","01625":"1","01722":"1",
	"01725":"5","01752":"1","01762":"1","01772":"1","02527":"1","10001":"1","10006":"1","10007":"7","10011":"1","10012":"1",
	"10021":"1","10024":"4","10027":"7","10051":"1","10101":"1","10111":"1","10124":"4","10127":"7","10202":"6",
	"10212":"1","10221":"1","10224":"4","10226":"3","10227":"7","10232":"7","10242":"4","10262":"6","10264":"4",
	"10267":"7","10271":"0","10272":"7","10542":"7","11112":"1","11122":"1","11124":"4","11125":"1","11126":"1",
	"11127":"7","11152":"2","11212":"1","11222":"1","11224":"4","11225":"1","11227":"7","11232":"1","11242":"4",
	"11262":"1","11272":"7","11322":"1","12224":"4","12227":"7","12243":"4","12254":"7","12324":"4","12327":"7",
	"12425":"5","12426":"7","12527":"5","20001":"2","20002":"2","20004":"2","20007":"1","20012":"2","20015":"2",
	"20021":"2","20022":"2","20023":"2","20024":"2","20025":"0","20026":"2","20027":"2","20032":"6","20042":"3",
	"20051":"7","20052":"2","20057":"5","20072":"2","20102":"2","20112":"2","20122":"2","20142":"2","20172":"2",
	"20202":"2","20203":"2","20205":"2","20207":"3","20212":"2","20215":"2","20221":"2","20222":"2","20227":"2",
	"20232":"1","20242":"2","20245":"2","20252":"0","20255":"2","20262":"2","20272":"2","20312":"2","20321":"6",
	"20322":"6","20342":"2","20422":"2","20512":"2","20521":"2","20522":"2","20552":"1","20572":"5","20622":"2",
	"20672":"2","20712":"2","20722":"2","20742":"2","20772":"2","21122":"2","21126":"1",
	"21222":"2","21224":"2","21226":"2","21227":"2","21422":"2","21522":"2","21622":"2","21722":"2","22227":"2","22244":"2",
	"22246":"2","22276":"2","22277":"2","30001":"3","30002":"2","30004":"1","30007":"6","30012":"3","30042":"1",
	"30062":"2","30102":"1","30122":"0","30251":"1","40112":"0","40122":"0","40125":"0","40212":"0","40222":"1",
	"40232":"6","40252":"0","40322":"1","50002":"2","50021":"5","50022":"5","50023":"2","50027":"2","50052":"0",
	"50202":"2","50212":"2","50215":"2","50222":"0","50224":"4","50272":"2","51212":"2","51222":"0","51242":"2","51272":"2",
	"60001":"1","60002":"1","60212":"0","61212":"5","61213":"1","61222":"5","70007":"7",
	"70112":"0","70122":"0","70125":"0","70212":"0","70222":"1","70225":"1","70232":"1","70252":"5","70272":"0"
}

def new_value(i, j):
	c = str(grid[i, j])
	a = [str(grid[(i-1)%N, j]), str(grid[i, (j+1)%N]), str(grid[(i+1)%N, j]), str(grid[i, (j-1)%N])]
	for i in range(4): # Try every rotation of this array: [TOP, RIGHT, BOTTOM, LEFT]
		try:
			return rules["".join([c, a[i%4], a[(i+1)%4], a[(i+2)%4], a[(i+3)%4]])]
		except KeyError:
			pass
	return grid[i, j] # if no rule is found, return the previous value



#############################################################################
#
# Now we simulate the model printing out every 50th step
#

grid = np.zeros((N,N), dtype="int")
new_grid = np.zeros((N,N), dtype="int")
rcParams['figure.figsize'] = 20/2.54, 20/2.54
initialize()
fig,axs=plt.subplots(4,4)
count=0
count2=0
for i in range(STEPS):
    grid, new_grid = iterate(new_grid) # Iterate & swap the two grids
    if (np.mod(i,50)==0):
        show_grid(axs[count][count2],new_grid)
        count=count+1
        if count>=4:
            count2=count2+1
            count=0
        
plt.show()


