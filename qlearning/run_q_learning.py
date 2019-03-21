import numpy as np

from copy import deepcopy
import time
import pygame
import random

from pacman.actions import Action
from pacman.game import Game
from pacman.gamelogic import ActionEvent, get_next_game_state_from_action


def pick_action(game_state, q_table, i):
    # TODO: Epsilon greedy
    exploration_prob = 0.35
    if exploration_prob > np.random.rand():
        # Explore
        return np.random.choice(Action.get_all_actions())
    else:
        # Exploit
        return pick_optimal_action(game_state, q_table)


def calculate_reward_for_move(action_event):
    if action_event == ActionEvent.DOT:
        return 5
    elif action_event == ActionEvent.CAPTURED_BY_GHOST:
        return -5
    elif action_event == ActionEvent.NONE:
        return -1
    elif action_event == ActionEvent.WALL:
        return -1
    elif action_event == ActionEvent.WON:
        return 100
    elif action_event == ActionEvent.LOST:
        return -100
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
        # print('not in q_table')
        q_table[state] = {key: 0.0 for key in Action.get_all_actions()}

    maxValue = max(q_table[state].values())
    actions = [key for key in q_table[state] if q_table[state][key] == maxValue]

    if printing:
        print(state)
        print(q_table[state])

    # max(self.q_table[state], key=self.q_table[state].get)

    return random.choice(actions)


def run():
    game = Game('level-0', 400)


    discount = 0.8
    alpha = 0.2

    now = time.time()

    q_table = {}

    # TODO: Intro RL
    # TODO: Intro Q-learn
    # TODO: Intro Deep-Q-learn

    # TODO: ------------Q-learn------------
    # TODO: What number of episodes?
    # TODO: Rewards?
    # TODO: Exploration vs Exploitation ratio
    # TODO: Discount factor?
    # TODO: Learning rate (alpha)?
    # TODO: q_table
    # TODO: q_learning update rule
    # TODO: Ghost strats
    # TODO: ------------Q-learn------------

    # TODO: ------------Deep-Q-learn------------
    # TODO: Represent state
    # TODO: NN-architecture
    # TODO: Experience Replay
    # TODO: ------------Deep-Q-learn------------

    for i in range(1, 500):

        done = False
        current_game_state = deepcopy(game.initial_game_state)

        while not done:

            # time.sleep(8)

            action = pick_action(current_game_state, q_table, i)

            _, action_event = get_next_game_state_from_action(current_game_state, action.value)

            # print(current_game_state)
            #
            # print(action)
            #
            # print(action_event)
            #
            # print(_)

            if action_event == ActionEvent.WON or action_event == ActionEvent.LOST:
                done = True
                if action_event == ActionEvent.WON:
                    print("Won!!")

            reward = calculate_reward_for_move(action_event)

            # print(reward)

            # game.execute_game_loop(action.value, False)

            if current_game_state not in q_table:
                q_table[current_game_state] = {key: 0.0 for key in Action.get_all_actions()} # only get legal actions

            q_table[current_game_state][action] = q_table[current_game_state][action] + alpha * (reward + (discount * computeValueFromQValues(_, q_table)) - q_table[current_game_state][action])

            # print(q_table[current_game_state])

            current_game_state = _

            # count += 1
            if i % 10 == 0:
                print(i)
                print(time.time() - now)
                # now = time.time()

    # print(q_table)
    #
    # print(q_table.keys())

    # new_game = Game('level-0', 2000)
    # new_game.run(q_table=q_table, pick_optimal_action=pick_optimal_action)

    current_game_state = deepcopy(game.initial_game_state)

    super_done = False

    clock = pygame.time.Clock()

    while not super_done:
        # pygame.event.get()

        action = pick_optimal_action(current_game_state, q_table, True)
        print(action)

        game.animate()

        next_game_state, action_event = get_next_game_state_from_action(current_game_state, action.value)

        print(action_event)

        game.game_state = next_game_state

        # game.animate()

        current_game_state = deepcopy(next_game_state)

        clock.tick(1)

run()
