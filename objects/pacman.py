from objects.existence import Existence


class Pacman(Existence):
    def __init__(self, position, gamestate):
        super().__init__(position, 'manu.png', gamestate)

    def move(self, vector):
        self.position = self.position[0] + vector[0], self.position[1] + vector[1]

