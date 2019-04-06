import random
import numpy as np 
'''
This is the basic q leaning agent 
Initially I will set this random action 

'''
random.seed(5)
Q = None
prev_state = None
prev_action = None 
alpha = 0.1
gamma = 0.9
epsilon = 0.1

def agent_init():
    global Q
    # Q = np.zeros([5,5,4])
    Q = np.zeros([5,2])

    return 


def agent_start(state):
    global Q, prev_state, prev_action
    # action = random.randint(0,3)
    action = random.randint(0,1)
    prev_action = action
    prev_state = state
    return action 


def agent_step(reward, state):
    global Q, prev_state, prev_action, alpha, gamma , epsilon
    # update q based on previous action
    # td_err = alpha*(reward + gamma* np.amax(Q[state[0], state[1], :]))
    # Q[prev_state[0], prev_state[1], prev_action] = Q[prev_state[0], prev_state[1], prev_action] + td_err
    
    td_err  = alpha*(reward + gamma*np.amax(Q[state,:] - Q[prev_state, prev_action])) 
    Q[prev_state, prev_action] = Q[prev_state, prev_action] + td_err
    # choose action based on policy 
    # epsilon greedy policy: 
    gen = random.randint(0, 100)
    
    if gen <= (epsilon*10): 
        action = random.randint(0, 1) # Random policy   
        print("Random action", action)
    else: 
        # action = np.argmax(Q[state[0], state[1], :])  #TODO: This is still not giving the right value all the time. 
        # TODO: Need to restric the best option to the current state, Can't select the action from the pool of all the states. 
        best_option = np.argwhere(Q == np.amax(Q[state,:]))
        num_options = len(best_option)
        best_option = (random.choice(best_option[:][state,:]))
        action = best_option
        print("Q action", action)
    prev_action = action 
    prev_state = state 
    # print('Q matrix:', Q) 
    return action 

def agent_end(reward):
    global Q, prev_state, prev_action
    # Q[prev_state[0], prev_state[1], prev_action] = Q[prev_state[0], prev_state[1], prev_action] + alpha*(reward) #TODO: m
    
    Q[0, prev_action] = Q[0, prev_action] + reward
    
    print("termination acheived, Reward received:", reward, '\n', 'termination state:', prev_state )
    print('Q matrix:', Q)
    return 

def agent_cleanup():
    print('value function:' ,Q)
    # print('Goal 2 value function:', Q[4,4])
    return 

def agent_message(in_message):

    return  ""


'''
TODO: WHY IS THIS STILL HERE 
'''
# max_steps = 100000
# num_steps = 0
# line.env_init()
# agent.agent_init()
# is_terminal = False
# start_state = line.env_start()
# l_action = agent.agent_start(start_state)
# print(l_action)
# while not is_terminal:
#     result = line.env_step(l_action)
#     is_terminal = result['isTerminal']
    
#     if result['isTerminal'] is False: 
#         l_action = agent.agent_step(result['reward'], result['state'])
#         num_steps += 1 
#     else:
#         agent.agent_step(result['reward'],result['state'])
#         agent.agent_end(result['reward'])
#         break
        
    
