'''
This is my debugging file:" 


'''

import gridworld as grid 
import basicAgent as agent

grid.env_init()
print('Grid initialized ')
agent.agent_init()
print('Agent initialized ')
start = grid.env_start()
print('Start location: ',start)
action = agent.agent_start(start)
result = grid.env_step(action)
print('Action:', action,'\nResult: ', result)