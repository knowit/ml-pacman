import pygame
import os

# NB: use lower case file names to ensure it will work on all OS

_image_library = {}


def get_image(path, force_reload=False):
    global _image_library
    image = _image_library.get(path)
    if image == None or force_reload:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image
