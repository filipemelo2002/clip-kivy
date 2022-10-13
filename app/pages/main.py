import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.lang.builder import Builder
from WindowManager import WindowManager


class Application(App):
    def build(self):
        return WindowManager()

if __name__ == "__main__":
    Application().run()
