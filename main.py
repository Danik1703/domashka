from kivy.app import App
from guess_number_app import GuessNumberGame

class GuessNumberApp(App):
    def build(self):
        return GuessNumberGame()

if __name__ == '__main__':
    GuessNumberApp().run()