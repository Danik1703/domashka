from game_data import GameData

class GameLogic:
    def __init__(self, lower_limit, upper_limit):
        self.game_data = GameData(lower_limit, upper_limit)

    def check_guess(self, user_guess):
        self.game_data.attempts += 1

        if user_guess < self.game_data.num_to_guess:
            return "Загадане число більше."
        elif user_guess > self.game_data.num_to_guess:
            return "Загадане число менше."
        else:
            return f"Вірно! Ви вгадали число. Знадобилося спроб: {self.game_data.attempts}"