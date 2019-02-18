import pygame
import graphics.draw_board as b
from initializer import initialize_game_from_file
from keymapper import map_key_to_move
import gamelogic

MOVE_GHOST_EVENT = pygame.USEREVENT+1
PACMAN_TICK = pygame.USEREVENT+2


class Game:
    def __init__(self, level):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.gamestate = initialize_game_from_file(level)
        self.done = False
        pygame.time.set_timer(MOVE_GHOST_EVENT, 400)
        pygame.time.set_timer(PACMAN_TICK, 400)

    def run(self):
        while not self.done:
            self.execute_game_loop()

    def move_ghosts(self):
        for ghost in self.gamestate.ghosts:
            ghost.tick()

    def execute_game_loop(self):
        # Handle keyboard events for manual playing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == MOVE_GHOST_EVENT:
                self.move_ghosts()
            if event.type == PACMAN_TICK:
                self.gamestate.pacman.tick()
            move = map_key_to_move(event)
            self.gamestate.pacman.set_move(move)
            gamelogic.check_collisions(self.gamestate)

        # Wipe screen from previous cycle
        self.screen.fill((255, 255, 255))

        # Draw current gamestate to the screen
        b.draw_board(self.gamestate, self.screen)
        b.draw_lives(self.gamestate, self.screen)
        b.draw_score(self.gamestate, self.screen)

        # Limit FPS to 60 (still unnecessarily high)
        self.clock.tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    game = Game('level-2')
    game.run()





