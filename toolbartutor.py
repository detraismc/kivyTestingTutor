from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder

Window.size = (300, 500)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Test Application'
            anchor_title: "left"
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["axe-battle", lambda x: app.navigation_draw()]]
            elevation: 2
        MDLabel:
            text: 'Hello, World!'
            halign: 'center'
        MDBottomAppBar:
            MDTopAppBar:
                title: "Bottom Bar"
                icon: "plus"
                type: "bottom"
                mode: "end"
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
"""

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.material_style = "M2"
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("navigation draw")

MyApp().run()