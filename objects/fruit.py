from objects.existence import Existence
from objects.animated import Animated


class Fruit(Existence):
    def __init__(self, position, gamestate):
        self.is_eaten = False
        super().__init__(position, gamestate, icon='chest_1.png', symbol='o', score=50)
        super().set_animation(Animated('chest', 4, 0.25))

    def eat(self):
        self.is_eaten = True
