from keras.engine.saving import load_model

from pacman.game import Game
from qlearning.deep_q_learning import DeepQ
from qlearning.q_learning import QLearn
from utils.file_utils import load_pickle


def play_q_learning_model(level='level-0', model_path='./q_table.pkl'):
    q_model = QLearn()
    q_model.q_table = load_pickle(model_path)

    def ai_func(current_game_state):
        return q_model.pick_optimal_action(current_game_state, printing=True)

    game = Game(level, init_screen=True, ai_function=ai_func)
    game.run()


def play_deep_q_model(level='level-0', model_path='./nn_model.h5'):
    dq_model = DeepQ(level)
    dq_model.model = load_model(model_path)

    def ai_func(current_game_state):
        return dq_model.pick_optimal_action(current_game_state)

    game = Game(level, init_screen=True, ai_function=ai_func)
    game.run()


# play_q_learning_model()
# play_deep_q_model()