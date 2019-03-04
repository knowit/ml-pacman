from enum import Enum


class Reward(Enum):
    # TODO: Define reward values for all Pac-man encounters
    DOT = 10
    CAPTURED_BY_GHOST = -100
    ACTION_PENALTY = -1
    FRUIT = 50
    WALL = -20
