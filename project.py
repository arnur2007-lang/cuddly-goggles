import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle


class RoundedTextInput(Widget):
    def __init__(self, hint_text="", **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)
        self.height = 50

        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.background = RoundedRectangle(pos=self.pos, size=self.size, radius=[25])

        self.bind(pos=self.update_background, size=self.update_background)

        self.text_input = TextInput(
            multiline=False,
            hint_text=hint_text,
            background_color=(0, 0, 0, 0),
            foreground_color=(0, 0, 0, 1),
            padding=(10, 10),
        )
        self.text_input.pos = self.pos
        self.text_input.size = self.size
        self.add_widget(self.text_input)

    def update_background(self, *args):
        self.background.pos = self.pos
        self.background.size = self.size
        self.text_input.pos = self.pos
        self.text_input.size = self.size


class LoginPage(Screen):
    def next_page(self, instance):
        self.manager.current = "next_page"

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        Window.size = (400, 750)
        Window.clearcolor = (4 / 255, 255 / 255, 119 / 255)

        self.window.add_widget(
            Image(source='/Users/arnurmussabekov/PycharmProjects/PythonProject/99a233a2-726e-4a63-a14e-985802a5c730_removalai_preview.png'))

        self.greeting = Label(text="Welcome! Please log in:", font_size=54)
        self.window.add_widget(self.greeting)

        self.username_label = Label(text="Username:", font_size=54)
        self.window.add_widget(self.username_label)
        self.username_input = RoundedTextInput(hint_text="Enter your username")
        self.window.add_widget(self.username_input)

        self.password_label = Label(text="Password:", font_size=54)
        self.window.add_widget(self.password_label)
        self.password_input = RoundedTextInput(hint_text="Enter your password")
        self.window.add_widget(self.password_input)

        self.next_button = Button(text='GO TO NEXT PAGE', font_size=54)
        self.next_button.bind(on_press=self.next_page)
        self.window.add_widget(self.next_button)

        self.add_widget(self.window)


class NextPage(Screen):
    def build(self):
        layout = GridLayout(cols=1)
        label = Label(text="You are on the next page!", font_size=54)
        layout.add_widget(label)
        back_button = Button(text="Go Back", font_size=18)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = "login_page"


class Qaiyrum(App):
    def build(self):
        sm = ScreenManager()

        login_page = LoginPage(name="login_page")
        login_page.build()

        next_page = NextPage(name="next_page")
        next_page.build()

        sm.add_widget(login_page)
        sm.add_widget(next_page)

        return sm


if __name__ == "__main__":
    Qaiyrum().run()
