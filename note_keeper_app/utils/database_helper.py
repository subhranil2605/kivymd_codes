import os
import sqlite3

try:
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()

except Exception as e:
    print(str(e))

class DatabaseHelper:
    noteTable = 'note_table'
    colId = 'id'

    colTitle = 'title'
    colDescription = 'description'
    colDate = 'date'

    def _create_table(self, db):
        cur = db.cursor()
        cur.execute(f'''
            CREATE TABLE {self.noteTable}({self.colId} INTEGER PRIMARY KEY AUTOINCREMENT, {self.colTitle} TEXT, {self.colDescription} TEXT, {self.colDate} TEXT)
        ''')

    def insertNote(self,id, title, des, date):
        con = sqlite3.connect('notes.db')
        cur = con.cursor()

        cur.execute(f"INSERT INTO {self.noteTable} VALUES (?, ?, ?, ?)", (id, title, des, date))
        # con.close()


