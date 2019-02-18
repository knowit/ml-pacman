from objects.existence import Existence


class Fruit(Existence):
    def __init__(self, position, gamestate):
        self.is_eaten = False
        super().__init__(position, gamestate, icon='banana.png', symbol='o', score=50)

    def eat(self):
        self.is_eaten = True
