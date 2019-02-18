from objects.existence import Existence
from objects.animated import Animated


class Dot(Existence):
    def __init__(self, position, gamestate):
        self.is_eaten = False
        super().__init__(position, gamestate, icon='coin_1.png', symbol='.', score=10)
        super().set_animation(Animated('coin', 4, 0.25))

    def eat(self):
        self.is_eaten = True
