import pygame

import graphics.draw_board as b
from pacman import gamelogic
from pacman.gamelogic import MoveEvent, determine_move_event_by_comparing_game_states
from pacman.gamestate import GameState
from pacman.initializer import initialize_gamestate_from_file
from pacman.keymapper import map_key_to_move

MOVE_GHOST_EVENT = pygame.USEREVENT+1
PACMAN_TICK = pygame.USEREVENT+2

# TODO: Embed AI in game or game in AI?


class Game:
    def __init__(self, level, ai_function=None):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.game_state = initialize_gamestate_from_file(level)
        self.done = False
        self.ai_function = ai_function
        pygame.time.set_timer(MOVE_GHOST_EVENT, 400)
        pygame.time.set_timer(PACMAN_TICK, 400)

    def run(self):
        while not self.done:
            self.execute_game_loop()

    def move_ghosts(self):
        for ghost in self.game_state.ghosts:
            ghost.tick()

    def animate(self):
        # Wipe screen from previous cycle
        self.screen.fill((89, 54, 104))

        # Draw current gamestate to the screen
        b.draw_board(self.game_state, self.screen)
        b.draw_lives(self.game_state, self.screen)
        b.draw_score(self.game_state, self.screen)

        pygame.display.flip()

    def handle_input_action(self, event):
        move = map_key_to_move(event)
        self.game_state.pacman.set_move(move)

    def execute_game_loop(self):
        move_event = None

        # Handle keyboard events for manual playing
        for event in pygame.event.get():
            current_game_state = self.game_state

            if event.type == pygame.QUIT:
                self.done = True
            if event.type == MOVE_GHOST_EVENT:
                self.move_ghosts()
            if event.type == PACMAN_TICK:
                is_move_valid = self.game_state.pacman.tick()
                if not is_move_valid:
                    move_event = MoveEvent.WALL

            if self.ai_function:
                move = self.ai_function(self.game_state)
                self.game_state.pacman.set_move(move)

            if move_event is None:
                self.handle_input_action(event)
                move_event = determine_move_event_by_comparing_game_states(current_game_state, self.game_state)
                gamelogic.check_ghost_collisions(self.game_state)

        self.animate()

        # Limit FPS to 60 (still unnecessarily high)
        self.clock.tick(60)

        return self.game_state, move_event
