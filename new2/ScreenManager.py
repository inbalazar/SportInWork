from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window


# Config.set('graphics','resizable','0')
Window.size = (700, 600)
# Window.maximize()


class FirstScreen(Screen):
    def changer(self,*args):
        self.manager.current = 'second'

class SecondScreen(Screen):
    def changer(self, *args):
        self.manager.current = 'first'

class ThirdScreen(Screen):
    def changer(self, *args):
        self.manager.current = 'first'

class MyScreenManager(ScreenManager):
    pass

class ScreenManagerApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='Third'))
        return sm

if __name__ == "__main__":
    ScreenManagerApp().run()