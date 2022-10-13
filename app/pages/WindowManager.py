from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from CreateGroup import CreateGroup
from GroupList import GroupList

Builder.load_file('ui/windowmanager.kv')
class WindowManager(ScreenManager):
    pass
