from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivy.properties import NumericProperty, StringProperty


class ListItem(ThreeLineAvatarIconListItem):
    title = StringProperty()
    description = StringProperty()
    id = NumericProperty()
    icon = StringProperty("delete")
    date = StringProperty()
