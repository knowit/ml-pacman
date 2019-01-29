from objects.existence import Existence


class Ghost(Existence):
    def __init__(self, position, gamestate):
        super().__init__(position, gamestate, icon='babyface.png', symbol='G', score=100)
        self.respawn_position = position

    def respawn(self):
        self.position = self.respawn_position

    def get_direction(self):
        pacman_position = self.gamestate.pacman.position
        direction = pacman_position[0] - self.position[0], pacman_position[1] - self.position[1]
        if direction == [0, 0]:
            return [0, 0]
        if abs(direction[0]) > abs(direction[1]):
            a = 1 if direction[0] > 0 else -1
            return [a, 0]
        if abs(direction[1]) >= abs(direction[0]):
            a = 1 if direction[1] > 0 else -1
            return [0, a]

    def chase_pacman(self):
        direction = self.get_direction()
        self.position = self.position[0] + direction[0], self.position[1] + direction[1]
