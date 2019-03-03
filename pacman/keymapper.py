import pygame


def map_key_to_move(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            return "UP"
        if event.key == pygame.K_RIGHT:
            return "RIGHT"
        if event.key == pygame.K_DOWN:
            return "DOWN"
        if event.key == pygame.K_LEFT:
            return "LEFT"
    return "NONE"
