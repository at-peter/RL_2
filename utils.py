'''
This is where utility functions will go 
'''
import math 
import random


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

'''
Plotter: 

'''
import seaborn as sns 
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
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

def avg_reward(reward_array, run):
    fig = plt.figure()
    sns.set_style('white')
    sns.set_style('ticks')
    x_axis = range(len(reward_array))
    # plt.plot(x_axis,reward_array)
    sns.scatterplot(x = x_axis, y = reward_array)
    sns.despine()
    # sns.regplot(x = x_axis, y = reward_array)
    plt.title("Average reward of each episode in run " + str(run))
    plt.xlabel('Episode')
    plt.ylabel('Average Reward per timestep')   
    
    return

def pltshow():
    plt.show()
    return 

def savefig(pdf_name):
    '''
    This function saves figures to a pdf 
    '''
    pp = PdfPages('pdf_path')


def __do_the_HeMAN_2(Q_array, run):
    fig = plt.figure()
    Q_2d = np.mean(Q_array, axis = 2)
    az = sns.heatmap(Q_2d, annot = True ,cmap='Greens')
    prefd_action = np.argmax(Q_array, axis=-1)
    print(prefd_action.shape)
    plt.title('State action value Heatmap: Run '+ str(run + 1))

    fig2 = plt.figure()
    ab = sns.heatmap(prefd_action, annot = True, cmap='Blues')
    plt.title('Policy: Run' + str(run + 1))
    return

def predictive_novelty_plot(diff_array, episode):
    fig = plt.figure()
    x_axis = range(len(diff_array))
    sns.scatterplot(x = x_axis, y = diff_array)
    plt.title('Predictive Novelty plot for episode' + str(episode))
    return


def random_seed(seed):
    random.seed(seed)
    return

def save_to_pdf(pdf_name):
    import matplotlib.backends.backend_pdf as pp
    pdf = pp.PdfPages(pdf_name + ".pdf")
    for fig in plt.get_fignums():
        pdf.savefig(fig)
        plt.close()
    pdf.close()
   