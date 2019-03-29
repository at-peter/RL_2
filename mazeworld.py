'''

'''

import numpy as np 

current_state = None
terminal_1 = None
terminal_2 = None
R_1 = None 
R_2 = None

def env_init():
    global current_state, terminal_1,terminal_2
    
    terminal_1 = [4,0]
    terminal_2 = [4,4]
    return 

def env_start():
    global R_1, R_2 , current_state
    start_state = [0,2]
    R_1 = np.random.normal(4,1)
    R_2 = np.random.normal(7,2)
    current_state = start_state 
    '''
    TODO: need to initialize the maze here for each of the runs. 
    '''
    return start_state 

def env_step(action):
    
     if action == 0: 
        # up
        new_state[0] = the_state[0]
        new_state[1] = the_state[1] - 1 
    
    elif action == 1:
        # right
        new_state[0] = current_state[0] + 1 
        new_state[1] = current_state[1] 
    
    elif action == 2:
        # down 
        new_state[0] = current_state[0]
        new_state[1] = current_state[1] + 1  
    
    elif action == 3:
        # left  
        new_state[0] = current_state[0] - 1
        new_state[1] = current_state[1] 
    
    else: 
        print('Not a valid action')
    # Outer wall check;
    if new_state[1] == -1:
        new_state[1] = 0
    elif new_state[0] == -1: 
        new_state[0] = 0
    elif new_state[1] == 5: 
        new_state[1] = 4
    elif new_state[0] == 5:
        new_state[0] = 4
    
    '''
    The next section will deal with the maze walls.
    I will need to keep track of which sections of the maze are up for each run.
    TODO: The next section is to check the maze layout. 
    '''    
    
    results = {'reward': , 'state': , 'isTerminal': } # TODO: put values here 
    return results 

def env_cleanup():

    return

def env_message(in_message):
    
    return "" 
