
import random
import gym
import numpy as np
import os

from deepq.DeepQAgent import DeepQAgent

env = gym.make('MountainCar-v0')

state_size = env.observation_space.shape[0]
action_size = env.action_space.n

agent = DeepQAgent(state_size, action_size)

batch_size = 64
episodes = 1000

done = False
for episode in range(episodes):

    state = env.reset()
    state = np.reshape(state, [1, state_size])

    time = 0
    while True:
        time += 1

        action = agent.act(state)
        next_state, reward, done, _ = env.step(action)

        next_state = np.reshape(next_state, [1, state_size])
        agent.remember(state, action, reward, next_state, done)
        state = next_state

        if done:
            print(
                f"episode: {episode}/{episodes}, time: {time}" +
                f" reward: {reward}, e: {agent.epsilon}"
            )
            break

        if len(agent.memory) > batch_size:
            agent.experience_replay(batch_size)
