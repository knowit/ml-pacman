from objects.existence import Existence
import utils.moves as moves
import random
import time

# Every ghost has a mode
# Either Chase, Scatter, or Frightened. Default is Chase
# Chase: target position is based on pacmans position
# Scatter: target position is outside one of the four corners

# The different modes are set based on a timer that is reset every time pacman loses a life

# 1 Scatter for 7 seconds, then Chase for 20 seconds.
# 2 Scatter for 7 seconds, then Chase for 20 seconds.
# 3 Scatter for 5 seconds, then Chase for 20 seconds.
# 4 Scatter for 5 seconds, then switch to Chase mode permanently.

# 0 seconds -> scatter
# 7 seconds -> chase
# 27 seconds -> scatter
# 34 seconds -> chase
# 54 seconds -> scatter
# 59 seconds -> chase
# 79 seconds -> scatter
# 84 seconds -> chase

# ghosts can never go back to the tile they came from. Unless frightened!

# Ghosts only ever plan 1 step in the future

CHASE = 'CHASE'
SCATTER = 'SCATTER'
FRIGHTENED = 'FRIGHTENED'


class Ghost(Existence):
    def __init__(self, position, gamestate):
        super().__init__(position, gamestate, icon='babyface.png', symbol='G', score=100)
        self.respawn_position = position
        self.target_position = (3, 3)
        self.mode = CHASE
        self.previous_move = None
        self.time_at_respawn = time.time()
        self.frightened = False

    def ghost_event_routine(self):
        if time.time() - self.time_at_respawn > 84:
            return CHASE
        if time.time() - self.time_at_respawn > 79:
            return SCATTER
        if time.time() - self.time_at_respawn > 59:
            return CHASE
        if time.time() - self.time_at_respawn > 54:
            return SCATTER
        if time.time() - self.time_at_respawn > 34:
            return CHASE
        if time.time() - self.time_at_respawn > 27:
            return SCATTER
        if time.time() - self.time_at_respawn > 7:
            return CHASE
        return SCATTER

    def respawn(self):
        self.time_at_respawn = time.time()
        self.position = self.respawn_position

    def get_available_moves(self):
        all_possible_moves = moves.get_next_position_by_move(self.position)

        non_blocked_moves = {}
        for direction, new_position in all_possible_moves.items():
            # Remove directions that hit a wall
            if new_position in self.gamestate.get_wall_positions():
                continue
            # Remove previous direction
            if moves.OPPOSITE_MOVES[direction] == self.previous_move:
                continue
            non_blocked_moves[direction] = new_position

        return non_blocked_moves

    def get_direction(self):
        possible_moves = self.get_available_moves()
        distance_per_move = {}
        for direction, new_position in possible_moves.items():
            distance_per_move[direction] = moves.calculate_euclidean_distance_to_target(self.target_position, new_position)

        min_distance = min(distance_per_move.values())
        best_moves = [move for move in distance_per_move if distance_per_move[move] == min_distance]
        # Return the best move based on prio list
        for move in best_moves:
            if move == "UP":
                return move
            if move == "LEFT":
                return move
            if move == "DOWN":
                return move
            if move == "RIGHT":
                return move

    def chase_pacman(self):
        direction = self.get_direction()
        self.execute_move(direction)

    def scatter(self):
        print(self.target_position)
        direction = self.get_direction()
        self.execute_move(direction)

    def run_away(self):
        pass

    def frighten(self):
        self.frightened = True

    def execute_move(self, next_move):
        self.previous_move = next_move
        direction = moves.DIRECTION_FROM_MOVE[next_move]
        super().move(direction)

    def set_mode(self, mode):
        if mode == self.mode:
            return
        if mode == SCATTER:
            corners = self.gamestate.get_corners()
            random.shuffle(corners)
            self.target_position = corners[0]
            self.mode = mode
        if mode == CHASE:
            self.target_position = self.gamestate.pacman.position

    def do_move(self):
        self.set_mode(self.ghost_event_routine())
        if self.mode == CHASE:
            self.chase_pacman()
        elif self.mode == SCATTER:
            self.scatter()
        elif self.mode == FRIGHTENED:
            self.run_away()
