from keras import Sequential
from keras.layers import Dense, Conv2D, Flatten

# TODO: Implement experience replay; Train after filling experience buffer?
# TODO: Implement epsilon greedy strategy deciding balancing exploration (random action) vs exploitation
# TODO: Implement neural network, taking game state/board as input (with stacking)
# TODO: Output is Q-value for each possible action.
# TODO: Q-Target function used in loss function. Q-target is maximum possible Q for next state
from pacman.actions import Action


class DeepQ:
    def __init__(self):
        self.rewards = []  # Fix reward structure
        self.states = []  # Fix state structure

        self.model = Sequential()

        self.model.add(Conv2D(filters=32,
                              kernel_size=[4, 4],
                              input_shape=(7, 20),
                              activation='relu'))  # TODO: Get shape dynamically

        # TODO: Batch Normalization?
        self.model.add(Flatten())
        self.model.add(Dense(512))

        output_layer_length = len(Action.get_all_actions())
        self.model.add(Dense(output_layer_length))  # Output layer

        self.model.compile(optimizer='adam',
                           loss='mse',

                           )