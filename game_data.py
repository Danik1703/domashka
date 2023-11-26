import random

class GameData:
    def __init__(self, lower, upper):
        self.num_to_guess = random.randint(lower, upper)
        self.attempts = 0
