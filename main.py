from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from game_logic import GameLogic

class GuessNumberGame(BoxLayout):
    def __init__(self, **kwargs):
        super(GuessNumberGame, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label_lower = Label(text="Введіть нижню межу діапазону:")
        self.add_widget(self.label_lower)
        self.input_lower = TextInput(multiline=False)
        self.add_widget(self.input_lower)

        self.label_upper = Label(text="Введіть верхню межу діапазону:")
        self.add_widget(self.label_upper)
        self.input_upper = TextInput(multiline=False)
        self.add_widget(self.input_upper)

        self.submit_button = Button(text="Почати гру", on_press=self.start_game)
        self.add_widget(self.submit_button)

        self.game_logic = None

    def start_game(self, instance):
        try:
            lower_limit = int(self.input_lower.text)
            upper_limit = int(self.input_upper.text)

            if lower_limit >= upper_limit:
                self.show_result("Неправильний діапазон. Нижня межа повинна бути менше за верхню.")
                return

            self.game_logic = GameLogic(lower_limit, upper_limit)

            # Очищаємо елементи від полів для вводу та кнопки
            self.remove_widget(self.label_lower)
            self.remove_widget(self.input_lower)
            self.remove_widget(self.label_upper)
            self.remove_widget(self.input_upper)
            self.remove_widget(self.submit_button)

            # Додаємо нові елементи для вводу чисел та кнопку "Відправити"
            self.label_prompt = Label(text="Вгадайте число від {} до {}:".format(lower_limit, upper_limit))
            self.add_widget(self.label_prompt)

            self.input_guess = TextInput(multiline=False)
            self.add_widget(self.input_guess)

            self.submit_button = Button(text="Відправити", on_press=self.check_guess)
            self.add_widget(self.submit_button)

        except ValueError:
            self.show_result("Будь ласка, введіть коректні цілі числа.")

    def check_guess(self, instance):
        try:
            user_guess = int(self.input_guess.text)
            result = self.game_logic.check_guess(user_guess)
            self.show_result(result)
        except ValueError:
            self.show_result("Будь ласка, введіть коректне ціле число.")

    def show_result(self, result):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=result))
        close_button = Button(text="Закрити")
        content.add_widget(close_button)

        popup = Popup(title='Результат', content=content, size_hint=(None, None), size=(300, 200))
        close_button.bind(on_press=popup.dismiss)

        popup.open()


class GuessNumberApp(App):
    def build(self):
        return GuessNumberGame()


if __name__ == '__main__':
    GuessNumberApp().run()