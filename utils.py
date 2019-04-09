'''
This is where utility functions will go 
'''
import math 


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

'''
Plotter: 

'''
import seaborn as sns 
from matplotlib import pyplot as plt
sns.set()
def heatmap(data,action):
    ax = sns.heatmap(data[:,:,action], annot = True)
    plt.show()
    return 