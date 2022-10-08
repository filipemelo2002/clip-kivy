import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.lang.builder import Builder
from CreateGroup import CreateGroup

import os.path
from kivy.resources import resource_add_path
KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'ui'))

resource_add_path(KV_PATH)

class Application(App):
    def build(self):
        return CreateGroup.CreateGroup()

if __name__ == "__main__":
    Application().run()
