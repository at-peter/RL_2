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
    action = random.randint(0,1) # This is what causes the single action to the end. 
    prev_action = action
    prev_state = state
    return action 


def agent_step(reward, state):
    global Q, prev_state, prev_action, alpha, gamma , epsilon
    # update q based on previous action
    td_err = alpha*(reward + gamma* np.amax(Q[state[0], state[1], :]) - Q[prev_state[0], prev_state[1], prev_action])
    Q[prev_state[0], prev_state[1], prev_action] = Q[prev_state[0], prev_state[1], prev_action] + td_err
    print(td_err)
    # 
    # td_err  = alpha*(reward + gamma*np.amax(Q[state,:] - Q[prev_state, prev_action])) 
    # Q[prev_state, prev_action] = Q[prev_state, prev_action] + td_err
    
    # choose action based on policy 
    # epsilon greedy policy: 
    gen = random.randint(0, 100)
    
    if gen <= (epsilon*10): 
        action = random.randint(0, 1) # Random policy   
        print("Random action", action)
    else: 
        
        best_option = np.argwhere(Q[state[0], state[1], :] == np.amax(Q[state[0], state[1], :])) #TODO I think this will work. maybe 
        num_options = len(best_option)
        best_option = (random.choice(best_option))
        action = best_option[0]
        print("Q action", action)
    
    prev_action = action 
    prev_state = state 
    
    return action 

def agent_end(reward):
    global Q, prev_state, prev_action
    # Q[prev_state[0], prev_state[1], prev_action] = Q[prev_state[0], prev_state[1], prev_action] + alpha*(reward) #TODO: m
    # TODO: this needs to be changed 
    '''
    TODO: Terminal state problem. now the agent end needs to check which terminal state we are in.
    need to update the state based on the action and then perform the 
    '''

    # if prev_action == 
    # term_state = []

    td_err  = alpha*(reward + gamma*np.amax(Q[0,4,:] - Q[prev_state[0],prev_state[1], prev_action])) 
    Q[prev_state[0], prev_state[1] ,prev_action] = Q[prev_state[0], prev_state[1], prev_action] + td_err

    # now update the state based on the prev action and perform the final update. 
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

    
