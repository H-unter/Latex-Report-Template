from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder

KV = '''
<DeletableLabel>:
    orientation: 'horizontal'
    size_hint_y: None
    height: dp(30)

    Label:
        text: root.text
        size_hint_x: 0.8

    Button:
        text: "Delete"
        size_hint_x: 0.2
        on_release: root.delete_section()

<SectionList>:
    name_input: name_input
    subject_code_input: subject_code_input
    title_input: title_input
    section_name_input: section_name_input
    sections_rv: sections_rv

    orientation: 'vertical'
    padding: 10
    spacing: 10

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 30

        Label:
            text: 'Name:'
        TextInput:
            id: name_input
            multiline: False
            size_hint_x: 2

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 30

        Label:
            text: 'Subject Code:'
        TextInput:
            id: subject_code_input
            multiline: False
            size_hint_x: 2

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 30

        Label:
            text: 'Title:'
        TextInput:
            id: title_input
            multiline: False
            size_hint_x: 2

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 30

        Label:
            text: 'Enter section name:'
        TextInput:
            id: section_name_input
            multiline: False
            size_hint_x: 2
        Button:
            text: 'Add Section'
            on_release: root.add_section()

    BoxLayout:
        size_hint_y: None
        height: 30
        Button:
            text: 'Clone and Generate Report'
            on_release: root.clone_and_generate()

    RecycleView:
        id: sections_rv
        viewclass: 'DeletableLabel'
        size_hint: (1, None)
        size: (self.width, 180)
        RecycleBoxLayout:
            default_size: None, dp(30)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'

# ... rest of your KV ...

'''

Builder.load_string(KV)

class DeletableLabel(RecycleDataViewBehavior, BoxLayout):
    text = StringProperty()

    def delete_section(self):
        # Find the item in the RecycleView data and remove it
        app = App.get_running_app()
        data = app.root.ids.sections_rv.data
        # Find the dictionary in the data list with a matching 'text' value
        item_to_delete = next((item for item in data if item['text'] == self.text), None)
        if item_to_delete:
            data.remove(item_to_delete)
            app.root.ids.sections_rv.refresh_from_data()

class SectionList(BoxLayout):
    name_input = ObjectProperty()
    subject_code_input = ObjectProperty()
    title_input = ObjectProperty()
    section_name_input = ObjectProperty()
    sections_rv = ObjectProperty()

    def add_section(self):
        section_name = self.section_name_input.text
        if section_name:
            self.sections_rv.data.append({'text': f"{section_name}.tex"})
            self.section_name_input.text = ''  # Clear the input field
            self.sections_rv.refresh_from_data()

    def clone_and_generate(self):
        # Here we would have the logic to clone the repository and rename files
        # according to the names given by the user.
        # This is a placeholder for the actual functionality.
        pass
class LatexTemplateApp(App):
    def build(self):
        return SectionList()

if __name__ == '__main__':
    LatexTemplateApp().run()
