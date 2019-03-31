from enum import Enum


class Action(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    @staticmethod
    def get_all_actions():
        return [action for action in Action]