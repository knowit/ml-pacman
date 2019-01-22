import pygame

DIRECTION_VECTORS = {
    "UP": [0, -1],
    "RIGHT": [1, 0],
    "DOWN": [0, 1],
    "LEFT": [-1, 0],
    "NONE": [0, 0],
}


def map_key_to_action(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            return DIRECTION_VECTORS["UP"]
        if event.key == pygame.K_RIGHT:
            return DIRECTION_VECTORS["RIGHT"]
        if event.key == pygame.K_DOWN:
            return DIRECTION_VECTORS["DOWN"]
        if event.key == pygame.K_LEFT:
            return DIRECTION_VECTORS["LEFT"]
    return DIRECTION_VECTORS["NONE"]
