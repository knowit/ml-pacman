from objects.pacman import Pacman
from objects.fruit import Fruit
from objects.wall import Wall
from objects.ghost import Ghost
from gamestate import GameState


def translate_input_symbol_to_object(position, gamestate, symbol):
    if symbol == "P":
        gamestate.pacman = Pacman(position, gamestate)
    if symbol == "F":
        gamestate.fruits.append(Fruit(position, gamestate))
    if symbol == "W":
        gamestate.walls.append(Wall(position, gamestate))
    if symbol == "G":
        gamestate.ghosts.append(Ghost(position, gamestate))


def initialize_game_from_file(file):
    gamestate = read_level(file)
    return gamestate


def read_level(level):
    y_pointer = 0
    x_pointer = 0
    gamestate = GameState()
    with open("./boards/" + level + '.txt', "r") as f:
        f = f.read().splitlines()
        gamestate.dimensions = [len(f), len(f[0])]
        for y in f:
            for item in y:
                current_position = x_pointer, y_pointer
                translate_input_symbol_to_object(current_position, gamestate, item)
                x_pointer += 1
            y_pointer += 1
            x_pointer = 0
    return gamestate
