import utils

class intrinsicMotivation:

    def __init__(self, motivation_type):
        
        if motivation_type is 'Predictive Novelty':
            # make stuff for predictive novelty.


    def predictive_novelty(state, Q, prev_action, prev_state):
        best_option = np.argwhere(Q[state[0],state[1],:] == np.amax(Q[state[0],state[1],:]))
        num_options = len(best_option)
        best_option = (random.choice(best_option))
        action = best_option[0]
        prev_estimate = utils.sigmoid(Q[prev_state[0], prev_state[1], prev_action])
        this_estimate = utils.sigmoid(Q[state[0], state[1], action])

        delta = this_estimate - prev_estimate
        return delta 

    def predictive_novelty_thresh():

        return


