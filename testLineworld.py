from rl_glue import*

RLGlue("lineworld","qAgent")
import lineworld as grid 
import qAgent as agent
 

import numpy as np 
import random 

random.seed(5)

grid.env_init()
agent.agent_init()
start = grid.env_start()
#agent = agent.agent_start()
# episode 1 
print('Episode 1')
r1 = grid.env_step(0)
A2 = agent.agent_step(r1['reward'],r1['state'])
print("First step:", r1, A2)
r2 = grid.env_step(0)
print('r2', r2)
At = agent.agent_step(r2['reward'],r2['state'])
# At = agent.agent_end(r2['reward'])
print('Second step:', r2, At)
term = agent.agent_end(1)
# print(agent.Q)

## Episode 2 
print('Episode 2')
start2 = grid.env_start()
r1 = grid.env_step(0)
A2 = agent.agent_step(r1['reward'],r1['state'])
print("First step:", r1, A2)
r2 = grid.env_step(0)
print('r2', r2)
At = agent.agent_step(r2['reward'],r2['state'])
# At = agent.agent_end(r2['reward'])
print('Second step:', r2, At)
term = agent.agent_end(1)

#
print('Episode 3')
start2 = grid.env_start()
r1 = grid.env_step(0)
A2 = agent.agent_step(r1['reward'],r1['state'])
print("First step:", r1, A2)
r2 = grid.env_step(0)
print('r2', r2)
At = agent.agent_step(r2['reward'],r2['state'])
# At = agent.agent_end(r2['reward'])
print('Second step:', r2, At)
term = agent.agent_end(1)

# print(agent.Q)

# agent.Q[]
# steps = 10000
# for i in range(steps):
#     if results['isTerminal'] == True:
#         term = agent.agent_end(results['reward'])
#         break
#     action = agent.agent_step(results['reward'], results['state'])
#     results = grid.env_step(action)

# print('done')


# gamma = 0.1
# alpha = 0.1
# epsilon = 50

# num_episodes = 10
# max_steps = 100000
# num_runs = 4

# for run in range(num_runs):
#     counter = 0 
#     RL_init()
#     print('\n')
#     for episode in range(num_episodes):
#         RL_episode(max_steps)
#     RL_cleanup()