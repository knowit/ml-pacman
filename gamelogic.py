import copy


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


def check_collisions(gamestate):
    for ghost in gamestate.ghosts:
        if ghost.position == gamestate.pacman.position:
            if ghost.frightened:
                ghost.respawn()
            else:
                reset(gamestate)


def get_next_gamestate_from_move(gamestate, move):
    gamestate_copy = copy.deepcopy(gamestate)
    gamestate_copy.pacman.set_move(move)
    gamestate_copy.pacman.tick()
    for ghost in gamestate_copy.ghosts:
        ghost.tick()
    return {
        'GAMESTATE': gamestate_copy,
        'SCORE': gamestate_copy.calculate_score(),
        'LIVES': gamestate_copy.pacman.lives,
        'HAS_WON': gamestate_copy.has_won()
    }


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
