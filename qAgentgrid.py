import random
import numpy as np
import utils 
'''
This is the basic q leaning 


'''
# system parameters 
# utils.random.seed(10)
Q = None
prev_state = None
prev_action = None 
alpha = 0.1
gamma = 0.9
# epsilon = None
# Drive tuneing: 
# novelty_thresh = 0.5 # This value is being subtracted from the sig Q
# novelty_coeff = 2 # this is the scale factor 

def agent_init(Epsilon, Novelty_coeff, Novelty_thresh):
    global Q, epsilon, novelty_coeff, novelty_thresh
    Q = np.zeros([10,10,4])
    epsilon = Epsilon
    novelty_coeff = Novelty_coeff
    novelty_thresh = Novelty_thresh
    return 


def agent_start(state):
    global Q, prev_state, prev_action
    action = random.randint(0,3) 
    prev_action = action
    prev_state = state
    return action 


def agent_step(reward, state):
    '''
    This is the Q learning algorithm with 
    '''
    global Q, prev_state, prev_action, alpha, gamma , epsilon
    # update q based on previous action  
    td_err = alpha*(reward + gamma* np.amax(Q[state[0], state[1], :]) - Q[prev_state[0],prev_state[1],prev_action])
    Q[prev_state[0], prev_state[1], prev_action] = Q[prev_state[0], prev_state[1], prev_action] + td_err

    # epsilon greedy policy: 
    gen = random.randint(0, 100)
    if gen <= (epsilon*10): 
        # Random policy
        action = random.randint(0,3)
        
    else: 
        # MaxA Q Action selection 
        best_option = np.argwhere(Q[state[0],state[1],:] == np.amax(Q[state[0],state[1],:]))
        num_options = len(best_option)
        best_option = (random.choice(best_option))
        action = best_option[0]

    # Save the state action pair for the next iteration 
    prev_action = action 
    prev_state = state 
    return action 

def agent_end(reward):
    global Q, prev_state, prev_action
    term_state = [0,0] #init the terminal state
    
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
    
    td_err = alpha*(reward + gamma* np.amax(Q[term_state[0], term_state[1], :]) - Q[prev_state[0], prev_state[1], prev_action])
    Q[prev_state[0], prev_state[1], prev_action] = Q[prev_state[0], prev_state[1], prev_action] + td_err
    
    # Update the p
    # Q[term_state[0], term_state[1], prev_action] = Q[term_state[0], term_state[1], prev_action] + reward
    Q[term_state[0], term_state[1], prev_action] = reward
    
    
    # print("termination acheived, Reward received:", reward, '\n', 'termination state:', prev_state )
    #print('Q matrix:', Q)
    return 

def agent_cleanup():
    print('value function:' ,Q)
    # print('Goal 2 value function:', Q[4,4])
    return 

def agent_message(in_message):

    return  ""

    
def predictive_novelty(state):
    global Q, prev_state, prev_action, novelty_coeff, novelty_thresh
    
    '''
    This function will implement predictive novelty motivation as described in P.Y.Oudeye
    Variables needed: 
    previous estimate 

    CURRENT ESTIMATE: THIS WILL BE PULLED FROM THE q VALUE  
        this value will be then passed to the sigmoid function to get   
    '''
    # Find the next best action based om the current state
    best_option = np.argwhere(Q[state[0],state[1],:] == np.amax(Q[state[0],state[1],:]))
    num_options = len(best_option)
    best_option = (random.choice(best_option))
    action = best_option[0]
    diff_array = np.zeros([4])
    
    # this finds the new values for all the states. 
    for a in range(len(Q[state[0], state[1], :])):
        diff_array[a] = utils.sigmoid(Q[state[0], state[1], a])
        Q[state[0],state[1], a] =+ (diff_array[a] - novelty_thresh)*novelty_coeff
     
    #Feed the Q values to the sigmoid function. 
    prev_estimate = utils.sigmoid(Q[prev_state[0], prev_state[1], prev_action])
    this_estimate = utils.sigmoid(Q[state[0], state[1], action])
    
    # make an array of deltas 
    # print('Prev estimate ', prev_estimate)
    # print('This estimate ', this_estimate)
    # delta = this_estimate - prev_estimate
    diff_array = diff_array - 0.5
    #print('Predictive novelty:', diff_array)
    delta = diff_array.max()

    # lets see what happens if I add this to the Q values? 
    
    return delta