from collections import deque
import random


class Memory:
    def __init__(self, max_size):
        self._buffer = deque(maxlen=max_size)

    def __len__(self):
        return len(self._buffer)

    def add(self, memory):
        self._buffer.append(memory)

    def get_minibatch(self, batch_size):
        return random.sample(self._buffer, batch_size)
