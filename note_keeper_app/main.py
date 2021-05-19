# ptyhon modules imports
import datetime
import asynckivy

# kivy imports
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.clock import Clock

# project imports
from utils.database_helper import DatabaseHelper
from models.note import Note
from models.list_item import ListItem



# Starting of app
class MainApp(MDApp):
    database = None

    def build(self):
        self.load_all_kv_files()
        return Builder.load_file('note_keeper_app.kv')

    def load_all_kv_files(self):
        Builder.load_file('screens/add_note.kv')
        Builder.load_file('screens/all_notes.kv')
        Builder.load_file('models/list_item.kv')
        Builder.load_file('screens/show_note.kv')
        Builder.load_file('screens/loading_screen.kv')

    def on_start(self):
        self.database = DatabaseHelper()
        self.database.initialize_database(self.directory)
        self.database.create_table()

        self.fetch_data_from_db()

    # Showing the list data
    def fetch_data_from_db(self):
        lists = self.root.ids.all_notes.ids.note_lists
        data = self.database.fetch_data()

        for i in data:
            lists.add_widget(ListItem(
                title=i.title,
                description=i.description,
                id=i.id,
                date=i.date,
                on_press=self.show_note
            ))

    # Add a note
    def add_note(self):
        async def some_task():
            title = self.root.ids.add_note.ids.title.text
            des = self.root.ids.add_note.ids.descrip.text
            date = self.getting_date()

            # Creating a Note object and pass its values
            note = Note(id=None, title=title, description=des, date=date)
            current_screen = self.root.current
            self.change_screen('loading')
            await asynckivy.run_in_thread(lambda :self.database.insert_data(note))
            self.clear_the_note_inputs()
            self.update_lists()

            self.change_screen(current_screen)

        asynckivy.start(some_task())

    # To clear the input fields
    def clear_the_note_inputs(self):
        self.root.ids.add_note.ids.title.text = ''
        self.root.ids.add_note.ids.descrip.text = ''

    # show the data
    def show_data(self):
        self.change_screen("all_notes")
        self.clear_the_note_inputs()

    # Changing the screen
    def change_screen(self, name: str):
        self.root.current = name

    # delete the note
    def delete_list_item(self, obj):
        async def some_task():
            id = self.get_id_from_list_item(obj)
            current_screen = self.root.current
            self.change_screen('loading')
            await asynckivy.run_in_thread(lambda :self.database.delete_note(id))
            self.update_lists()
            self.change_screen(current_screen)
        asynckivy.start(some_task())

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

    def getting_date(self):
        datetime_obj = datetime.datetime.now()
        formatted_date_stamp = datetime_obj.strftime("%d-%m-%Y %I:%M:%S %p")
        return f"{formatted_date_stamp}"

    def show_note(self, obj):
        self.root.ids.show_note.ids.show_title.text = obj.title
        self.root.ids.show_note.ids.show_description.text = obj.description
        self.root.ids.show_note.id = obj.id
        self.root.ids.show_note.date = obj.date
        self.change_screen('show_note')

    def update_note(self, obj):
        async def some_task():
            uid = obj.id
            date = self.getting_date()
            title = obj.ids.show_title.text
            description = obj.ids.show_description.text
            current_screen = self.root.current
            self.change_screen('loading')
            await asynckivy.run_in_thread(lambda : self.database.update_data(title=title, description=description, date=date, id=uid))
            self.update_lists()
            self.change_screen(current_screen)
        asynckivy.start(some_task())


if __name__ == '__main__':
    MainApp().run()
