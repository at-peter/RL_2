'''
This is the agent debugging environement in wich I will be testing if the agent learns properly. 
'''

import numpy as np 

current_state = None
terminal_state = None
terminal_reward = None


def env_init():
    global terminal_state, terminal_reward
    terminal_reward = 1 
    terminal_state = 0
    return 

def env_start():
    global current_state
    start_state = 2
    current_state = start_state
    return start_state 

def env_step(action):
    global current_state
    '''
    line world: 
    straight line with termination on the end. 
    Reward is 0 on all steps until termination where reward is 1 
    '''
    # action selection: 
    if action == 0: 
        # go left: 
        current_state = current_state - 1 
    if action == 1: 
        # go right
        current_state = current_state + 1 
        
    #TODO: need to make the wall code:
    if current_state == 5:
        current_state = 4

    reward = 0 
    is_terminal = False
    # terminal condition: 
    if current_state == 0: 
        is_terminal = True
        reward = 1 
        current_state = 0

    results = {'reward': reward , 'state': current_state , 'isTerminal': is_terminal } # TODO: put values here 
    return results 

def env_cleanup():

    return

def env_message(in_message):
    
    return "" 
