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
num_episodes = 3
num_runs = 1
for run in range(num_runs):
    grid.env_init()
    agent.agent_init()
    print('Run:', run)
    
    for episode in range(num_episodes):
        is_terminal = False
        start_state = grid.env_start()
        l_action = agent.agent_start(start_state)
        num_steps = 0  
        print('Episode:', episode) 
        print(l_action)
        while not is_terminal:
            result = grid.env_step(l_action)
            is_terminal = result['isTerminal']
            
            if result['isTerminal'] is False: 
                l_action = agent.agent_step(result['reward'], result['state'])
                num_steps += 1 
            else:
                # agent.agent_step(result['reward'],result['state'])
                agent.agent_end(result['reward'])
                break
        episode += 1 

utils.heatmap(agent.Q, 1 )

