from game import Game
from deepq.ai_example import get_suggested_move


if __name__ == '__main__':
    game = Game('level-2', get_suggested_move)
    game.run()





