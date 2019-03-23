import os
import sys

# Append path to use modules outside pycharm environment, e.g. terminal
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

from pacman.game import Game


if __name__ == '__main__':
    game = Game('level-2', True)
    game.run()





