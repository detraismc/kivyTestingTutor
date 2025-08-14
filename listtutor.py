from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList
from kivymd.uix.list import ThreeLineListItem, ThreeLineIconListItem, ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget
from kivy.uix.scrollview import ScrollView

class MyApp(MDApp):
    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        for i in range(20):
            #icon = IconLeftWidget(icon="android")
            image = ImageLeftWidget(source="discord.webp")
            items = ThreeLineAvatarListItem(text="Item " + str(i),
                                    secondary_text="Secondary Item " + str(i),
                                    tertiary_text="Tertiary Item " + str(i))
            items.add_widget(image)
            list_view.add_widget(items)

        screen.add_widget(scroll)
        return screen

MyApp().run()