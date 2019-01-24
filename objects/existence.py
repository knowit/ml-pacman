class Existence:
    def __init__(self, location, icon, gamestate, symbol):
        self.position = location
        self.icon = icon
        self.gamestate = gamestate
        self.symbol = symbol

    def get_position(self):
        return self.position

    def get_icon(self):
        return self.icon

    def get_symbol(self):
        return self.symbol
