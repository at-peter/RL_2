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
num_episodes = 1000
num_runs = 1
avg_reward = np.zeros(num_episodes)
for run in range(num_runs):
    grid.env_init()
    agent.agent_init()
    print('Run:', run)
    
    for episode in range(num_episodes):
        print('.')
        is_terminal = False
        start_state = grid.env_start()
        l_action = agent.agent_start(start_state)
        num_steps = 0  
        print('Episode:', episode) 
        # print(l_action)
        counter = 0
    
        while not is_terminal:
            result = grid.env_step(l_action)
            # print(result)
            is_terminal = result['isTerminal']
            counter += 1 
            if result['isTerminal'] is False: 
                l_action = agent.agent_step(result['reward'], result['state'])
                num_steps += 1 
            else:
                # agent.agent_step(result['reward'],result['state'])
                agent.agent_end(result['reward'])
                break
            # if counter is max_steps:
            #     print('Max steps achieved')
            # #     # TODO: For some reason this happens alot. 
            #     break
        avg_reward[episode] = result['reward']/counter
        # utils.heatmap(agent.Q, episode)
        print(counter)
        episode += 1
    # utils.heatmap(agent.Q,run) 
    utils.__do_the_HeMAN_2(agent.Q,run)
# print(avg_reward)
utils.avg_reward(avg_reward)
utils.pltshow()
# utils.heatmap(agent.Q)
