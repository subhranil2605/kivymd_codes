import sqlite3


class DatabaseHelper:

    # Initialize the database connection
    def initialize_database(self):
        self.conn = sqlite3.connect('notes.db')
        self.cur = self.conn.cursor()

    # Creating Table
    def create_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS note_table (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT)
        ''')
        self.conn.commit()

    # Fetching all the data from the database as a list
    def fetch_data(self):
        result = self.cur.execute("SELECT * FROM note_table")
        for row in result:
            print(row[0])

    # Inserting data

    def insert_data(self, title, des):
        try:
            self.cur.execute(
                f'INSERT INTO note_table (title, description) VALUES (?, ?)', (title, des))
            self.conn.commit()

        except Exception as e:
            print(str(e))

    # Deleting the data
    def delete_data(self, id):
        try:
            self.cur.execute(''' 
                DELETE FROM note_table WHERE id = ?
            ''', (id, ))

            self.conn.commit()
        except Exception as e:
            print(str(e))

    # Closing the connection
    def close_connection(self):
        self.conn.commit()
        self.conn.close()


# database = DatabaseHelper()
# database.initialize_database()
# database.create_table()
# database.insert_data("Roni", "Des")
# database.delete_data(1)
# database.fetch_data()
# database.close_connection()
# print("done")


# class Note:
#     def __init__(self, title, description, id=None):
#         self.title = title
#         self.description = description
#         self.id = id

#     @classmethod
#     def create_note_from_dict(cls, note_data: dict):
#         return cls(
#             title=note_data['title'],
#             description=note_data['description']
#         )


# note = Note("my my", "friza")
# print(note.title)
# print(note.description)
# print(note.id)
# my_note = {'title': "hyyy", "description": "gnfjg"}
# test = Note.create_note_from_dict(my_note)
# print(test.title)
# print(test.description)
# print(test.id)
