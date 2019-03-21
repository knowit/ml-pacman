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
    input_size = 60

    model = Sequential()
    model.add(Dense(hidden_size, input_shape=(input_size,), activation='relu'))
    model.add(Dense(hidden_size, activation='relu'))
    model.add(Dense(num_actions))
    model.compile(sgd(lr=.01), "mse")

    return model


def convert_state_to_input(state):

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

    return r.reshape(1, 60)
    # return np.ones(shape=(1, 100))


def pick_optimal_action(state, model, a):

    q = model.predict(convert_state_to_input(state))

    if a:
        print(q)

    return Action.get_all_actions()[np.argmax(q[0])]


def pick_action(game_state, model):
    exploration_prob = 0.15
    if exploration_prob > np.random.rand():
        # Explore
        return np.random.choice(Action.get_all_actions())
    else:
        # Exploit
        return pick_optimal_action(game_state, model, False)


def calculate_reward_for_move(action_event):
    if action_event == ActionEvent.DOT:
        return 20
    elif action_event == ActionEvent.CAPTURED_BY_GHOST:
        return -5
    elif action_event == ActionEvent.NONE:
        return -1
    elif action_event == ActionEvent.WALL:
        return -1
    elif action_event == ActionEvent.WON:
        return 100
    elif action_event == ActionEvent.LOST:
        return -50
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

    batch_size = 50

    exp_replay = ExperienceReplay()
    model = init_model()

    for i in range(1, 200):

        done = False
        current_game_state = deepcopy(game.initial_game_state)

        print(i)
        print(time.time() - now)

        while not done:

            action = pick_action(current_game_state, model)
            next_game_state, action_event = get_next_game_state_from_action(current_game_state, action.value)

            if action_event == ActionEvent.WON or action_event == ActionEvent.LOST:
                done = True

            reward = calculate_reward_for_move(action_event)

            # print(current_game_state)
            # print(action)
            # print(reward)
            # print(next_game_state)
            #
            # print('-----states------')

            states = [convert_state_to_input(current_game_state), convert_action_to_int(action), reward, convert_state_to_input(next_game_state)]

            # print(states)

            exp_replay.remember(states=states, game_over=done)

            # Load batch of experiences
            inputs, targets = exp_replay.get_batch(model=model, batch_size=batch_size)

            # print('----inputs------')
            #
            # print(inputs)
            #
            # print('----targets-----')
            #
            # print(targets)

            # train model on experiences
            model.train_on_batch(inputs, targets)

            current_game_state = deepcopy(next_game_state)

            # count += 1
            # if i % 5 == 0:
            #     print(i)
            #     print(time.time() - now)
                # now = time.time()

            # time.sleep(10)

    current_game_state = deepcopy(game.initial_game_state)

    super_done = False

    clock = pygame.time.Clock()

    while not super_done:
        # pygame.event.get()

        action = pick_optimal_action(current_game_state, model, True)

        print(action)

        game.animate()

        next_game_state, action_event = get_next_game_state_from_action(current_game_state, action.value)

        print(action_event)

        game.game_state = next_game_state

        # game.animate()

        current_game_state = deepcopy(next_game_state)

        clock.tick(1)

run()
