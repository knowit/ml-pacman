from keras import Sequential
from keras.layers import Dense, Conv2D


# TODO: Implement experience replay; Train after filling experience buffer?
# TODO: Implement epsilon greedy strategy deciding balancing exploration (random action) vs exploitation
# TODO: Implement neural network, taking game state/board as input (with stacking)
    # TODO: Output is Q-value for each possible action.
# TODO: Q-Target function used in loss function. Q-target is maximum possible Q for next state

class DeepQ:
    def __init__(self):
        self.rewards = []  # Fix reward structure
        self.states = []  # Fix state structure

        self.model = Sequential()

        # self.conv1 = Conv2D(input_shape=)
        self.model.add(self.conv1)



