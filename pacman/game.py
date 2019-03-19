from copy import deepcopy

import pygame

import graphics.draw_board as b
from pacman import gamelogic
from pacman.gamelogic import ActionEvent, check_if_pacman_ate_food, check_ghost_collisions
from pacman.gamestate import GameState
from pacman.initializer import initialize_gamestate_from_file
from pacman.keymapper import map_key_to_move

import time

MOVE_GHOST_EVENT = pygame.USEREVENT+1
PACMAN_TICK = pygame.USEREVENT+2

# TODO: Embed AI in game or game in AI?


class Game:
    def __init__(self, level, a, ai_function=None):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.initial_game_state = initialize_gamestate_from_file(level)
        self.game_state = self.initial_game_state
        self.done = False
        self.ai_function = ai_function
        pygame.time.set_timer(MOVE_GHOST_EVENT, a)
        pygame.time.set_timer(PACMAN_TICK, a)

    def run(self, q_table=None, pick_optimal_action=None):
        while not self.done:
            if q_table:
                action = pick_optimal_action(self.game_state, q_table, True)
                print(action)
                self.execute_game_loop(ai_action=action.value)
            else:
                self.execute_game_loop()

    def move_ghosts(self):
        for ghost in self.game_state.ghosts:
            ghost.tick()

    def animate(self):
        """
            Draws game graphics
        """
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

    def execute_game_loop(self, ai_action=None, animate=True):
        # Handle keyboard events for manual playing
        for event in pygame.event.get():
            self.game_state.last_game_event = ActionEvent.NONE

            if event.type == pygame.QUIT:
                self.done = True
            if event.type == MOVE_GHOST_EVENT:
                self.move_ghosts()
            if event.type == PACMAN_TICK:
                is_move_valid = self.game_state.pacman.tick(self.game_state)
                if not is_move_valid:
                    self.game_state.last_game_event = ActionEvent.WALL

            if self.ai_function:
                move = self.ai_function(self.game_state)
                self.game_state.pacman.set_move(move)

            self.handle_input_action(event)

            # check_if_pacman_ate_food(previous_game_state, self.game_state)
            # return self.game_state, self.game_state.last_game_event
            if ai_action:
                self.game_state.pacman.set_move(ai_action)

        if animate:
            self.animate()

        if check_ghost_collisions(self.game_state):
            self.game_state = deepcopy(self.initial_game_state)
        # Limit FPS to 60 (still unnecessarily high)
        self.clock.tick(60)
