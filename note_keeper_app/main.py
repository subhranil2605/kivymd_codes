from kivymd.app import MDApp
from kivy.lang.builder import Builder

from utils.database_helper import DatabaseHelper

KV = '''
MDScreen:
    
    MDBoxLayout:
        orientation: 'vertical'
        spacing: 20
        padding: 30
        adaptive_height: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        
        MDLabel:
            text: "Add Note"
            halign: 'center'
            font_size: 35
        
        MDTextField:
            id: title
            hint_text: "Title"
            
        MDTextField:
            id: descrip
            hint_text: "Description"
        
        MDRaisedButton:
            text: "Add"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_press: app.add_note()
'''


class MainApp(MDApp):
    database = None

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.database = DatabaseHelper()
        self.database.initialize_database()
        self.database.create_table()

    def add_note(self):
        title = self.root.ids.title.text
        des = self.root.ids.descrip.text
        self.database.insert_data(title, des)

    def on_stop(self):
        self.database.close_connection()


if __name__ == '__main__':
    MainApp().run()
