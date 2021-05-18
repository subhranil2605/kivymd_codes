from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.list import OneLineAvatarIconListItem, IconRightWidget

KV = '''  
<ListItemWithDeleteIcon>:

    IconRightWidget:
        icon: "android"
        on_release: app.delete(self.parent.parent)
              
MDBoxLayout:

    ScrollView:
    
        MDList:        
            id: list
                  
'''


class ListItemWithDeleteIcon(OneLineAvatarIconListItem):
    pass


class MainApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        # initialized the lists
        for i in range(10):
            self.root.ids.list.add_widget(ListItemWithDeleteIcon(
                text=str(i)
            ))

    def delete(self, obj):
        self.root.ids.list.remove_widget(obj)


if __name__ == '__main__':
    MainApp().run()
