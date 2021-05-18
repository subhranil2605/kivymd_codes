from kivymd.app import MDApp
from kivy.lang.builder import Builder

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
    def build(self):
        return Builder.load_string(KV)

    def add_note(self):
        print(self.root.ids.title.text)
        print(self.root.ids.descrip.text)


if __name__ == '__main__':
    MainApp().run()
