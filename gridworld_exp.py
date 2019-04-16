#!/usr/bin/env python

'''
This is the file that will be run for the gridworld experiment

This currently is just a skeleton 

'''
import datetime
import time
import qAgentgrid as agent
import gridworld as grid
import numpy as np 
import random 
import utils
import pandas as pd
from matplotlib import pyplot as plt 

max_steps = 1000
num_episodes = 8000
num_runs = 100
# avg_reward = np.zeros((num_episodes,max_steps))
avg_reward = []
run_array = []
# tstart = datetime.datetime.now().timestamp()
# utils.random_seed(10)
title = 'Benchmark_egreedy'
for run in range(num_runs):
    # initialize all the values for each run 
    grid.env_init()
    agent.agent_init()
    print('Run:', run)
    # random.seed() # This line makes true random action selection. 
    utils.random_seed(run)
    # TODO: Make a way for the figures to be stored over multiple runs. 
    for episode in range(num_episodes):
        '''
        Initialize for each episode
        '''
        im_diff = [] 
        is_terminal = False
        start_state = grid.env_start()
        l_action = agent.agent_start(start_state)
        step_count = 0  
        # print('Episode:', episode)
        average_reward_per_episode = 0 
        prev_mean_val = 0 
    
        while not is_terminal:
            '''
            This is where each step happens 
            '''
            # Increment the step count
            step_count += 1  
            # Step through the environment 
            result = grid.env_step(l_action)
            is_terminal = result['isTerminal']
           
            average_reward_per_episode = (((step_count - 1)* prev_mean_val) + result['reward']) / step_count
            

            prev_mean_val = average_reward_per_episode

            if result['isTerminal'] is False:
                # Step through the agent  
                l_action = agent.agent_step(result['reward'], result['state'])
                # This is where the IM section will be 
                #im_diff.append(10*(agent.predictive_novelty(result['state']))) 
                 
                
            else:   
                agent.agent_end(result['reward'])
                

        # if episode % 10 == 0: #TODO: This prints one in 10 graphs. 
            # utils.predictive_novelty_plot(im_diff, episode)
        # avg_reward[episode] = average_reward_per_episode
        avg_reward.append(average_reward_per_episode)
        # print('\n number of steps: ', step_count)
        episode += 1
    # utils.heatmap(agent.Q,run)
    
    
    # utils.avg_reward(avg_reward, run)
    # Start storing values in the run array 
    # run_array.append(avg_reward) 
    # run_array_np = np.array(run_array)
    # utils.__do_the_HeMAN_2(agent.Q, run)
    run_array.append(('run ' + str(run), avg_reward.copy())) # this preps for the dataframe 
    # this is where the average reward plots will go 
    utils.avg_reward(avg_reward, run)
    avg_reward.clear()

run_frame = pd.DataFrame.from_items(run_array)
# print(run_frame.head())

# run_frame.plot()
# utils.save_to_pdf('Benchmark_epsilon')
utils.save_to_pdf(title)

run_frame.to_csv(title + '.csv')
# utils.heatmap(agent.Q)
# data = pd.DataFrame(run_array_np.T, columns = range(num_runs), index = range(num_episodes))
# data.plot()
# print(data.head) 
# utils.pltshow()
# # Reshape the run array: 


# save_str = str(agent.novelty_coeff) +'_' + str(agent.novelty_thresh) + '_' + str(num_runs) + '_' + str(num_episodes)
# np.savetxt('average_reward_' + save_str ,run_array_np, delimiter = ',')

'''
Time stuff: This really should be a utils function. 
'''
# t_end = datetime.datetime.now().timestamp()
# tspent = tstart-t_end
# print("Simulation time: " + str(tspent)