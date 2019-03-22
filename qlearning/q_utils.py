from pacman.actions import Action
from pacman.gamelogic import ActionEvent
import matplotlib.pyplot as plt


# TODO: Implement rewards for each action. I wonder what the best values are...
def calculate_reward_for_move(action_event):
    if action_event == ActionEvent.DOT:
        return 0
    elif action_event == ActionEvent.CAPTURED_BY_GHOST:
        return 0
    elif action_event == ActionEvent.NONE:
        return 0
    elif action_event == ActionEvent.WALL:
        return 0
    elif action_event == ActionEvent.WON:
        return 0
    elif action_event == ActionEvent.LOST:
        return 0
    return 0


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

