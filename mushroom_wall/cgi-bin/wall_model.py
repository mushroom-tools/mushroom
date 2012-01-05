import sqlite3

db_name = '../data/wall_db.sqlite'


def put_text(name, text):
    connection = sqlite3.connect(db_name)
    connection.text_factory = str
    cursor = connection.cursor()
    result = cursor.execute("INSERT INTO wall_logs (name, content, is_text) VALUES (?,?,1)", (name, text))
    connection.commit()
    connection.close()


def put_filename(name, filename):
    connection = sqlite3.connect(db_name)
    connection.text_factory = str
    cursor = connection.cursor()
    result = cursor.execute("INSERT INTO wall_logs (name, content, is_text) VALUES (?,?,0)", (name, filename))
    connection.commit()
    connection.close()


def get_transcript_from_date(year, month, day):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("SELECT (name, content, datetime, is_text) FROM wall_logs ORDER BY datetime")
    #data = 
    return(response)