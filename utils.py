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
import numpy as np
sns.set()

def heatmap(data, episode):
    fig = plt.figure(episode)
    for action in range(1,5):
        plt.subplot(2,2,action)
        ax = sns.heatmap(data[:,:,action-1], annot = True, cmap='Blues')
        plt.title("Action:" + str(action))
    # ax.set_title('State action values for action', action)
    
    fig.suptitle('Heatmaps for episode:'+ str(episode+1))
    # plt.show()
    
    return 

def avg_reward(reward_array):
    fig = plt.figure()
    print(len(reward_array))
    x_axis = range(len(reward_array))
    print('x axis', len(x_axis))
    # plt.plot(x_axis,reward_array)
    # sns.scatterplot(x = x_axis, y = reward_array)
    sns.regplot(x = x_axis, y = reward_array)
    plt.title("Agent Performance")
    plt.xlabel('Episode')
    plt.ylabel('Average Reward per timestep')   
    
    return

def pltshow():
    plt.show()
    return 

def __do_the_HeMAN_2(Q_array, episode):
    fig = plt.figure()
    Q_2d = np.mean(Q_array, axis = 2)
    az = sns.heatmap(Q_2d, annot = True ,cmap='Greens')
    prefd_action = np.argmax(Q_array, axis=-1)
    print(prefd_action.shape)
    plt.title('Agregatte state action value Heatmap:'+ str(episode))

    fig2 = plt.figure()
    ab = sns.heatmap(prefd_action, annot = True, cmap='Blues')
    plt.title('Best action for each state')
    return