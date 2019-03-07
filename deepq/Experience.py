from pacman.gamestate import GameState
from pacman.actions import Action

class Experience:

    def __init__(self, current_game_state, action, reward, next_game_state):
        """

        Args:
            current_game_state (GameState):
            action (Action):
            reward (int):
            next_game_state (GameState):
        """
        self.current_game_state = current_game_state
        self.action = action
        self.reward = reward
        self.next_game_state = next_game_state

    # def __str__(self):
    #     return self.current_state
