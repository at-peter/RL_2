import pandas as pd
import numpy as np 
import seaborn as sns
from matplotlib import pyplot as plt


def loadDataframe(Filename):
    '''

    '''
    data = pd.read_csv(str(Filename))
    return data



def average_index(filename):
    data = pd.read_csv(filename)
    average_data = (data.mean(axis = 1)).values
    return average_data

def plotting_on_the_same_thing(useable_data):
    sns.set()
    sns.set_style('white')
    sns.set_style('ticks')
    log_scale = np.logspace(1,0,num = 10)/10
    x_axis = range(8000)
    handles = []
    for i in range(0,len(useable_data)):
        a, = plt.plot(x_axis,useable_data[i], label = 'Coefficient value :'+str(i+1))
        handles.append(a)
        # plt.yscale('log')
        plt.title('Parameter Sweep of Intermediate Novelty Coefficient Values')
        plt.ylabel('Average Reward Per Episode')
        plt.xlabel('Episode')
    # plt.legend(handles, bbox_to_anchor=(1.05, 1), loc = 2, borderaxespad=0.)
    plt.legend()
    sns.despine()
    # plt.annotate('Blue Line', xy=(6400,200), xytext=(6500, 250),color ='blue',
    # arrowprops=dict(facecolor='blue',shrink = 0.05),
    # )
    # plt.show()
    return 

def plotting_on_the_same_thing2(useable_data):
    sns.set()
    sns.set_style('white')
    sns.set_style('ticks')
    log_scale = np.logspace(1,0,num = 10)/10
    x_axis = range(8000)
    handles = []
    for i in range(0,10,2):
        lab = str(range(1))
        a, = plt.plot(x_axis,useable_data[i], label = 'Threshold Value: ' + str(log_scale[i]))
        handles.append(a)
        # plt.yscale('log')
        plt.title('Parameter Sweep of Predictive Novelty Threshold Values')
        plt.ylabel('Average Reward Per Episode')
        plt.xlabel('Episode')
    # plt.legend(handles, bbox_to_anchor=(1.05, 1), loc = 2, borderaxespad=0.)
    plt.legend()
    sns.despine()
    # plt.annotate('Blue Line', xy=(6400,200), xytext=(6500, 250),color ='blue',
    # arrowprops=dict(facecolor='blue',shrink = 0.05),
    # )
    # plt.show()
    return 


if __name__ == "__main__":
    
    '''
    This is for rapidfiring through the parameter sweeps: 
    '''
    
    '''
    This is the EPE coefficient and the coefficitant thresh. 
    '''
    
    # fig = plt.figure()
    Epsilon = 0
    # NovelCoeff = 1
    run_average = []
    NovelThresh = 0.5
    log_scale = np.logspace(1,0,num = 10)/10
    
    for i in range(1,7, 2):
        NovelCoeff = i
        # title = 'ParamSweep3ETC' + str(Epsilon) + str(NovelThresh) + str(NovelCoeff) + '.csv'
        title = 'ParamSweepETC' + str(Epsilon) + str(NovelThresh)+ str(NovelCoeff) + '.csv'
        # title = 'ExpParamSweepETC00.5' + str(i) + '.csv'
        avg_data = average_index(title)
        run_average.append(avg_data)
        print('.')
        
    print(len(run_average))
    fig = plt.figure()
    plotting_on_the_same_thing(run_average)

    eps_baseline = average_index('Benchmark_egreedy.csv')
    ax, = plt.plot(range(len(eps_baseline)),eps_baseline,'--', label='epsilon')
    
    plt.legend() 
    '''
    This is the Threshold graph
    '''
    NovelCoeff = 1
    for i in log_scale:
        NovelThresh = i
        # title = 'ParamSweep3ETC' + str(Epsilon) + str(NovelThresh) + str(NovelCoeff) + '.csv'
        title = 'ParamSweep3ETC' + str(Epsilon) + str(NovelThresh)+ str(NovelCoeff) + '.csv'
        # title = 'ExpParamSweepETC00.5' + str(i)
        avg_data = average_index(title)
        run_average.append(avg_data)
        print('.')

    fig = plt.figure()
    plotting_on_the_same_thing2(run_average)
    '''
    This is for treating the baseline tests: 
    '''
    # fig = plt.figure()
    eps_baseline = average_index('Benchmark_egreedy.csv')
    ax, = plt.plot(range(len(eps_baseline)),eps_baseline,'--', label='epsilon')
    # plt.yscale('log')
    # sns.set()
    # sns.set_style('white')
    # sns.set_style('ticks')
    # sns.despine()
    # plt.title('Baseline')
    # plt.ylabel('Average reward per episode')
    # plt.xlabel('Episode')
    plt.legend()
    plt.show()
    pass