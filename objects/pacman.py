import time

import utils.moves as moves
from objects.animated import Animated
from objects.existence import Existence
from objects.fruit import Fruit
from objects.dot import Dot
from pacman.gamestate import GameState


class Pacman(Existence):
    def __init__(self, position, gamestate):
        super().__init__(position, gamestate, icon='priest_1.png', symbol='P')
        super().set_animation(Animated('priest', 4, 0.25))
        self.lives = 3
        self.max_lives = 3
        self.respawn_position = position
        self.current_move = "NONE"
        self.time_at_last_tick = time.time()
        self.number_of_ticks = 0

    def lose_life(self, lives_lost):
        self.lives -= lives_lost

    def respawn(self):
        self.position = self.respawn_position
        self.current_move = "NONE"

    def set_move(self, move):
        if move == "NONE":
            return
        self.current_move = move

    def handle_action(self, game_state):
        """

        Args:
            game_state (GameState):

        Returns:

        """
        active_items = []
        active_items.extend(self.gamestate.get_active_fruits())
        active_items.extend(self.gamestate.get_active_dots())

        for item in active_items:
            if item.position == self.position:
                item.eat()
                if type(item) == Dot:
                    game_state.num_dots_left -= 1
                if type(item) == Fruit:
                    game_state.num_fruits_left -= 1
                    for ghost in self.gamestate.ghosts:
                        ghost.frighten()

    def tick(self, game_state):
        direction = moves.DIRECTION_FROM_MOVE[self.current_move]
        is_move_valid = super().move(direction)  # If not valid -> wall crash
        self.handle_action(game_state)
        self.time_at_last_tick = time.time()
        self.number_of_ticks += 1

        return is_move_valid
