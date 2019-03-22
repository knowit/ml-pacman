import numpy as np

from copy import deepcopy
import time
import pygame
import random

from pacman.actions import Action
from pacman.game import Game
from pacman.gamelogic import ActionEvent, get_next_game_state_from_action
from qlearning.q_utils import calculate_reward_for_move, convert_action_to_int
from qlearning.q_config import QConfig


class QLearn(object):

    def __init__(self):
        self.q_table = {}
        self.config = QConfig()

    def pick_action(self, game_state):
        exploration_prob = 0.35
        if exploration_prob > np.random.rand():
            # Explore
            return np.random.choice(Action.get_all_actions())
        else:
            # Exploit
            return self.pick_optimal_action(game_state)

    def compute_value_from_q_values(self, state):
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

        return random.choice(actions)

    def run(self):
        game = Game('level-0')

        now = time.time()

        for i in range(1, 500):

            done = False
            current_game_state = deepcopy(game.initial_game_state)

            while not done:

                action = self.pick_action(current_game_state)

                _, action_event = get_next_game_state_from_action(current_game_state, action.value)

                if action_event == ActionEvent.WON or action_event == ActionEvent.LOST:
                    done = True
                    if action_event == ActionEvent.WON:
                        print("Won!!")

                reward = calculate_reward_for_move(action_event)

                if current_game_state not in self.q_table:
                    self.q_table[current_game_state] = {key: 0.0 for key in Action.get_all_actions()}

                self.q_table[current_game_state][action] = self.q_table[current_game_state][action] + self.config.alpha * (reward + (self.config.discount * self.compute_value_from_q_values(_)) - self.q_table[current_game_state][action])

                current_game_state = _

                # count += 1
                if i % 10 == 0:
                    print(i)
                    print(time.time() - now)
                    # now = time.time()

        game.init_screen()

        clock = pygame.time.Clock()

        for i in range(5):

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

                clock.tick(1)


q_learn = QLearn()
q_learn.run()
