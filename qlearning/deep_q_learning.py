import numpy as np

from copy import deepcopy
import pygame
from qlearning.exp_rep import ExperienceReplay
from qlearning.q_config import DeepQConfig
from qlearning.q_utils import calculate_reward_for_move, convert_action_to_int


from pacman.actions import Action
from pacman.game import Game
from pacman.gamelogic import ActionEvent, get_next_game_state_from_action
from keras import Sequential
from keras.layers import Dense
from keras.optimizers import sgd
from keras.models import load_model


class DeepQ(object):

    def __init__(self):
        self.config = DeepQConfig()
        self.model = self.init_model()
        self.exp_replay = ExperienceReplay()

    def init_model(self):

        # TODO: Make your own neural network with keras!
        pass

    def convert_state_to_input(self, state):

        # TODO: If you get confused by this, its ok... Ask Malte or Manu and we will try to explain :-)

        # TODO: Alright, you've gotten this far. Now the fun part starts.
        # TODO: We need somehow to represent a state. In q learning we held
        # TODO: a state as a key in dictionary which works when the __eq__ and __hash__ functions
        # TODO: are overwritten in the GameState object.

        # TODO: However that doesn't work with neural networks. Neural networks needs numerical inputs.
        # TODO: The easy way to do this is to one-hot-encode each
        # TODO: possible "map-element" (Like pacman, ghost, wall, etc), and
        # TODO: loop over each map-element and make a long list of integers of 1s and 0s.

        # TODO: The length of this list is therefore based on how big your pacman map is. Therefore the size of
        # TODO: the map will dictate the size of the input layer of your neural network.

        # TODO: When that is done you need to make sure the input layer of your neural network are of the exact same
        # TODO: length as this state-encoding. Therefore you need to make sure input_size in DeepQConfig is the same
        # TODO: size as the list you return from this method.

        pass

    def pick_optimal_action(self, state):

        # TODO: Do a prediction on the given state with the model you have.
        # TODO: Return the action with the highest score

        pass

    # Identical to q_learn
    def pick_action(self, game_state):
        exploration_prob = 0.20
        if exploration_prob > np.random.rand():
            # Explore
            return np.random.choice(Action.get_all_actions())
        else:
            # Exploit
            return self.pick_optimal_action(game_state)

    def train(self):

        # Very close to the training part of regular q_learning.

        game = Game('level-0')
        tot_loss = {}

        # TODO: change number of episodes needed for training.
        for i in range(1, self.config.episodes):

            loss = 0.

            iteration = 0

            done = False
            current_game_state = deepcopy(game.initial_game_state)

            while not done:

                action = self.pick_action(current_game_state)
                next_game_state, action_event = get_next_game_state_from_action(current_game_state, action.value)

                if action_event == ActionEvent.WON or action_event == ActionEvent.LOST:
                    done = True
                    if action_event == ActionEvent.WON:
                        print("Won!!")
                    else:
                        print('lost')

                reward = calculate_reward_for_move(action_event)

                states = [self.convert_state_to_input(current_game_state), convert_action_to_int(action), reward,
                          self.convert_state_to_input(next_game_state)]

                # We save the information about current_state, action, reward and next_state. In addition we need to
                # know if the game is over.
                self.exp_replay.remember(states=states, game_over=done)

                # Load batch of experiences
                inputs, targets = self.exp_replay.get_batch(model=self.model, batch_size=self.config.batch_size)

                # train model on experiences
                batch_loss = self.model.train_on_batch(inputs, targets)

                loss += batch_loss

                iteration += 1

                current_game_state = deepcopy(next_game_state)

            print(i)
            print(loss/iteration)

            tot_loss[i] = (loss/iteration)

        print(tot_loss)

        # plot_training_history(tot_loss)

        self.model.save('./models/nn_model.h5')

    def run_model(self, model_path='./models/nn_model.h5'):

        # Also closely related to the "runnable" part of regular q_learning

        # Get saved model
        self.model = load_model(model_path)
        game = Game('level-0')
        clock = pygame.time.Clock()
        game.init_screen()

        # TODO: Change how many times you want to see pacman play
        for i in range(10):

            current_game_state = deepcopy(game.initial_game_state)
            super_done = False

            while not super_done:

                action = self.pick_optimal_action(current_game_state)

                game.animate()

                next_game_state, action_event = get_next_game_state_from_action(current_game_state, action.value)

                if action_event == ActionEvent.WON or action_event == ActionEvent.LOST:
                    super_done = True
                    if action_event == ActionEvent.WON:
                        print("Won!!")
                    else:
                        print('lost')

                game.game_state = next_game_state

                current_game_state = deepcopy(next_game_state)
                pygame.display.flip()

                clock.tick(2)


dq = DeepQ()
dq.train()
dq.run_model()
