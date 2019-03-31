from pacman import gamelogic


class Existence:
    def __init__(self, location, gamestate, icon, symbol, score=0):
        self.position = location
        self.previous_position = location
        self.icon = icon
        self.gamestate = gamestate
        self.symbol = symbol
        self.score = score
        self.animation = None

    def set_animation(self, animation):
        self.animation = animation

    def get_position(self):
        return self.position

    def get_icon(self):
        if self.animation:
            return self.animation.get_icon()
        return self.icon

    def get_symbol(self):
        return self.symbol

    def move(self, direction):
        self.previous_position = self.position
        if self.is_move_valid(direction):
            self.position = self.position[0] + direction[0], self.position[1] + direction[1]
            return True
        else:
            return False

    def is_move_valid(self, direction):
        old_position = self.position
        attempted_new_position = gamelogic.add_move_to_position(old_position, direction)
        return not gamelogic.is_wall(self.gamestate, attempted_new_position)



