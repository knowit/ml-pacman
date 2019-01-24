from objects.existence import Existence


class Dot(Existence):
    def __init__(self, position, gamestate):
        self.is_eaten = False
        super().__init__(position, gamestate, icon='dot.png', symbol='-', score=10)

    def eat(self):
        self.is_eaten = True
