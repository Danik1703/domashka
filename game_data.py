import random

class GameData:
    def __init__(self, lower_limit, upper_limit):
        self.number_to_guess = random.randint(lower_limit, upper_limit)
        self.attempts = 0