import numpy as np


'''
This is where I will be making the stochastic gridworld environement. 

Environment mechanics: 
- start position -- this could be hardcoded but may also be worth looking into the idea of having the starting positions also stochastic
- goal position -- there will be many goals that are fairly easy to find, but they are not always there. They will stochastically happen. 


'''
current_state = None
def env_init():
    global current_state
    #setting up gridworld 
    gridworldMap = np.zeros((5,5))
    
    # se
    return

def env_start():
    # set the starting location 
    return 

def env_step(action):
    global current_state
    new_state = []
    # action logic should go here 
    '''
    Check if current state is at a wall
        Walls are:
        - top = [:,0]
        - Right = [4,:]
        - bottom = [:,4]
        - Left = [0,:]
    Perform action 
    update state 
    check if state is terminal 
    get reward depending on if you are terminal or not. 
    
    '''
    # WALL PHASE: 

    if current_state

    # ACTION PHASE: 
    if action = 1: 
        # up
        new_state[0] = current_state[0]
        new_state[1] = current_state[1] + 1 
    
    elif action = 2:
        # right
        new_state[0] = current_state[0] + 1 
        new_state[1] = current_state[1] 
    
    elif action = 3:
        # down 
        new_state[0] = current_state[0]
        new_state[1] = current_state[1] - 1  
    
    elif action = 4:
        # left  
        new_state[0] = current_state[0] - 1
        new_state[1] = current_state[1] 
    
    else: 
        print('Not a valid action')

    #UPDATE PHASE: 
    current_state = new_state 

    #TERMINAL PHASE: 
    if current_state = terminal_1 or current_state = terminal_2 




    results = {'reward': ,'state': , 'isTerminal': }
    return results 

def env_cleanup():

    return 

def env_message(in_message):
    return ""