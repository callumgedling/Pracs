from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicWidgetsAppTwo(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Callum", "Frank", "Andrea", "Keegan"]

    def build(self):
        self.title = "Dynamic Widgets Two"
        self.root = Builder.load_file('dynamic_widgets_two.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.names_box.add_widget(temp_label)

    def press_entry(self, instance):
        name = instance.id
        self.status_text = "{}".format(name)


DynamicWidgetsAppTwo().run()
