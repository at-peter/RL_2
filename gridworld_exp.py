#!/usr/bin/env python

'''
This is the file that will be run for the gridworld experiences 

This currently is just a skeleton 
~20$ 
'''

from rl_glue import* 
RLGlue("gridworld","basicAgent")

import numpy as np 
import pickle

if __name__ == "__main__":
    num_episodes = 8000
    max_steps = 10000

    num_runs = 10

    key_episodes = [99,999,7999]


    for run in range(num_runs):
        counter = 0 
        print("run number: ", run)
        RL_init()
        print('\n')
        for episode in range(num_episodes):
            RL_episode(max_steps)
            
        RL_cleanup()

