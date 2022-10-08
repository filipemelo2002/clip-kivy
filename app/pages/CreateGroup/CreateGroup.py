import kivy
kivy.require('2.1.0')

from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen

Builder.load_file('ui/creategroup.kv')
class CreateGroup(Screen):
    pass
