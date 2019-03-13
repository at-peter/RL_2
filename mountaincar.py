
'''
The mountain car environment that is given in chapter 11.

Bound operation: 
velocity is bound between -0.07 and 0.07 
position is bounded between -1.2 and 0.05 

Mechanics: 
x_(t+1) = bound[x_t + xdot_(t+1)]
xdot_(t+1) = bound[xdot_t + 0.001A_t - 0.0025cos(3x_t)]

actions: 
full throttle A = 1 
full reverse A = -1 
Nothing A = 0 

Initialization: 
- position = [-0.6, -0.4)
- velocity = 0

Reward: 
R = -1 on all timesteps unless 
    - x_t = 0.5 


Tiling: 
- 8 tiles 

iht = IHT(4096) 
tiles(iht, 8 , [8*x/(0.5+1.2), 8*xdot/(0.07+0.07)],a) -- this will give the indicies of the ones in the feature vector for the state (x,xdot) and action A 

'''

import random
import numpy as np

current_state = None 

def env_init():
    global current_state
    '''
    This function initializes the environment 
    '''
    return None

def env_start():
    global current_state 
    '''
    This function starts the environment; 

    '''
    x = random.uniform(-0.6, -0.4)
    xdot = 0 

    current_state = np.asarray([x,xdot])
    return current_state


def env_step(action):
    global current_state
    '''
    This function steps the environment
    Result should be a dictionary with the following keys: 
    {reward, state, isTerminal}
    
    Actions are either 1, -1 or 0
    '''
    a_t = action 

    #TODO: environment mechanics 

    result = {'reward': , 'state': , 'isTerminal':is_terminal}

    return result 

def env_cleanup():
    return 

def env_message(in_message):
    return ""