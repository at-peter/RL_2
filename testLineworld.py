from rl_glue import*

RLGlue("lineworld","qAgent")
import lineworld as grid 
import qAgent as agent
import lineworld as line 

import numpy as np 
import random 

random.seed(5)

'''
Agent hand testing
'''
grid.env_init()
agent.agent_init()
start = grid.env_start()

# # episode 1 
# print('Episode 1')
# r1 = grid.env_step(0)
# A2 = agent.agent_step(r1['reward'],r1['state'])
# print("First step:", r1, A2)
# r2 = grid.env_step(0)
# print('r2', r2)
# At = agent.agent_step(r2['reward'],r2['state'])
# # At = agent.agent_end(r2['reward'])
# print('Second step:', r2, At)
# term = agent.agent_end(1)
# # print(agent.Q)
# print('Episode 1 last action:',agent.last_action, 'Last state', agent.last_state)
## Episode 2 

# print('Episode 2')
# start2 = grid.env_start()
# print('state:', agent.last_state, 'action', agent.last_action)
# agStart = agent.agent_start(start2)
# r1 = grid.env_step(0)
# print('state:', agent.last_state, 'action', agent.last_action)
# A2 = agent.agent_step(r1['reward'],r1['state'])
# print('state:', agent.last_state, 'action', agent.last_action)
# print("First step:", r1, A2)
# r2 = grid.env_step(0)
# print('r2', r2)
# At = agent.agent_step(r2['reward'],r2['state'])
# # At = agent.agent_end(r2['reward'])
# print('Second step:', r2, At)
# term = agent.agent_end(1)

# #
# print('Episode 3')
# start2 = grid.env_start()
# start4 = agent.agent_start(start2)
# r1 = grid.env_step(0)
# A2 = agent.agent_step(r1['reward'],r1['state'])
# print("First step:", r1, A2)
# r2 = grid.env_step(0)
# print('r2', r2)
# At = agent.agent_step(r2['reward'],r2['state'])
# # At = agent.agent_end(r2['reward'])
# print('Second step:', r2, At)
# term = agent.agent_end(1)


'''
RL glue testing. 
'''
num_episodes = 2
max_steps = 100000
num_runs = 1

# for run in range(num_runs):
#     counter = 0 
#     RL_init()
#     print('\n')

#     for episode in range(num_episodes):
#         RL_episode(max_steps)
#     RL_cleanup()

# for run in range(num_runs):
#     line.env_init()
#     agent.agent_init()

#     for episode in range(num_episodes):
#         start_env = line.env_start()
#         l_action = agent.agent_start(start_env)
#         is_terminal = False
#         num_steps = 1
#         while (not is_terminal) and ((max_steps == 0) or (num_steps < max_steps)):
            
#             result = line.env_step(l_action)

#             if result['isTerminal'] == True: 
#                 agent.agent_end(result['reward'])

#             else: 
#                 l_action = agent.agent_step(result['reward'], result['state'])
#                 num_steps += 1 
            
#             is_terminal = result['isTerminal']



# max_steps = 100000
# num_steps = 0
# line.env_init()
# agent.agent_init()
# is_terminal = False
# start_state = line.env_start()
# l_action = agent.agent_start(start_state)
# while not(is_terminal):
#     result = line.env_step(l_action)
    
#     if result['isTerminal'] == True: 
#         agent.agent_end(result['reward'])
#         break
#     else: 
#         l_action = agent.agent_step(result['reward'], result['state'])
#         num_steps += 1 
#     is_terminal = result['isTerminal']

# is_terminal = False
# start_state = line.env_start()
# l_action = agent.agent_start(start_state)
# while not(is_terminal):
#     result = line.env_step(l_action)
    
#     if result['isTerminal'] == True: 
#         agent.agent_end(result['reward'])
#         break
#     else: 
#         l_action = agent.agent_step(result['reward'], result['state'])
#         num_steps += 1 
#     is_terminal = result['isTerminal']


# is_terminal = False
# start_state = line.env_start()
# l_action = agent.agent_start(start_state)
# while not(is_terminal):
#     result = line.env_step(l_action)
    
#     if result['isTerminal'] == True: 
#         agent.agent_end(result['reward'])
#         break
#     else: 
#         l_action = agent.agent_step(result['reward'], result['state'])
#         num_steps += 1 
#     is_terminal = result['isTerminal']


max_steps = 100000
num_steps = 0
num_episodes = 10

for run in range()
    line.env_init()
    agent.agent_init()

    for episode in range(num_episodes):
        is_terminal = False
        start_state = line.env_start()
        l_action = agent.agent_start(start_state)

        print(l_action)
        while not is_terminal:
            result = line.env_step(l_action)
            is_terminal = result['isTerminal']
            
            if result['isTerminal'] is False: 
                l_action = agent.agent_step(result['reward'], result['state'])
                num_steps += 1 
            else:
                agent.agent_step(result['reward'],result['state'])
                agent.agent_end(result['reward'])
                break
        episode += 1 



