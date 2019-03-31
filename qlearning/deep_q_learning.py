import numpy as np

from copy import deepcopy
import pygame
from qlearning.exp_rep import ExperienceReplay
from qlearning.q_config import DeepQConfig
from qlearning.q_utils import convert_action_to_int


from pacman.actions import Action
from pacman.game import Game
from pacman.gamelogic import ActionEvent, get_next_game_state_from_action
from keras import Sequential
from keras.layers import Dense
from keras.optimizers import sgd
from keras.models import load_model

def calculate_reward_for_move(action_event):
    if action_event == ActionEvent.DOT:
        return 1
    elif action_event == ActionEvent.CAPTURED_BY_GHOST:
        return -5
    elif action_event == ActionEvent.NONE:
        return -0.1
    elif action_event == ActionEvent.WALL:
        return -0.1
    elif action_event == ActionEvent.WON:
        return 10
    elif action_event == ActionEvent.LOST:
        return -10
    return 0

class DeepQ(object):

    def __init__(self):
        self.config = DeepQConfig()
        self.model = self.init_model()
        self.exp_replay = ExperienceReplay()

    def init_model(self):

        self.model = Sequential()
        self.model.add(Dense(self.config.hidden_size, input_shape=(self.config.input_size,), activation='relu'))
        self.model.add(Dense(self.config.hidden_size, activation='relu'))
        self.model.add(Dense(self.config.num_actions))
        self.model.compile(sgd(lr=.01), "mse")

        return self.model

    def convert_state_to_input(self, state):
        string_rep = state.__str__()
        r = np.array([])

        for char in string_rep:
            # if char == '%':
            #     r = np.concatenate([r, [0, 0, 0, 0, 1]])
            if char == ' ':
                r = np.concatenate([r, [0, 0, 0, 1, 0]])
            if char == 'P':
                r = np.concatenate([r, [0, 0, 1, 0, 0]])
            if char == 'G':
                r = np.concatenate([r, [0, 1, 0, 0, 0]])
            if char == '.':
                r = np.concatenate([r, [1, 0, 0, 0, 0]])

        return r.reshape(1, self.config.input_size)

    def pick_optimal_action(self, state):
        q = self.model.predict(self.convert_state_to_input(state))
        return Action.get_all_actions()[np.argmax(q[0])]

    def pick_action(self, game_state):
        exploration_prob = 0.20
        if exploration_prob > np.random.rand():
            # Explore
            return np.random.choice(Action.get_all_actions())
        else:
            # Exploit
            return self.pick_optimal_action(game_state)

    def train(self):

        game = Game('level-0')
        tot_loss = {}

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

        self.model = load_model(model_path)
        game = Game('level-0')
        clock = pygame.time.Clock()
        game.init_screen()

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
