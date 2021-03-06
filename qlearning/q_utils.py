from pacman.actions import Action
from pacman.gamelogic import ActionEvent
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def convert_action_to_int(action):
    if action == Action.UP:
        return 0
    elif action == Action.RIGHT:
        return 1
    elif action == Action.DOWN:
        return 2
    elif action == Action.LEFT:
        return 3
    return None


def plot_training_history(training_history):
    """

    :param training_history:

    :type training_history: dict
    :return:
    """
    # print(training_history)

    metrics = list(training_history.keys())
    metric_history = list(training_history.values())
    plt.figure(figsize=(40, 40))

    for i in range(len(metrics)):
        plt.plot(metric_history[i], label=metrics[i])

    plt.ylabel('Metric value')
    plt.xlabel('Epoch')
    plt.legend()
    plt.show()

# TODO: Intro RL
# TODO: Intro Q-learn
# TODO: Intro Deep-Q-learn

# TODO: ------------Q-learn------------
# TODO: What number of episodes?
# TODO: Rewards?
# TODO: Exploration vs Exploitation ratio
# TODO: Discount factor?
# TODO: Learning rate (alpha)?
# TODO: q_table
# TODO: q_learning update rule
# TODO: Ghost strats
# TODO: ------------Q-learn------------

# TODO: ------------Deep-Q-learn------------
# TODO: Represent state
# TODO: NN-architecture
# TODO: Experience Replay
# TODO: ------------Deep-Q-learn------------

