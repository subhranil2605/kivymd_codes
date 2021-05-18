from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.list import OneLineListItem

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class MainApp(MDApp):
    counter = 0
    note_list = []

    def build(self):
        if len(self.note_list) == 0:
            self.update_list()

        return Builder.load_file("list_view_delete.kv")

    def on_start(self):
        # showing the data in the list
        lists = self.root.ids.list
        for i in range(self.counter):
            lists.add_widget(OneLineListItem(
                text=str(self.note_list[i]),
                on_press=self.delete_note
            ))

    # delete note within the list
    def delete_note(self, obj):
        val = obj.text
        values.remove(int(val))
        print(values)

        self.update_list()
        self.update_list_view()

    def update_list(self):
        self.note_list = values
        self.counter = len(values)

    def update_list_view(self):
        self.root.ids.list.clear_widgets()
        self.on_start()


if __name__ == '__main__':
    MainApp().run()
