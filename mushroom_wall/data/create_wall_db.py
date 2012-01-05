import sqlite3

connection = sqlite3.connect('wall_db.sqlite')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE wall_logs(
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    content TEXT NOT NULL,
                    datetime DATETIME NOT NULL,
                    is_text BOOLEAN NOT NULL)""")
connection.commit()
connection.close()