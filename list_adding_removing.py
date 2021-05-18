from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.list import OneLineListItem

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: 30
        padding: 30
        
        MDRaisedButton:
            text: "Add List Item"
            pos_hint: {"top": 1}
            on_release: app.add_item()
    
            
        ScrollView:
            MDList:
                id: list
'''

values = [1, 2, 3, 4, 5]


class MainApp(MDApp):
    note_list = []
    counter = 0

    def build(self):
        if len(self.note_list) == 0:
            self.update_list()

        return Builder.load_string(KV)

    def on_start(self):
        for i in range(self.counter):
            self.root.ids.list.add_widget(OneLineListItem(
                text=str(i),
                on_press=self.delete_item
            ))

    def add_item(self):
        self.root.ids.list.add_widget(OneLineListItem(
            text=str(self.counter),
            on_press=self.delete_item
        ))
        self.counter += 1

    def delete_item(self, obj):
        self.root.ids.list.remove_widget(obj)
        self.counter -= 1
        print(self.note_list)

    def update_list(self):
        self.note_list = values
        self.counter = len(self.note_list)


if __name__ == '__main__':
    MainApp().run()
