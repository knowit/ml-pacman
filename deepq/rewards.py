from enum import Enum


class Reward(Enum):
    # TODO: Define reward values for Pac-man encounters
    PELLET = 10
    GHOST = -100
    ACTION_PENALTY = -1
    FRUIT = 50
