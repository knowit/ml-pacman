import utils.load_asset as load
import pygame
import time
from objects.pacman import Pacman
from objects.ghost import Ghost

image_size = 40
font_name = "comicsansms"


def translate_position_to_pixels(position):
    return position[0] * image_size, position[1] * image_size


def draw_item(item, screen):
    if type(item) == Pacman:
        animate_item(item, screen, 0.1)
    elif type(item) == Ghost:
        animate_item(item, screen, 0.1)
    else:
        screen.blit(load.get_image('./images/' + item.get_icon()),
                    translate_position_to_pixels(item.get_position()))


def animate_item(item, screen, animation_delta):
    time_since_tick = time.time() - item.time_at_last_tick
    direction_offset = [0, 0]
    if item.previous_position != item.position:
        offset = image_size - (image_size * (min(time_since_tick / animation_delta, 1)))
        direction = item.position[0] - item.previous_position[0], item.position[1] - item.previous_position[1]
        direction_offset = direction[0] * offset, direction[1] * offset

    pixel_position = translate_position_to_pixels(item.get_position())
    pixel_position_offset = pixel_position[0] - direction_offset[0], pixel_position[1] - direction_offset[1]
    screen.blit(load.get_image('./images/' + item.get_icon()), pixel_position_offset)


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
