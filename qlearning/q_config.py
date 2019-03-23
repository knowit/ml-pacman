
class QConfig(object):
    def __init__(self):
        self.discount = 0.8
        self.alpha = 0.2
        self.episodes = 1


class DeepQConfig(object):
    def __init__(self):
        self.num_actions = 4
        self.input_size = 60 # TODO: Change this. Based on how big your map is, and how you represent your game state you will know the size of this.
        self.hidden_size = 512
        self.batch_size = 75
        self.episodes = 15