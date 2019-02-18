import pygame
import graphics.draw_board as b
from initializer import initialize_gamestate_from_file
from keymapper import map_key_to_move
import gamelogic

MOVE_GHOST_EVENT = pygame.USEREVENT+1
PACMAN_TICK = pygame.USEREVENT+2


class Game:
    def __init__(self, level, ai_function=None):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.gamestate = initialize_gamestate_from_file(level)
        self.done = False
        self.ai_function = ai_function
        pygame.time.set_timer(MOVE_GHOST_EVENT, 400)
        pygame.time.set_timer(PACMAN_TICK, 400)

    def run(self):
        while not self.done:
            self.execute_game_loop()

    def move_ghosts(self):
        for ghost in self.gamestate.ghosts:
            ghost.tick()

    def animate(self):
        # Wipe screen from previous cycle
        self.screen.fill((255, 255, 255))

        # Draw current gamestate to the screen
        b.draw_board(self.gamestate, self.screen)
        b.draw_lives(self.gamestate, self.screen)
        b.draw_score(self.gamestate, self.screen)

        pygame.display.flip()

    def handle_input_action(self, event):
        move = map_key_to_move(event)
        self.gamestate.pacman.set_move(move)

    def execute_game_loop(self):
        # Handle keyboard events for manual playing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == MOVE_GHOST_EVENT:
                self.move_ghosts()
            if event.type == PACMAN_TICK:
                self.gamestate.pacman.tick()

            if self.ai_function:
                move = self.ai_function(self.gamestate)
                self.gamestate.pacman.set_move(move)

            self.handle_input_action(event)

            gamelogic.check_collisions(self.gamestate)

        self.animate()

        # Limit FPS to 60 (still unnecessarily high)
        self.clock.tick(60)
