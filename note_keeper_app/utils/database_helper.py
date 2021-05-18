import sqlite3


conn = sqlite3.connect('notes.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS note_table (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT)
''')
print('Data table created')

cur.execute('INSERT INTO note_table (title, description) VALUES ("my_title", "my_description")')

conn.close()