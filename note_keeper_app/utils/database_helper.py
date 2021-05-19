import sqlite3
from note_keeper_app.models.note import Note


class DatabaseHelper:

    # Initialize the database connection
    def initialize_database(self):
        self.conn = sqlite3.connect('notes.db')
        self.cur = self.conn.cursor()

    # Creating Table
    def create_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS note_table (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, date TEXT)
        ''')
        self.conn.commit()

    # Fetching all the data from the database as a list
    def fetch_data(self):
        result = self.cur.execute("SELECT * FROM note_table")
        note_list = [Note.list_to_note(row) for row in result]
        return note_list

    # Inserting data

    def insert_data(self, note: Note):
        try:
            self.cur.execute(
                f'INSERT INTO note_table (title, description, date) VALUES (?, ?, ?)', (note.title, note.description, note.date))
            self.conn.commit()

        except Exception as e:
            print(str(e))

    # Deleting the data
    def delete_note(self, id):
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

