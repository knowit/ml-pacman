class Existence:
    def __init__(self, location, icon, gamestate):
        self.position = location
        self.icon = icon
        self.gamestate = gamestate

    def get_position(self):
        return self.position

    def get_icon(self):
        return self.icon
