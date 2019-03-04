import copy
from enum import Enum
from pacman.gamestate import GameState


class MoveEvent(Enum):
    DOT = 1
    CAPTURED_BY_GHOST = 2
    FRUIT = 3
    OUT_OF_LIVES = 4
    GHOST_FRIGHTENED = 5
    CAPTURED_FRIGHTENED_GHOST = 6
    WALL = 7
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
                ghost.respawn()
                return MoveEvent.CAPTURED_FRIGHTENED_GHOST
            else:
                reset(gamestate)
                return MoveEvent.CAPTURED_BY_GHOST

    return None


def determine_move_event_by_comparing_game_states(
        current_game_state,
        next_game_state
):
    """
        Determine if Pac-Man has eaten food or captured ghost
    Args:
        current_game_state (GameState):
        next_game_state (GameState):

    Returns:

    """
    ghost_collision_event = check_ghost_collisions(next_game_state)
    if ghost_collision_event is not None:
        return ghost_collision_event
    elif has_eaten_dot(current_game_state, next_game_state):
        return MoveEvent.DOT
    elif has_eaten_fruit(current_game_state, next_game_state):
        return MoveEvent.FRUIT


def has_eaten_dot(current_game_state, next_game_state):
    """
        Determine if Pac-Man has eaten dot
    Args:
        current_game_state (GameState):
        next_game_state (GameState):

    Returns:
        Boolean
    """
    dots_diff = next_game_state.get_number_of_dots_eaten() - current_game_state.get_number_of_dots_eaten()
    if dots_diff == 1:
        return True
    elif dots_diff != 1 and dots_diff != 0:
        raise Exception("Error: dots_diff should be 0 or 1")
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
    fruits_diff = next_game_state.get_number_of_fruits_eaten() - current_game_state.get_number_of_fruits_eaten()
    if fruits_diff == 1:
        return True
    elif fruits_diff != 1 and fruits_diff != 0:
        raise Exception("Error: dots_diff should be 0 or 1")
    else:
        return False


def get_next_gamestate_from_move(gamestate, move):
    gamestate_copy = copy.deepcopy(gamestate)
    gamestate_copy.pacman.set_move(move)
    gamestate_copy.pacman.tick()
    for ghost in gamestate_copy.ghosts:
        ghost.tick()
    return gamestate_copy


def get_next_gamestate_DEBUG(gamestate):
    print("----------")
    print(gamestate)
    print('|')
    print('|')
    print('|')
    print('\\/')
    for move in ["UP", "LEFT", "DOWN", "RIGHT"]:
        print(get_next_gamestate_from_move(gamestate, move))


# Returns how the gamestate would look if current move is executed
def get_next_gamestate_by_move(gamestate):
    return {move: get_next_gamestate_from_move(gamestate, move) for move in ["UP", "LEFT", "DOWN", "RIGHT"]}


def is_wall(gamestate, position):
    for wall in gamestate.walls:
        if wall.position == position:
            return True
    return False
