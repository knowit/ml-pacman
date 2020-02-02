import numpy as np
import random
import tensorflow as tf
config = tf.ConfigProto()
# config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 0.02
from keras.backend.tensorflow_backend import set_session
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import sgd

set_session(tf.Session(config=config))

def getX():
    return np.zeros(shape=(1, 100))

def getY():
    return np.array([random.randint(0, 1)])

model = Sequential()
model.add(Dense(20, input_shape=(100,), activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(1))
model.compile(sgd(lr=.01), "mse")

for i in range(9999):
    model.train_on_batch(getX(), getY())
