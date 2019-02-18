from objects.existence import Existence
import utils.moves as moves
from objects.fruit import Fruit
import time


class Pacman(Existence):
    def __init__(self, position, gamestate):
        super().__init__(position, gamestate, icon='manu.png', symbol='P')
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

    def handle_action(self):
        active_items = []
        active_items.extend(self.gamestate.get_active_fruits())
        active_items.extend(self.gamestate.get_active_dots())

        for item in active_items:
            if item.position == self.position:
                item.eat()
                if type(item) == Fruit:
                    for ghost in self.gamestate.ghosts:
                        ghost.frighten()

    def tick(self):
        direction = moves.DIRECTION_FROM_MOVE[self.current_move]
        super().move(direction)
        self.handle_action()
        self.time_at_last_tick = time.time()
        self.number_of_ticks += 1




