from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from helpers import *

class MyApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        #username = MDTextField(text = 'Enter Username',
        #                       pos_hint = {'center_x': 0.5, 'center_y': 0.5},
        #                       size_hint_x=None,width=300)
        button = MDRectangleFlatButton(
            text="Login",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            on_release=self.show_data
        )
        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        print("Username: " + self.username.text)
        print("Password: " + self.password.text)

MyApp().run()