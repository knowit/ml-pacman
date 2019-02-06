import gamelogic

class Existence:
    def __init__(self, location, gamestate, icon, symbol, score=0):
        self.position = location
        self.icon = icon
        self.gamestate = gamestate
        self.symbol = symbol
        self.score = score

    def get_position(self):
        return self.position

    def get_icon(self):
        return self.icon

    def get_symbol(self):
        return self.symbol

    def move(self, direction):
        if self.is_move_valid(direction):
            self.position = self.position[0] + direction[0], self.position[1] + direction[1]

    def is_move_valid(self, direction):
        old_position = self.position
        attempted_new_position = gamelogic.add_move_to_position(old_position, direction)
        return not gamelogic.is_wall(self.gamestate, attempted_new_position)
