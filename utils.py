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

def heatmap(data, episode):
    fig = plt.figure(episode)
    for action in range(1,5):
        plt.subplot(2,2,action)
        ax = sns.heatmap(data[:,:,action-1], annot = True)
        plt.title("Action:" + str(action))
    # ax.set_title('State action values for action', action)
    
    fig.suptitle('Heatmaps for episode:'+ str(episode+1))
    # plt.show()
    
    return 

def avg_reward(reward_array):
    fig = plt.figure()
    x_axis = range(len(reward_array))
    # plt.plot(x_axis,reward_array)
    sns.scatterplot(x = x_axis, y = reward_array)
    plt.title("Agent Performance")
    plt.xlabel('Episode')
    plt.ylabel('Average Reward per timestep')   
    
    return

def pltshow():
    plt.show()
    return 