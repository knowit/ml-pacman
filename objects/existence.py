class Existence:
    def __init__(self, location, gamestate, icon, symbol, score=0):
        self.position = location
        self.icon = icon
        self.gamestate = gamestate
        self.symbol = symbol
        self.score = score

    def get_position(self):
        return self.position

    def get_icon(self):
        return self.icon

    def get_symbol(self):
        return self.symbol
