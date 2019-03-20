import copy
from enum import Enum
from pacman.gamestate import GameState
from copy import deepcopy


class ActionEvent(Enum):
    DOT = 1
    CAPTURED_BY_GHOST = 2
    FRUIT = 3
    OUT_OF_LIVES = 4
    GHOST_FRIGHTENED = 5
    CAPTURED_FRIGHTENED_GHOST = 6
    WALL = 7
    NONE = 8
    WON = 9
    LOST = 10

    # TODO: Frightened ghost?


def add_move_to_position(old_position, move):
    return old_position[0] + move[0], old_position[1] + move[1]


def is_eaten_by_ghost(gamestate, position):
    for ghost in gamestate.ghosts:
        if ghost.position == position:
            reset(gamestate)
            break


def reset(gamestate):
    for ghost in gamestate.ghosts:
        ghost.respawn()
    gamestate.pacman.lose_life(1)
    gamestate.pacman.respawn()


def check_ghost_collisions(gamestate):
    for ghost in gamestate.ghosts:
        if ghost.position == gamestate.pacman.position:
            if ghost.frightened:
                gamestate.last_game_event = ActionEvent.CAPTURED_FRIGHTENED_GHOST
                ghost.respawn()
            else:
                gamestate.last_game_event = ActionEvent.CAPTURED_BY_GHOST
                reset(gamestate)

    return None


def check_if_pacman_ate_food(
        current_game_state,
        next_game_state
):
    """
        Determine if Pac-Man has eaten food
    Args:
        current_game_state (GameState):
        next_game_state (GameState):

    Returns:

    """
    if has_eaten_dot(current_game_state, next_game_state):
        return ActionEvent.DOT
    elif has_eaten_fruit(current_game_state, next_game_state):
        return ActionEvent.FRUIT
    else:
        return None


def has_eaten_dot(current_game_state, next_game_state):
    """
        Determine if Pac-Man has eaten dot
    Args:
        current_game_state (GameState):
        next_game_state (GameState):

    Returns:
        Boolean
    """
    dots_diff = current_game_state.num_dots_left - next_game_state.num_dots_left
    if dots_diff == 1:
        return True
    elif dots_diff != 1 and dots_diff != 0:
        raise Exception("Error: dots_diff should be 0 or 1. Dots diff:", dots_diff)
    else:
        return False


def has_eaten_fruit(current_game_state, next_game_state):
    """
        Determine if Pac-Man has eaten fruit
    Args:
        current_game_state (GameState):
        next_game_state (GameState):

    Returns:
        Boolean
    """
    fruits_diff = current_game_state.num_fruits_left - next_game_state.num_fruits_left
    if fruits_diff == 1:
        return True
    elif fruits_diff != 1 and fruits_diff != 0:
        raise Exception("Error: dots_diff should be 0 or 1")
    else:
        return False


def get_next_game_state_from_action(current_game_state, action):
    """

    Args:
        current_game_state (GameState):
        action:
        game:

    Returns:

    """
    # next_game_state = copy.deepcopy(current_game_state)
    # next_game_state.pacman.set_move(action)
    #
    # is_move_valid = next_game_state.pacman.tick(next_game_state)
    # if not is_move_valid:
    #     next_game_state.last_game_event = ActionEvent.WALL
    # else:
    #     next_game_state.last_game_event = ActionEvent.NONE
    #
    # eaten_food = check_if_pacman_ate_food(current_game_state, next_game_state)
    # if eaten_food is not None:
    #     if next_game_state.num_dots_left == 0:
    #         next_game_state = deepcopy(game.initial_game_state)
    #         next_game_state.last_game_event = ActionEvent.WIN
    #     else:
    #         next_game_state.last_game_event = eaten_food
    #
    # for ghost in next_game_state.ghosts:
    #     ghost.tick()
    #
    # if check_ghost_collisions(next_game_state):
    #     next_game_state = deepcopy(game.initial_game_state)
    #     next_game_state.last_game_event = ActionEvent.CAPTURED_BY_GHOST
    #
    # return next_game_state, next_game_state.last_game_event

#     --------------------------------
    next_game_state = copy.deepcopy(current_game_state)
    next_game_state.pacman.set_move(action)

    is_move_valid = next_game_state.pacman.tick(next_game_state)
    if not is_move_valid:
        next_game_state.last_game_event = ActionEvent.WALL
    else:
        next_game_state.last_game_event = ActionEvent.NONE

    eaten_food = check_if_pacman_ate_food(current_game_state, next_game_state)
    if eaten_food is not None:
        next_game_state.last_game_event = eaten_food

    check_ghost_collisions(next_game_state)

    for ghost in next_game_state.ghosts:
        ghost.tick()

    check_ghost_collisions(next_game_state)

    if next_game_state.has_won():
        next_game_state.last_game_event = ActionEvent.WON

    if next_game_state.has_lost():
        next_game_state.last_game_event = ActionEvent.LOST

    return next_game_state, next_game_state.last_game_event


def get_next_gamestate_DEBUG(gamestate):
    print("----------")
    print(gamestate)
    print('|')
    print('|')
    print('|')
    print('\\/')
    for move in ["UP", "LEFT", "DOWN", "RIGHT"]:
        print(get_next_game_state_from_action(gamestate, move))


# Returns how the gamestate would look if current move is executed
def get_next_gamestate_by_move(gamestate):
    return {move: get_next_game_state_from_action(gamestate, move) for move in ["UP", "LEFT", "DOWN", "RIGHT"]}


def is_wall(gamestate, position):
    for wall in gamestate.walls:
        if wall.position == position:
            return True
    return False