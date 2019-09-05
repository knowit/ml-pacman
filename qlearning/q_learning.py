import numpy as np

from copy import deepcopy
import random

from pacman.actions import Action
from pacman.game import Game
from pacman.gamelogic import ActionEvent, get_next_game_state_from_action
from utils.file_utils import save_pickle, load_pickle


def calculate_reward_for_move(action_event):
    if action_event == ActionEvent.DOT:
        return 2
    elif action_event == ActionEvent.CAPTURED_BY_GHOST:
        return -5
    elif action_event == ActionEvent.NONE:
        return -0.1
    elif action_event == ActionEvent.WALL:
        return -0.1
    elif action_event == ActionEvent.WON:
        return 20
    elif action_event == ActionEvent.LOST:
        return -10
    return 0


class QLearn(object):

    def __init__(self):
        self.q_table = {}

    def pick_action(self, game_state):
        exploration_prob = 0.20
        if exploration_prob > np.random.rand():
            # Explore
            return np.random.choice(Action.get_all_actions())
        else:
            # Exploit
            return self.pick_optimal_action(game_state)

    def compute_max_q_value(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """

        if state not in self.q_table:
            self.q_table[state] = {key: 0.0 for key in Action.get_all_actions()}

        return max(self.q_table[state].values())

    def pick_optimal_action(self, state, printing=False):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """

        if state not in self.q_table:
            self.q_table[state] = {key: 0.0 for key in Action.get_all_actions()}

        max_value = max(self.q_table[state].values())
        actions = [key for key in self.q_table[state] if self.q_table[state][key] == max_value]

        if printing:
            print(state)
            print(self.q_table[state])
            print(state.__hash__())

        return random.choice(actions)

    def train(self, level='level-0', num_episodes=10):
        game = Game(level)
        discount = 0.8
        alpha = 0.2

        for i in range(num_episodes):
            current_game_state = deepcopy(game.initial_game_state)

            episode_done = False
            while not episode_done:
                if i % 50 == 0:
                    print("Iteration number", i)
                action = self.pick_action(current_game_state)
                new_game_state, action_event = get_next_game_state_from_action(current_game_state, action.name)

                if action_event == ActionEvent.WON or action_event == ActionEvent.LOST:
                    episode_done = True
                    if action_event == ActionEvent.WON:
                        print("Won!!")

                reward = calculate_reward_for_move(action_event)

                if current_game_state not in self.q_table:
                    self.q_table[current_game_state] = {key: 0.0 for key in Action.get_all_actions()}

                self.q_table[current_game_state][action] = self.q_table[current_game_state][action] + alpha * (reward + (discount * self.compute_max_q_value(new_game_state)) - self.q_table[current_game_state][action])

                current_game_state = new_game_state

        save_pickle('./q_table', self.q_table, True)


def run_with_game_loop(level='level-0', model_path='./q_table.pkl'):

    q_model = QLearn()
    q_model.q_table = load_pickle(model_path)

    def ai_func(current_game_state):
        return q_model.pick_optimal_action(current_game_state)

    game = Game(level, init_screen=True, ai_function=ai_func)
    game.run()


if __name__ == '__main__':
    # q_learn = QLearn()
    # q_learn.train(num_episodes=400)
    
    run_with_game_loop()
