import utils.load_asset as load

image_size = 40


def translate_position_to_pixels(position):
    return position[0] * image_size, position[1] * image_size


def draw_item(item, screen):
    screen.blit(load.get_image('./images/' + item.get_icon()),
                translate_position_to_pixels(item.get_position()))


def draw_board(gamestate, screen):
    for item in gamestate.retrieve_all_active_items():
        draw_item(item, screen)




