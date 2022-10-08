import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.lang.builder import Builder
from CreateGroup import CreateGroup

class Application(App):
    def build(self):
        return CreateGroup.CreateGroup()

if __name__ == "__main__":
    Application().run()
