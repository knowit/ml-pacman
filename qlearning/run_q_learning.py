import numpy as np

from copy import deepcopy
import time
import pygame
import random

from pacman.actions import Action
from pacman.game import Game
from pacman.gamelogic import ActionEvent, get_next_game_state_from_action


def pick_action(game_state, q_table):
    # TODO: Epsilon greedy
    exploration_prob = 0.3
    if exploration_prob > np.random.rand():
        # Explore
        return np.random.choice(Action.get_all_actions())
    else:
        # Exploit
        return pick_optimal_action(game_state, q_table)


def calculate_reward_for_move(action_event):
    if action_event == ActionEvent.DOT:
        return 10
    elif action_event == ActionEvent.CAPTURED_BY_GHOST:
        return -100
    elif action_event == ActionEvent.OUT_OF_LIVES:
        return -400
    elif action_event == ActionEvent.WALL:
        return -5
    else:
        return 0

def computeValueFromQValues(state, q_table):
    """
      Returns max_action Q(state,action)
      where the max is over legal actions.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return a value of 0.0.
    """

    if state not in q_table:
        q_table[state] = {key: 0.0 for key in Action.get_all_actions()}

    return max(q_table[state].values())


def pick_optimal_action(state, q_table, printing=False):
    """
      Compute the best action to take in a state.  Note that if there
      are no legal actions, which is the case at the terminal state,
      you should return None.
    """

    if state not in q_table:
        q_table[state] = {key: 0.0 for key in Action.get_all_actions()}

    maxValue = max(q_table[state].values())
    actions = [key for key in q_table[state] if q_table[state][key] == maxValue]

    if printing:
        print(state)
        print(q_table[state])

    # max(self.q_table[state], key=self.q_table[state].get)

    return random.choice(actions)


def run():
    game = Game('level-0', 1)
    current_game_state = deepcopy(game.game_state)

    done = False

    discount = 0.8
    alpha = 0.8

    count = 0
    now = time.time()

    q_table = {}

    for i in range(0, 10):

        action = pick_action(current_game_state, q_table)

        _, action_event = get_next_game_state_from_action(current_game_state, action.value)

        print(action)

        print(action_event)

        print(_)

        reward = calculate_reward_for_move(action_event)

        print(reward)

        # game.execute_game_loop(action.value, False)

        if current_game_state not in q_table:
            q_table[current_game_state] = {key: 0.0 for key in Action.get_all_actions()} # only get legal actions

        q_table[current_game_state][action] = q_table[current_game_state][action] + alpha * (reward + (discount * computeValueFromQValues(_, q_table)) - q_table[current_game_state][action])

        current_game_state = _

        count += 1
        if count % 1000 == 0:
            print(count)
            print(time.time() - now)
            # now = time.time()

    print(q_table)

    # new_game = Game('level-0', 1000)
    # new_game.run(q_table=q_table, pick_optimal_action=pick_optimal_action)


run()
