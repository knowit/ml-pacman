

# Takes current action and determines what will happen to the game world
def handle_action(gamestate, move):
    old_position = gamestate.pacman.position
    attempted_new_position = add_move_to_position(old_position, move)
    # Check if the action is blocked by a wall
    if is_wall(gamestate, attempted_new_position):
        gamestate.pacman.move((0, 0))
        return

    # Check if the action eats a banana
    if is_banana(gamestate, attempted_new_position):
        eat_banana(gamestate, attempted_new_position)

    # Check if the action eats a dot
    if is_dot(gamestate, attempted_new_position):
        eat_dot(gamestate, attempted_new_position)

    is_eaten_by_ghost(gamestate, attempted_new_position)

    # Finally if we get this far pacman is allowed to move
    gamestate.pacman.move(move)


def check_move_validity(gamestate, move):
    old_position = gamestate.pacman.position
    attempted_new_position = add_move_to_position(old_position, move)
    return not is_wall(gamestate, attempted_new_position)


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


# TODO: This can be generalized
def is_banana(gamestate, position):
    for fruit in gamestate.get_active_fruits():
        if fruit.position == position:
            return True
    return False


def eat_banana(gamestate, position):
    for fruit in gamestate.fruits:
        if fruit.position == position:
            fruit.eat()


def is_dot(gamestate, position):
    for dot in gamestate.get_active_dots():
        if dot.position == position:
            return True
    return False


def eat_dot(gamestate, position):
    for dot in gamestate.dots:
        if dot.position == position:
            dot.eat()


# Returns how the gamestate would look if current move is executed
def get_next_gamestate(gamestate, move):
    pass


def is_wall(gamestate, position):
    for wall in gamestate.walls:
        if wall.position == position:
            return True
    return False
