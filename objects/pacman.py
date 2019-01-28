from objects.existence import Existence


class Pacman(Existence):
    def __init__(self, position, gamestate):
        super().__init__(position, gamestate, icon='manu.png', symbol='P')
        self.lives = 3

    def move(self, vector):
        self.position = self.position[0] + vector[0], self.position[1] + vector[1]

    def lose_life(self, lives_lost):
    	self.lives -= lives_lost

