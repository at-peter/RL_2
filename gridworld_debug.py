import qAgentgrid as agent
import gridworld as grid
import numpy as np 
import random 
import utils

max_steps = 1000
num_episodes = 1000
num_runs = 1
avg_reward = np.zeros(num_episodes)

grid.env_init()
agent.agent_init()

is_terminal = False
start_state = grid.env_start()
l_action = agent.agent_start(start_state)

grid.current_state = [8,8]
agent.prev_action = 2
agent.prev_state = [9,8]
# state = grid.env_step(1)
agent.agent_end(1)

grid.current_state = [8,8]
agent.prev_action = 2
agent.prev_state = [9,8]

grid.current_state = [8,8]
agent.prev_action = 2
agent.prev_state = [9,8]
# state = grid.env_step(1)

agent.agent_end(1)
print(agent.Q)
utils.heatmap(agent.Q,2)
utils.pltshow()

