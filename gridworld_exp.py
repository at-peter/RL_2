#!/usr/bin/env python

'''
This is the file that will be run for the gridworld experiment

This currently is just a skeleton 

'''

import qAgentgrid as agent
import gridworld as grid
import numpy as np 
import random 
import utils


max_steps = 1000
num_episodes = 500
num_runs = 5
avg_reward = np.zeros(num_episodes)

run_array = []

for run in range(num_runs):
    grid.env_init()
    agent.agent_init()
    print('Run:', run)
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
             
            if result['isTerminal'] is False:
                # Step through the agent  
                l_action = agent.agent_step(result['reward'], result['state'])
                # This is where the IM section will be 
                im_diff.append(10*(agent.predictive_novelty(result['state']))) 
                # Increment the step countet
                num_steps += 1 
                print('.', end = '')
            else:   
                agent.agent_end(result['reward'])
                break

        # if episode % 10 == 0: #TODO: This prints one in 10 graphs. 
            # utils.predictive_novelty_plot(im_diff, episode)
        avg_reward[episode] = result['reward']/num_steps
        print('\n number of steps: ', num_steps)
        # print(im_diff)
        episode += 1
    # utils.heatmap(agent.Q,run)
    # 
    # Start storing values in the run array 
    run_array.append(avg_reward) 
    utils.__do_the_HeMAN_2(agent.Q, run)
# print(avg_reward)
utils.avg_reward(avg_reward, run)
utils.pltshow()
# utils.heatmap(agent.Q)
