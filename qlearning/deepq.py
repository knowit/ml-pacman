import numpy as np

from copy import deepcopy
import time
import pygame
from qlearning.exp_rep import ExperienceReplay


from pacman.actions import Action
from pacman.game import Game
from pacman.gamelogic import ActionEvent, get_next_game_state_from_action
from keras import Sequential
from keras.layers import Dense
from keras.optimizers import sgd


def init_model():
    num_actions = 4
    hidden_size = 512
    input_size = 100

    model = Sequential()
    model.add(Dense(hidden_size, input_shape=(input_size,), activation='relu'))
    model.add(Dense(hidden_size, activation='relu'))
    model.add(Dense(num_actions))
    model.compile(sgd(lr=.01), "mse")

    return model


def convert_state_to_input(state):
    return np.random.randint(2, size=(1, 100))
    # return np.ones(shape=(1, 100))


def pick_optimal_action(state, model):
    q = model.predict(convert_state_to_input(state))

    print(q)

    return Action.get_all_actions()[np.argmax(q[0])]


def pick_action(game_state, model):
    exploration_prob = 0.35
    if exploration_prob > np.random.rand():
        # Explore
        return np.random.choice(Action.get_all_actions())
    else:
        # Exploit
        return pick_optimal_action(game_state, model)


def calculate_reward_for_move(action_event):
    if action_event == ActionEvent.DOT:
        return 70
    elif action_event == ActionEvent.CAPTURED_BY_GHOST:
        return -50
    elif action_event == ActionEvent.NONE:
        return -5
    elif action_event == ActionEvent.WALL:
        return -5
    elif action_event == ActionEvent.WON:
        return 1000
    elif action_event == ActionEvent.LOST:
        return -1000
    else:
        return 0


def convert_action_to_int(action):
    if action == Action.DOWN:
        return 2
    if action == Action.LEFT:
        return 3
    if action == Action.UP:
        return 0
    if action == Action.RIGHT:
        return 1
    return 5


def run():
    game = Game('level-0', 400)
    now = time.time()

    batch_size = 1

    exp_replay = ExperienceReplay()
    model = init_model()

    for i in range(1, 10):

        done = False
        current_game_state = deepcopy(game.initial_game_state)

        while not done:

            action = pick_action(current_game_state, model)
            next_game_state, action_event = get_next_game_state_from_action(current_game_state, action.value)

            if action_event == ActionEvent.WON or action_event == ActionEvent.LOST:
                done = True

            reward = calculate_reward_for_move(action_event)

            exp_replay.remember(states=[convert_state_to_input(current_game_state), convert_action_to_int(action), reward, convert_state_to_input(next_game_state)], game_over=done)

            # Load batch of experiences
            inputs, targets = exp_replay.get_batch(model=model, batch_size=batch_size)

            # train model on experiences
            model.train_on_batch(inputs, targets)

            current_game_state = deepcopy(next_game_state)

            # count += 1
            if i % 5 == 0:
                print(i)
                print(time.time() - now)
                # now = time.time()

    current_game_state = deepcopy(game.initial_game_state)

    super_done = False

    clock = pygame.time.Clock()

    while not super_done:
        # pygame.event.get()

        action = pick_optimal_action(current_game_state, model)

        print(action)

        game.animate()

        next_game_state, action_event = get_next_game_state_from_action(current_game_state, action.value)

        print(action_event)

        game.game_state = next_game_state

        # game.animate()

        current_game_state = deepcopy(next_game_state)

        clock.tick(1)

run()
