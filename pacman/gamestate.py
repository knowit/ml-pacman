from functools import reduce
import collections

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
        self.last_game_event = None
        self.num_dots_left = 0
        self.num_fruits_left = 0

    def __str__(self):
        board = self.get_text_representation_of_gamestate()
        collapsed = [''.join(row) for row in board]

        return '\n'.join(collapsed)

    def __hash__(self):
        obj_hash = hash(tuple([9 * x for x in self.pacman.position]))

        for w in self.walls:
            obj_hash += hash(w.position)

        for f in self.fruits:
            if not f.is_eaten:
                obj_hash += hash(f.position)

        for g in self.ghosts:
            obj_hash += hash(g.position)

        for d in self.dots:
            if not d.is_eaten:
                obj_hash += hash(d.position)

        return obj_hash

    def __eq__(self, other):
        if isinstance(other, GameState):
            if self.pacman.position != other.pacman.position:
                return False
            if collections.Counter([w.position for w in self.walls]) != collections.Counter(
                    [w.position for w in other.walls]):
                return False
            if collections.Counter([w.position for w in self.fruits]) != collections.Counter(
                    [w.position for w in other.fruits]):
                return False
            if collections.Counter([w.position for w in self.ghosts]) != collections.Counter(
                    [w.position for w in other.ghosts]):
                return False
            if collections.Counter([w.position for w in self.dots]) != collections.Counter(
                    [w.position for w in other.dots]):
                return False
            if self.num_dots_left != other.num_dots_left:
                return False
            if self.num_fruits_left != other.num_fruits_left:
                return False
        return True

    def get_active_fruits(self):
        return [fruit for fruit in self.fruits if not fruit.is_eaten]

    def get_active_dots(self):
        return [dot for dot in self.dots if not dot.is_eaten]

    def get_number_of_dots_eaten(self):
        # TODO: Test
        return reduce((lambda acc, dot: acc + 1 if dot.is_eaten else acc), self.dots, 0)

    def get_number_of_fruits_eaten(self):
        # TODO: Test
        return reduce((lambda acc, fruit: acc + 1 if fruit.is_eaten else acc), self.fruits, 0)

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

    def has_lost(self):
        return self.pacman.lives <= 0

    def calculate_score(self):
        score = 0
        for fruit in self.fruits:
            score += fruit.score if fruit.is_eaten else 0
        for dot in self.dots:
            score += dot.score if dot.is_eaten else 0
        return score - self.pacman.number_of_ticks  # TODO: Score trenger ikke gå ned?

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





