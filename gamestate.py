
class GameState:
    def __init__(self):
        self.pacman = None
        self.walls = []
        self.fruits = []
        self.ghosts = []

    def get_active_fruits(self):
        return [fruit for fruit in self.fruits if not fruit.is_eaten]

    def retrieve_all_active_items(self):
        # The order matters. It determines the drawing order
        items = []
        items.extend(self.walls)
        items.extend(self.get_active_fruits())
        items.extend(self.ghosts)
        items.append(self.pacman)
        return items
