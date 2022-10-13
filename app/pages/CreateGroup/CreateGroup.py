from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file('ui/creategroup.kv')
class CreateGroup(Screen):
    def on_save(self):
        title = self.ids.title.text
        description = self.ids.description.text
        if (len(title) == 0 or len(description) == 0):
            self.ids.error_label.opacity = 1
            return
        self.ids.title.text = ""
        self.ids.description.text = ""
        group_list_screen = self.manager.get_screen('GroupList')
        group_list_screen.add_group(title, description)
        self.ids.error_label.opacity = 0
        self.parent.current = "GroupList"
        self.parent.transition.direction = "left"
    def navigate_list(self):
        self.parent.current = "GroupList"
        self.parent.transition.direction = "left"
