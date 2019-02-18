from objects.existence import Existence
from objects.animated import Animated
import utils.moves as moves
import random
import time

# Ghost logic mostly follows this: http://gameinternals.com/post/2072558330/understanding-pac-man-ghost-behavior

CHASE = 'CHASE'
SCATTER = 'SCATTER'
FRIGHTENED_DURATION = 5


class Ghost(Existence):
    def __init__(self, position, gamestate):
        super().__init__(position, gamestate, icon='skull_1.png', symbol='G', score=100)
        super().set_animation(Animated('skull', 4, 0.25))

        self.respawn_position = position
        self.target_position = (3, 3)
        self.mode = CHASE
        self.previous_move = None
        self.time_at_respawn = time.time()
        self.time_at_last_tick = time.time()
        self.time_at_frightened_start = None
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

        # This means that we are stuck in a corner
        if len(non_blocked_moves.values()) == 0:
            opposite_direction = moves.OPPOSITE_MOVES[self.previous_move]
            non_blocked_moves[opposite_direction] = all_possible_moves[opposite_direction]

        return non_blocked_moves

    def get_direction(self):
        possible_moves = self.get_available_moves()
        distance_per_move = {}
        for direction, new_position in possible_moves.items():
            distance_per_move[direction] = moves.calculate_euclidean_distance_to_target(self.target_position, new_position)

        min_distance = min(distance_per_move.values())
        best_moves = [move for move in distance_per_move if distance_per_move[move] == min_distance]
        return self.get_prioritized_moves(best_moves)

    def get_prioritized_moves(self, possible_moves):
        for move in possible_moves:
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
        direction = self.get_direction()
        self.execute_move(direction)

    def run_away(self):
        possible_moves = [move for move in self.get_available_moves().keys()]
        random.shuffle(possible_moves)
        move = possible_moves[0]
        self.execute_move(move)
        self.end_run_away_if_time_is_out()

    def end_run_away_if_time_is_out(self):
        if time.time() - self.time_at_frightened_start > FRIGHTENED_DURATION:
            self.frightened = False

    def frighten(self):
        self.time_at_frightened_start = time.time()
        self.frightened = True
        self.previous_move = moves.OPPOSITE_MOVES[self.previous_move]

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

    def tick(self):
        self.time_at_last_tick = time.time()
        self.set_mode(self.ghost_event_routine())
        if self.frightened:
            return self.run_away()
        if self.mode == CHASE:
            self.chase_pacman()
        elif self.mode == SCATTER:
            self.scatter()
