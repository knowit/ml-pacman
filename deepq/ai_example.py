import random
from pacman import gamelogic


# The game is supplied one function that it will call for every time the game updates.
# Must return one of the following moves "UP", "LEFT", "DOWN", "RIGHT"
def get_suggested_move(gamestate):
    moves = ["UP", "LEFT", "DOWN", "RIGHT"]

    # Get all the possible enumerations (for each move
    gamestate_by_move = gamelogic.get_next_gamestate_by_move(gamestate)

    # For each next state you can calculate its utility and board representation

    for move, gamestate in gamestate_by_move.items():
        # Use this to get the textual representation fo the board
        board = gamestate.get_text_representation_of_gamestate()

        # Use this to get the score of current gamestate
        score = gamestate.calculate_score()

        # Get how many lives pacman has left to create a utility function
        lives = gamestate.pacman.lives

        # Get whether the game is won yet
        has_won = gamestate.has_won()

    random.shuffle(moves)
    return moves[0]
