from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam


class NeuralNet:
    def __init__(self, name, state_size, action_size):
        self._name = name

        self._model = Sequential()
        self._model.add(Dense(20, input_dim=state_size, activation='relu'))
        self._model.add(Dense(20, activation='relu'))
        self._model.add(Dense(action_size, activation='linear'))
        self._model.compile(loss='mse', optimizer=Adam(lr=0.001))

    def train(self, state, target):
        self._model.fit(state, target, epochs=1, verbose=0)

    def predict(self, state):
        return self._model.predict(state)

    def get_weights(self):
        return self._model.get_weights()

    def set_weights(self, weights):
        return self._model.set_weights(weights)

    def save(self):
        output_dir = 'saved_models/'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        self._model.save_weights(output_dir + self._name + '.hdf5')

    def load(self):
        return self._model.load_weights(output_dir + self._name + '.hdf5')
