from utils.database_helper import DatabaseHelper

database = DatabaseHelper()


database.initialize_database()
print("Success")

database.insertNote(0 ,'title', 'desci', '19.05.2021')