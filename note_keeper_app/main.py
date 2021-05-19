from kivymd.app import MDApp
from kivy.lang.builder import Builder

from utils.database_helper import DatabaseHelper
from models.note import Note

from models.list_item import ListItem


class MainApp(MDApp):
    database = None

    def build(self):
        self.load_all_kv_files()
        return Builder.load_file('note_keeper_app.kv')

    def load_all_kv_files(self):
        Builder.load_file('screens/add_note.kv')
        Builder.load_file('screens/all_notes.kv')

    def on_start(self):
        self.database = DatabaseHelper()
        self.database.initialize_database()
        self.database.create_table()

        self.fetch_data_from_db()

    # Showing the list data
    def fetch_data_from_db(self):
        lists = self.root.ids.all_notes.ids.note_lists
        data = self.database.fetch_data()

        for i in data:
            lists.add_widget(ListItem(
                text=i.title,
                secondary_text=i.description,
                id=i.id,
                on_press=self.delete_list_item
            ))

    # Add a note
    def add_note(self):
        title = self.root.ids.add_note.ids.title.text
        des = self.root.ids.add_note.ids.descrip.text

        # Creating a Note object and pass its values
        note = Note(id=None, title=title, description=des)
        self.database.insert_data(note)

        self.clear_the_note_inputs()
        self.update_lists()

    # To clear the input fields
    def clear_the_note_inputs(self):
        self.root.ids.add_note.ids.title.text = ''
        self.root.ids.add_note.ids.descrip.text = ''

    # show the data
    def show_data(self):
        self.change_screen("all_notes")

    def change_screen(self, name: str):
        self.root.current = name

    # delete the note
    def delete_list_item(self, obj):
        id = self.get_id_from_list_item(obj)
        self.database.delete_note(id)
        self.update_lists()

    # getting note id from list item
    def get_id_from_list_item(self, obj):
        return obj.id

    # update according to the delete or add
    def update_lists(self):
        self.root.ids.all_notes.ids.note_lists.clear_widgets()
        self.on_start()

    # On closing the app
    def on_stop(self):
        self.database.close_connection()
        print('Connection closed!')


if __name__ == '__main__':
    MainApp().run()
