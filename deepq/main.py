import numpy as np

from copy import deepcopy
import time
import pygame

from deepq.Experience import Experience
from deepq.Memory import Memory
from deepq.rewards import Reward
from pacman.actions import Action
from pacman.game import Game
from deepq.ai_example import get_suggested_move
from pacman.gamelogic import ActionEvent, get_next_game_state_from_action


def pick_action(game_state):
    # TODO: Epsilon greedy
    exploration_prob = 1.0
    if exploration_prob > np.random.rand():
        # Explore
        return np.random.choice(Action.get_all_actions())
    else:
        # Exploit
        print("Exploit")
        # TODO: Run DeepQ with game_state (potentially stacked) as input


def calculate_reward_for_move(action_event):
    # TODO: Add all rewards
    reward = Reward.ACTION_PENALTY.value
    if action_event == ActionEvent.DOT:
        reward += Reward.DOT.value
    elif action_event == ActionEvent.CAPTURED_BY_GHOST:
        reward += Reward.CAPTURED_BY_GHOST.value
    return reward


class DeepQMain:

    def train(self):
        # Init game
        game = Game('level-2')
        current_game_state = deepcopy(game.game_state)

        # Init Memory
        memory = Memory(max_size=10)

        # TODO: Init DeepQNetwork
        done = False

        ## METHOD 1
        # while not done:
        #     action = pick_action(current_game_state)
        #     game_feedback = game.execute_game_loop()
        #
        #     if game_feedback is not None:
        #         next_game_state, move_event = game.execute_game_loop()
        #
        #         print(move_event)
        #         reward = calculate_reward_for_move(move_event)
        #         # print(reward)
        #
        #         experience = Experience(current_game_state, action, reward, next_game_state)
        #         print(experience.next_state)
        #         memory.add(experience)
        #
        #         current_game_state = deepcopy(next_game_state)

            # game.run()

        ## METHOD2
        count = 0
        now = time.time()
        while not done:
            pygame.event.get()
            action = pick_action(current_game_state)
            next_game_state, action_event = get_next_game_state_from_action(current_game_state, action.value)
            reward = calculate_reward_for_move(action_event)

            # print(action.value, action_event)
            game.game_state = next_game_state

            # print(game.game_state)
            # game.animate()

            current_game_state = deepcopy(next_game_state)
            count += 1
            if count % 1000 == 0:
                print(count)
                print(now - time.time())

deepQ = DeepQMain()
deepQ.train()