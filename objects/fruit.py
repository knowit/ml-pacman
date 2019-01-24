from objects.existence import Existence


class Fruit(Existence):
    def __init__(self, position, gamestate):
        self.is_eaten = False
        super().__init__(position, 'banana.png', gamestate, 'F')

    def eat(self):
        self.is_eaten = True
