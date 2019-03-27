'''
This is my debugging file:" 


'''
from rl_glue import*
RLGlue("gridworld","qAgent")
import gridworld as grid 
import qAgent as agent
import numpy as np 
import random 
Q = np.zeros([5,5,4])

reward = 5
gamma = 0.1
alpha = 0.1
epsilon = 50

num_episodes = 5
max_steps = 100000
num_runs = 2

for run in range(num_runs):
    counter = 0 
    RL_init()
    print('\n')
    for episode in range(num_episodes):
        RL_episode(max_steps)
    RL_cleanup()