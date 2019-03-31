from pacman.gamestate import GameState
from pacman.actions import Action
from collections import deque

import numpy as np


class Memory:
    def __init__(self, max_size):
        self.memory = deque(maxlen=max_size)

    def add(self, experience):
        self.memory.append(experience)

    def get(self, index):
        return self.memory[index]

    def get_mini_batch(self, batch_size):
        memory_size = self.get_size()
        indices = np.random.choice(np.arange(memory_size), min(batch_size, memory_size), replace=False)
        return [self.memory[i] for i in indices]

    def get_size(self):
        return len(self.memory)


class Experience:

    def __init__(self, current_state, action, reward, next_state, done: bool):
        """
        Args:
            done (bool):
            current_state (GameState):
            action (Action):
            reward (int):
            next_state (GameState):
        """
        self.current_state = current_state
        self.action = action
        self.reward = reward
        self.next_state = next_state
        self.done = done
