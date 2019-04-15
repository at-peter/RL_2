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


max_steps = 1000
num_episodes = 100
num_runs = 5
avg_reward = np.zeros((num_episodes,max_steps))

run_array = []
# tstart = datetime.datetime.now().timestamp()
# utils.random_seed(10)
for run in range(num_runs):
    grid.env_init()
    agent.agent_init()
    print('Run:', run)
    # utils.random_seed(num_runs)
    # TODO: Make a way for the figures to be stored over multiple runs. 
    for episode in range(num_episodes):
        im_diff = [] 
        is_terminal = False
        start_state = grid.env_start()
        l_action = agent.agent_start(start_state)
        num_steps = 0  
        print('Episode:', episode)
        
    
        while not is_terminal:
            # Step through the environment 
            result = grid.env_step(l_action)
            is_terminal = result['isTerminal']
            avg_reward[episode][num_steps] = (result['reward']/(num_steps+1))
            if result['isTerminal'] is False:
                # Step through the agent  
                l_action = agent.agent_step(result['reward'], result['state'])
                # This is where the IM section will be 
                im_diff.append(10*(agent.predictive_novelty(result['state']))) 
                # Increment the step counter
                num_steps += 1 
                print('.', end = '')
            else:   
                agent.agent_end(result['reward'])
                break

        # if episode % 10 == 0: #TODO: This prints one in 10 graphs. 
            # utils.predictive_novelty_plot(im_diff, episode)
        # avg_reward[episode] = result['reward']/num_steps
        # print('\n number of steps: ', num_steps)
        # print(im_diff)
        episode += 1
    # utils.heatmap(agent.Q,run)
    # 
    # Start storing values in the run array 
    run_array.append(avg_reward) 
    run_array_np = np.array(run_array)
    utils.__do_the_HeMAN_2(agent.Q, run)
print(avg_reward)
# utils.avg_reward(avg_reward, run)
# utils.pltshow()
# utils.heatmap(agent.Q)
# data = pd.DataFrame(run_array_np.T, columns = range(num_runs), index = range(num_episodes))
# data.plot()
# print(data.head) 
# utils.pltshow()
# # Reshape the run array: 


# save_str = str(agent.novelty_coeff) +'_' + str(agent.novelty_thresh) + '_' + str(num_runs) + '_' + str(num_episodes)
# np.savetxt('average_reward_' + save_str ,run_array_np, delimiter = ',')
# t_end = datetime.datetime.now().timestamp()
# tspent = tstart-t_end

# print("Simulation time: " + str(tspent)