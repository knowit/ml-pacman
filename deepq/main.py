import numpy as np

from copy import deepcopy

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

        count = 0
        while not done:
            pygame.event.get()
            # action = pick_action(current_game_state)
            action = Action.RIGHT
            if count > 8:
                action = Action.LEFT
            next_game_state, action_event = get_next_game_state_from_action(current_game_state, action.value)
            reward = calculate_reward_for_move(action_event)

            print(count, action.value, action_event)
            game.game_state = next_game_state
            # print(game.game_state)
            game.animate()

            experience = Experience(
                current_game_state=current_game_state,
                action=action,
                reward=calculate_reward_for_move(action),
                next_game_state=next_game_state
            )
            memory.add(experience)

            nparray = np.asarray(next_game_state.get_text_representation_of_gamestate())
            print(nparray.shape)


            current_game_state = deepcopy(next_game_state)






            count += 1
            # if count == 10:
            #     print(count)
            #     break

deepQ = DeepQMain()
deepQ.train()