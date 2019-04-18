'''
This is the first refactor of the agent files that were used in this project. 
This time round classes will be used since then multi-agent settings will be possible 0w0
Start your engins for V2 
Start date: April 18th 2019
'''
import numpy as np
import utils

class agent:
    
    Q = None
    prev_state = 0
    prev_action = 0 
    alpha = None
    gamma = None
    
    def __init__(self,alg ,alpha = 0.1, gamma = 0.9 , epsilon = 0.1, ):
        '''
        This constructor will take the place of the agent.init() function in V1
        '''
        return
    
    def start():

        return 

    def step(self):

        if self.alg == 'qlearning':
        # Q learning update 
            td_err = alpha*(reward + self.gamma* np.amax(Q[state[0], state[1], :]) - Q[prev_state[0],prev_state[1],prev_action])
            self.Q[prev_state[0], prev_state[1], prev_action] = Q[prev_state[0], prev_state[1], prev_action] + td_err
            return
        
        else: 
        return
    
    def end(self):

        return

    def cleanup(self):

        return
   
    def policy(self, method, epsilon = 0.1):

        if method == 'egreedy':
            #epsilon greedy method

        return

    def function_approximation(self):


        return
    