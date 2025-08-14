from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x': .5, 'center_y': .6}
        on_press: root.manager.current = 'upload'
        
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome to Profile'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press: root.manager.current = 'menu'
        
<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Lets upload some files!'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press: root.manager.current = 'menu'

"""


class ProfileScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(ProfileScreen(name='menu'))
sm.add_widget(MenuScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(screen_helper)

MyApp().run()