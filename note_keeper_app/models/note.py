

class Note:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

    # To convert fetch data back to a Note
    @classmethod
    def list_to_note(cls, note_list):
        return cls(
            id=note_list[0],
            title=note_list[1],
            description=note_list[2],
        )
