from pacman.gamestate import GameState
from pacman.actions import Action

class Experience:

    def __init__(self, current_state, action, reward, next_state):
        """

        Args:
            current_state (GameState):
            action (Action):
            reward (int):
            next_state (GameState):
        """
        self.current_state = current_state
        self.action = action
        self.reward = reward
        self.next_state = next_state

    # def __str__(self):
    #     return self.current_state
