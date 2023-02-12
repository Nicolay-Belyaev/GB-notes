import datetime
import sqlite3
from typing import List, Any


#TODO: make it work with try-except + with


def create(title: str, content: str):
    sqlite_connection = sqlite3.connect('database.sqlite')
    cursor = sqlite_connection.cursor()
    now = datetime.datetime.now()

    values = (title, content, str(now.date()), str(now.time())[0:5])
    sql_request = "INSERT INTO notes (title, content, creationdata, creationtime) VALUES (?, ?, ?, ?)"
    cursor.execute(sql_request, values)
    sqlite_connection.commit()

    sqlite_connection.close()


def read(search_key: str, search_value):
    sqlite_connection = sqlite3.connect('database.sqlite')
    cursor = sqlite_connection.cursor()

    # Небезопасный метод, но оказывается нельзя так просто (как со значениями, values) подставить идентификаторы.
    # Приходится выкручиваться.
    cursor.execute('SELECT * FROM notes WHERE "{}" = ?'.format(search_key), (search_value,))

    result = cursor.fetchall()
    sqlite_connection.close()
    return result


def update(column_name, new_value, note_id):
    sqlite_connection = sqlite3.connect('database.sqlite')
    cursor = sqlite_connection.cursor()

    cursor.execute('UPDATE notes SET "{}" = ? WHERE ID = ?'.format(column_name), (new_value, note_id))
    sqlite_connection.commit()
    sqlite_connection.close()


def delete(note_id):
    sqlite_connection = sqlite3.connect('database.sqlite')
    cursor = sqlite_connection.cursor()

    cursor.execute('DELETE FROM notes WHERE ID = ?', note_id)

    sqlite_connection.commit()
    sqlite_connection.close()

