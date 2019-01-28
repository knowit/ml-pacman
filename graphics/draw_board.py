import utils.load_asset as load
import pygame

image_size = 40
font_name = "comicsansms"


def translate_position_to_pixels(position):
    return position[0] * image_size, position[1] * image_size


def draw_item(item, screen):
    screen.blit(load.get_image('./images/' + item.get_icon()),
                translate_position_to_pixels(item.get_position()))

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




