import numpy as np

from copy import deepcopy
import pygame

from pacman.initializer import initialize_gamestate_from_file
from qlearning.ExperienceReplay import Memory, Experience
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

    def __init__(self, level):
        initial_game_state = initialize_gamestate_from_file(level)

        self.input_size = self.convert_state_to_input(initial_game_state).size
        self.num_actions = len(Action.get_all_actions())
        self.model = self.init_model()

    def init_model(self):
        self.model = Sequential()
        self.model.add(Dense(512, input_shape=(self.input_size,), activation='relu'))
        self.model.add(Dense(512, activation='relu'))
        self.model.add(Dense(self.num_actions))
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

        return r.reshape(1, r.size)

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

    def train(self, level, num_training_episodes, batch_size, gamma=0.9):

        initial_game_state = initialize_gamestate_from_file(level)
        tot_loss = {}
        memory = Memory(max_size=5000)

        for i in range(1, num_training_episodes):

            loss = 0.
            num_episode_steps = 0

            done = False
            current_game_state = deepcopy(initial_game_state)

            while not done:
                if num_episode_steps > 1000:
                    break

                action = self.pick_action(current_game_state)
                next_game_state, action_event = get_next_game_state_from_action(current_game_state, action.name)

                if action_event == ActionEvent.WON or action_event == ActionEvent.LOST:
                    done = True
                    if action_event == ActionEvent.WON:
                        print("Won!!")
                    else:
                        print('lost')

                reward = calculate_reward_for_move(action_event)

                experience = Experience(
                    current_state=self.convert_state_to_input(current_game_state),
                    action=action,
                    reward=reward,
                    next_state=self.convert_state_to_input(next_game_state),
                    done=done
                )
                memory.add(experience)

                batch = memory.get_mini_batch(batch_size=batch_size)

                # Dimensions of our observed states, ie, the input to our model.
                input_dim = batch[0].current_state.shape[1]
                x_train = np.zeros((min(memory.get_size(), batch_size), input_dim))
                y_train = np.zeros((x_train.shape[0], len(Action.get_all_actions())))  # Target Q-value

                sample: Experience
                for j, sample in enumerate(batch):
                    y_target = self.model.predict(sample.current_state)[0]

                    x_train[j:j + 1] = sample.current_state
                    if sample.done:
                        y_target[sample.action.value] = sample.reward
                    else:
                        y_target[sample.action.value] = sample.reward + gamma * np.max(self.model.predict(sample.next_state))
                    y_train[j] = y_target

                batch_loss = self.model.train_on_batch(x_train, np.asarray(y_train))

                loss += batch_loss

                num_episode_steps += 1

                current_game_state = deepcopy(next_game_state)

            print(i)
            print(loss / num_episode_steps)

            tot_loss[i] = (loss / num_episode_steps)

        print(tot_loss)

        # plot_training_history(tot_loss)

        self.model.save('./nn_model.h5')


def run_with_game_loop(level='level-0', model_path='./nn_model.h5'):
    dq_model = DeepQ()
    dq_model.model = load_model(model_path)

    def ai_func(current_game_state):
        return dq_model.pick_optimal_action(current_game_state)

    game = Game(level, init_screen=True, ai_function=ai_func)
    game.run()


# dq = DeepQ()
# dq.train(level='level-0', num_training_episodes=150, batch_size=75)

# run_with_game_loop()
