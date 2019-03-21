import random
import numpy as np 
'''
This is the basic agent 
Initially I will set this random action 

'''
Q = None
last_state = None
last_action = None 
alpha = 0.1
gamma = 0.1
epsilon = 0.1

def agent_init():
    global Q
    Q = np.zeros([5,5,4])

    return 


def agent_start(state):
    global Q, last_state, last_action
    action = random.randint(1,4)
    last_action = action
    last_state = state
    return action 


def agent_step(reward, state):
    global Q, last_state, last_action, alpha, gamma 
    # update q based on previous action
    Q[last_state[0],last_state[1],last_action] = Q[last_state[0],last_state[1],last_action] + alpha*(reward + gamma* np.amax(Q[state[0],state[1],:]))
    # choose action based on policy 
    # epsilon greedy policy: 
    gen = random.randint(0,100)
    
    if gen <= 10: 
        action = random.randint(1,4) # Random policy   
    else: 
        action = np.argmax(Q[0,1,:])
     
    last_action = action 
    last_state = state 
    print(action)
    return action 

def agent_end(reward):
    global Q, last_state, last_action,alpha, gamma
    Q[last_state[0],last_state[1],last_action] = Q[last_state[0],last_state[1],last_action] + alpha*(reward)
    print("termination acheived", reward)
    return 

def agent_cleanup():

    return 

def agent_message(in_message):

    return  