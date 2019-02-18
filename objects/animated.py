import time


class Animated:
    def __init__(self, folder, animation_count, animation_speed):
        self.folder = folder
        self.current_animation = 1
        self.animation_count = animation_count
        self.animation_speed = animation_speed
        self.time_at_last_change = time.time()

    def increment_animation_count(self):
        self.current_animation = ((self.current_animation + 1) % self.animation_count) + 1
        self.time_at_last_change = time.time()

    def get_icon(self):
        icon_name = self.folder + "/" + self.folder + "_" + str(self.current_animation) + ".png"
        if time.time() - self.time_at_last_change > self.animation_speed:
            self.increment_animation_count()

        return icon_name
