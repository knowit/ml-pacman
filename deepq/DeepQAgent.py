import numpy as np
import random

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

from deepq.Memory import Memory
from deepq.NeuralNet import NeuralNet


class DeepQAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size

        self.memory_size = 2000

        self.gamma = 0.95
        self.epsilon = 1.0
        self.tau = 0.125

        self.q_model = NeuralNet('q-model', state_size, action_size)
        self.target_model = NeuralNet('target-model', state_size, action_size)
        self.memory = Memory(self.memory_size)

    def _decay_epsilon(self):
        self.epsilon = np.max([self.epsilon * 0.995, 0.01])

    def _act_after_e_greedy_policy(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        else:
            predicted_action_values = self.q_model.predict(state)
            return np.argmax(predicted_action_values[0])

    def _train_target_model(self):
        q_weights = self.q_model.get_weights()
        target_weights = self.target_model.get_weights()

        for i in range(len(target_weights)):
            q_part = self.tau * q_weights[i]
            target_part = (1 - self.tau) * target_weights[i]
            target_weights[i] = q_part + target_part

        self.target_model.set_weights(target_weights)

    def remember(self, state, action, reward, next_state, done):
        self.memory.add((state, action, reward, next_state, done))

    def act(self, state):
        return self._act_after_e_greedy_policy(state)

    def experience_replay(self, batch_size):
        minibatch = self.memory.get_minibatch(batch_size)

        for state, action, reward, next_state, done in minibatch:

            q_updated = reward
            target = self.target_model.predict(state)

            if not done:
                target_next = self.target_model.predict(next_state)
                q_updated += self.gamma * np.amax(target_next[0])

            target[0][action] = q_updated
            self.q_model.train(state, target)

        self._train_target_model()
        self._decay_epsilon()
