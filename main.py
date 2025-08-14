from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.label import MDIcon, MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton

class MyApp(MDApp):
    def build(self):
        #label = MDLabel(text='Hello World', halign='center', theme_text_color='Custom',
        #                text_color=(200/255, 120/255, 50/255, 1),
        #                font_style='H2')
        #anchor = MDAnchorLayout(anchor_x='center', anchor_y='center')
        #anchor.add_widget(MDIcon(icon='axe-battle'))
        #return anchor
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text="Hello World",
                                pos_hint={"center_x": 0.5, "center_y": 0.5})
        icon_btn = MDFloatingActionButton(icon="axe-battle", pos_hint={"center_x": 0.5, "center_y": 0.5})
        screen.add_widget(icon_btn)
        return screen

MyApp().run()
