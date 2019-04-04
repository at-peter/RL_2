import random
import numpy as np 
'''
This is the basic q leaning agent 
Initially I will set this random action 

'''
random.seed(5)
Q = None
last_state = None
last_action = None 
alpha = 0.1
gamma = 0.9
epsilon = 0.1

def agent_init():
    global Q
    # Q = np.zeros([5,5,4])
    Q = np.zeros([5,2])

    return 


def agent_start(state):
    global Q, last_state, last_action
    # action = random.randint(0,3)
    action = random.randint(0,1)
    last_action = action
    last_state = state
    return action 


def agent_step(reward, state):
    global Q, last_state, last_action, alpha, gamma 
    # update q based on previous action
    # td_err = alpha*(reward + gamma* np.amax(Q[state[0], state[1], :]))
    # Q[last_state[0], last_state[1], last_action] = Q[last_state[0], last_state[1], last_action] + td_err
    
    td_err  = alpha*(reward + gamma*np.amax(Q[state,:] - Q[last_state, last_action])) 
    Q[last_state, last_action] = Q[last_state, last_action] + td_err
    # choose action based on policy 
    # epsilon greedy policy: 
    gen = random.randint(0, 100)
    
    if gen <= 10: 
        action = random.randint(0, 1) # Random policy   
        # print("Random action")
    else: 
        # print("Q action")
        # action = np.argmax(Q[state[0], state[1], :])  #TODO: need to use numpy.argwhere here. This is to get rid of the bias that is created by using argmax()
        best_option = np.argwhere(Q == np.amax(Q[state,:]))
        num_options = len(best_option)
        best_option = (random.choice(best_option))
        action = best_option[1]
    
    last_action = action 
    last_state = state 
    # print('Q matrix:', Q) 
    return action 

def agent_end(reward):
    global Q, last_state, last_action
    # Q[last_state[0], last_state[1], last_action] = Q[last_state[0], last_state[1], last_action] + alpha*(reward) #TODO: m
    
    Q[0, last_action] = Q[0, last_action] + reward
    
    print("termination acheived, Reward received:", reward, '\n', 'termination state:', last_state )
    print('Q matrix:', Q)
    return 

def agent_cleanup():
    print('value function:' ,Q)
    # print('Goal 2 value function:', Q[4,4])
    return 

def agent_message(in_message):

    return  ""