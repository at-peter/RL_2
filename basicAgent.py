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

def agent_init():
    global Q
    Q = np.zeros([5,5,4])

    return 


def agent_start(state):
    global Q
    action = random.randint(1,4)
    return action 


def agent_step(reward, state):
    global Q, last_state, last_action 
    
    # choose action based on policy 

    # update q based on action taken 
    action = random.randint(1,4)
    return action 

def agent_end(reward):
    global Q, last_state

    return 

def agent_cleanup():

    return 

def agent_message(in_message):

    return  