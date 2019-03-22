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
        # TODO: Initialize q table and QConfig
        pass

    def pick_action(self, game_state):

        # TODO: Set an exploration probability.
        # TODO: If exploration: Return a random choice from Action.get_all_actions()
        # TODO: If not, call the pick_optimal_action with game_state as param and return it.

        pass

    def compute_value_from_q_values(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """

        # TODO: Check if state is in q_table; If not we need to put a value of 0.0 for each
        # TODO: action in Action.get_all_actions() for the given state.
        # TODO: return the highest q_value (NOT BEST ACTION, but the value of the best action) for the given state

        pass

    def pick_optimal_action(self, state, printing=False):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """

        # TODO: Check if state is in q_table; If not we need to put a value of 0.0 for each
        # TODO: action in Action.get_all_actions() for the given state.
        # TODO: Find the action that gives the highest q score
        # TODO: HOWEVER, if multiple actions have the same q score, you should probably choose
        # TODO: a random action among those actions.

        pass

    def run(self):
        game = Game('level-0')
        now = time.time()

        # TODO: Fill in number of episodes (the number of games your AI should train on.
        # TODO: Should not be lower than a few hundred...) in q_config.py.
        # This loop is the training loop where we fill in our q table
        # When this loop ends, the AI will play games with its learned q table
        for i in range(1, self.config.episodes):

            # Done becomes true when a game is over
            done = False

            # Set current game state to initial game state
            current_game_state = deepcopy(game.initial_game_state)

            while not done:

                # Choose action that AI will perform. During training it should either explore or exploit.
                action = self.pick_action(current_game_state)

                # Get next game state and an action event that tells us what happened when we perform the action
                # chosen above in current_game_state
                next_game_state, action_event = get_next_game_state_from_action(current_game_state, action.value)

                # We check if the game ended, and just prints if it won
                if action_event == ActionEvent.WON or action_event == ActionEvent.LOST:
                    done = True
                    if action_event == ActionEvent.WON:
                        print("Won!!")

                # Get the rewards that we implemented for each action event.
                reward = calculate_reward_for_move(action_event)

                # Need to check if the q table has seen the state before. If not we fill in that all actions in that
                # state has a score of 0.0, since we saw the state for the first time. You might have seen this before.
                if current_game_state not in self.q_table:
                    self.q_table[current_game_state] = {key: 0.0 for key in Action.get_all_actions()}

                # TODO: Implement the update rule for the q table here.

                # Stt the current state
                current_game_state = next_game_state

                # Print progression so we know something is happening
                if i % 30 == 0:
                    print(i)
                    print(time.time() - now)

        # Okay, so the training is done, and we want to see our pacman in action! The loop is basically the same
        # as the previous loop, but instead of choosing between exploration and exploitation we always choose
        # exploitation and just choose the best action directly. Also animate game and stuff.
        game.init_screen()
        clock = pygame.time.Clock()

        # TODO: Choose amount of games you want to watch your pacman AI play
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
