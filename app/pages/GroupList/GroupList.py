from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button



Builder.load_file('ui/grouplist.kv')
class GroupList(Screen):
    groups = []

    def add_group(self, title, description):
        self.groups.append(title)
        add_group = Button(text=title, height=44, padding=(10, 10), size_hint_y=None)
        self.ids.container.add_widget(add_group)

    def __init__(self, **kvargs):
        super(GroupList, self).__init__(**kvargs)

    def on_navigate_back(self):
        self.parent.current = "CreateGroup"
        self.parent.transition.direction = "right"
