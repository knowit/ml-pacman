from objects.existence import Existence


class Wall(Existence):
    def __init__(self, position, gamestate):
        super().__init__(position, 'wall.png', gamestate)
