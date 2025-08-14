from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder

#Window.size = (450, 750)

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    MDTopAppBar:
                        title: "My App"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("toggle")]]
                        elevation: 2
                        
                    Widget:
                        
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: "vertical"
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'gambar.jpg'
                MDLabel:
                    text: "My App"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "detraismc@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'axe-battle'
                        OneLineIconListItem:
                            text: 'Upload'
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'android'
                                
                    
                    
"""

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.material_style = "M2"
        screen = Builder.load_string(navigation_helper)
        return screen


MyApp().run()