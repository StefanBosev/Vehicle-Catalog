import sqlite3

DB_NAME = 'vehicle_catalog.db'

connection = sqlite3.connect(DB_NAME)


connection.cursor().execute('''
    CREATE TABLE IF NOT EXISTS Users 
    (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

connection.cursor().execute('''
    CREATE TABLE IF NOT EXISTS Vehicles
    (
        vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner_id INTEGER NOT NULL,
        model TEXT NOT NULL,
        colour TEXT NOT NULL,
        manufacture_year DATE NOT NULL,
        FOREIGN KEY(owner_id) REFERENCES Users(user_id)
    )
''')

connection.commit()

class DB:
    def __enter__(self):
        self.connection = sqlite3.connect(DB_NAME)
        return self.connection.cursor()

    def __exit__(self, type, value, traceback):
        self.connection.commit()