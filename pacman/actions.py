from enum import Enum


class Action(Enum):
    UP = "UP"
    RIGHT = "RIGHT"
    DOWN = "DOWN"
    LEFT = "LEFT"

    @staticmethod
    def get_all_actions():
        return [action for action in Action]

