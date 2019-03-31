from pacman.game import Game
from qlearning.q_learning import QLearn
from utils.file_utils import load_pickle


def run_jupyter(level='level-0', model_path='./q_table.pkl'):

    q_model = QLearn()
    q_model.q_table = load_pickle(model_path)

    print('twfd')
    def ai_func(current_game_state):
        return q_model.pick_optimal_action(current_game_state, printing=True)

    game = Game(level, init_screen=True, ai_function=ai_func)
    game.run()

run_jupyter()