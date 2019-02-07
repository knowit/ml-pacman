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


# Returns how the gamestate would look if current move is executed
def get_next_gamestate(gamestate, move):
    pass


def is_wall(gamestate, position):
    for wall in gamestate.walls:
        if wall.position == position:
            return True
    return False
