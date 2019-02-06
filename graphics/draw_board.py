import utils.load_asset as load
import pygame
import time
from objects.pacman import Pacman
from utils.moves import DIRECTION_FROM_MOVE
import gamelogic

image_size = 40
font_name = "comicsansms"


def translate_position_to_pixels(position):
    return position[0] * image_size, position[1] * image_size


def draw_item(item, screen):
    if type(item) == Pacman:
        draw_pacman(item, screen)
    else:
        screen.blit(load.get_image('./images/' + item.get_icon()),
                    translate_position_to_pixels(item.get_position()))


def draw_pacman(pacman, screen):
    time_since_tick = time.time() - pacman.time_at_last_tick
    direction_offset = [0, 0]
    if pacman.current_move is not "None":
        offset = (image_size * (time_since_tick/0.2))
        direction = DIRECTION_FROM_MOVE[pacman.current_move]

        #check if position we are moving to is a wall
        next_position = gamelogic.add_move_to_position(pacman.position, direction)
        if not gamelogic.is_wall(pacman.gamestate, next_position):
            direction_offset = direction[0] * offset, direction[1] * offset

    pixel_position = translate_position_to_pixels(pacman.get_position())
    pixel_position_offset = pixel_position[0] + direction_offset[0], pixel_position[1] + direction_offset[1]
    screen.blit(load.get_image('./images/' + pacman.get_icon()),
                pixel_position_offset)


def draw_score(gamestate, screen):
    score = gamestate.calculate_score()
    font = pygame.font.SysFont(font_name, 72)
    text = font.render("Score: " + str(score), True, (0, 128, 0))
    w, h = pygame.display.get_surface().get_size()
    screen.blit(text, (0, h - text.get_height()))


def draw_lives(gamestate, screen):
    lives = gamestate.pacman.lives
    font = pygame.font.SysFont(font_name, 72)
    text = font.render("Lives: " + str(lives), True, (0, 128, 0))
    w, h = pygame.display.get_surface().get_size()
    screen.blit(text, (w - text.get_width(), h - text.get_height()))


def draw_board(gamestate, screen):
    for item in gamestate.retrieve_all_active_items():
        draw_item(item, screen)
