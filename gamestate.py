
class GameState:
    def __init__(self):
        self.pacman = None
        self.walls = []
        self.fruits = []
        self.ghosts = []
        self.dots = []
        self.dimensions = []
        # As walls are static, we do not need to look them up every time we need to know
        self.wall_positions = []

    def __str__(self):
        board = self.get_text_representation_of_gamestate()
        collapsed = [''.join(row) for row in board]

        return '\n'.join(collapsed)

    def get_active_fruits(self):
        return [fruit for fruit in self.fruits if not fruit.is_eaten]

    def get_active_dots(self):
        return [dot for dot in self.dots if not dot.is_eaten]

    def get_wall_positions(self):
        return self.wall_positions

    def get_corners(self):
        w, h = self.dimensions
        return [(0,0), (w, 0), (0, h), (h, w)]

    def has_won(self):
        if len(self.get_active_dots()) > 0:
            return False
        if len(self.get_active_fruits()) > 0:
            return False
        if self.pacman.lives > 0:
            return True
        return False

    def calculate_score(self):
        score = 0
        for fruit in self.fruits:
            score += fruit.score if fruit.is_eaten else 0
        for dot in self.dots:
            score += dot.score if dot.is_eaten else 0
        return score - self.pacman.number_of_ticks

    # The order matters. It determines the drawing order
    def retrieve_all_active_items(self):
        items = []
        items.extend(self.walls)
        items.extend(self.get_active_fruits())
        items.extend(self.get_active_dots())
        items.extend(self.ghosts)
        items.append(self.pacman)
        return items

    def insert_object_symbol_into_textual_gamestate(self, item, board):
        board[item.position[1]][item.position[0]] = item.symbol

    def get_text_representation_of_gamestate(self):
        board = [[' ' for i in range(self.dimensions[1])] for j in range(self.dimensions[0])]
        active_items = self.retrieve_all_active_items()
        for item in active_items:
            self.insert_object_symbol_into_textual_gamestate(item, board)
        return board





