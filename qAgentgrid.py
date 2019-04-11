import random
import numpy as np 
'''
This is the basic q leaning agent 
Initially I will set this random action 

'''
random.seed(4)
Q = None
prev_state = None
prev_action = None 
alpha = 0.1
gamma = 0.9
epsilon = 0.1

def agent_init():
    global Q
    Q = np.zeros([10,10,4])
    return 


def agent_start(state):
    global Q, prev_state, prev_action
    action = random.randint(0,3) 
    prev_action = action
    prev_state = state
    return action 


def agent_step(reward, state):
    global Q, prev_state, prev_action, alpha, gamma , epsilon
    # update q based on previous action
    td_err = alpha*(reward + gamma* np.amax(Q[state[0], state[1], :]) - Q[prev_state[0],prev_state[1],prev_action])
    Q[prev_state[0], prev_state[1], prev_action] = Q[prev_state[0], prev_state[1], prev_action] + td_err
    print(td_err)
   
    # choose action based on policy 
    # epsilon greedy policy: 
    gen = random.randint(0, 100)
    
    if gen <= (epsilon*10): 
        action = random.randint(0,3)
        # Random policy   
        # print("Random action", action)
    else: 
        # Action selection 
        best_option = np.argwhere(Q[state[0],state[1],:] == np.amax(Q[state[0],state[1],:]))
        num_options = len(best_option)
        best_option = (random.choice(best_option))
        action = best_option[0]
        #print("Q action", action)
    prev_action = action 
    prev_state = state 
    
    return action 

def agent_end(reward):
    global Q, prev_state, prev_action
    term_state = [0,0]
    td_err = alpha*(reward + gamma* np.amax(Q[prev_state[0], prev_state[1], :]))
    Q[prev_state[0], prev_state[1], prev_action] = Q[prev_state[0], prev_state[1], prev_action] + td_err
    
    if prev_action == 0:
        term_state[0] = prev_state[0]
        term_state[1] = prev_state[1] - 1 
    elif prev_action == 1: 
        term_state[0] = prev_state[0] + 1
        term_state[1] = prev_state[1]
    elif prev_action == 2: 
        term_state[0] = prev_state[0]
        term_state[1] = prev_state[1] + 1
    elif prev_action == 3: 
        term_state[0] = prev_state[0] - 1
        term_state[1] = prev_state[1]
    #TODO: Need to have this line be able to accept multiple terminal states
    
    Q[term_state[0], term_state[1], prev_action] = Q[term_state[0], term_state[1], prev_action] + reward
    
    
    # print("termination acheived, Reward received:", reward, '\n', 'termination state:', prev_state )
    # print('Q matrix:', Q)
    return 

def agent_cleanup():
    print('value function:' ,Q)
    # print('Goal 2 value function:', Q[4,4])
    return 

def agent_message(in_message):

    return  ""

    
def predictive_novelty():

    '''
    This function will implement predictive novelty motivation as described in P.Y.Oudeye
    Variables needed: 
    previous estimate 
      
    
    '''
    
    return