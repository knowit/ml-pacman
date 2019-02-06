

OPPOSITE_MOVES = dict(UP="DOWN", LEFT="RIGHT", DOWN="UP", RIGHT="LEFT")
DIRECTION_FROM_MOVE = dict(UP=(0,1), LEFT=(-1,0), DOWN=(0,-1), RIGHT=(1,0))


def calculate_euclidean_distance_to_target(current, target):
    return (current[0] - target[0]) ** 2 + (current[1] - target[1]) ** 2


def get_next_position_by_move(current_position):
    return dict(UP=(current_position[0] + DIRECTION_FROM_MOVE["UP"][0], current_position[1] + DIRECTION_FROM_MOVE["UP"][1]),
                              LEFT=(current_position[0] + DIRECTION_FROM_MOVE["LEFT"][0], current_position[1] + DIRECTION_FROM_MOVE["LEFT"][1]),
                              DOWN=(current_position[0] + DIRECTION_FROM_MOVE["DOWN"][0], current_position[1] + DIRECTION_FROM_MOVE["DOWN"][1]),
                              RIGHT=(current_position[0] + DIRECTION_FROM_MOVE["RIGHT"][0], current_position[1] + DIRECTION_FROM_MOVE["RIGHT"][1]))
