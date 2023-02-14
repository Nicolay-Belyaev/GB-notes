import datetime
import sqlite3
from typing import Callable


def create(add):
    title, content = add()
    now = datetime.datetime.now()
    values = (title, content, str(now.date()), str(now.time())[0:5])
    request = "INSERT INTO notes (title, content, creation_date, creation_time) VALUES (?, ?, ?, ?)"

    with sqlite3.connect('database.sqlite') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(request, values)
            return True
        except sqlite3.DatabaseError:
            return False


def read(find: Callable):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    search_key, search_value = find()

    cursor.execute('SELECT * FROM notes WHERE "{}" = ?'.format(search_key), (search_value,))

    result = cursor.fetchall()
    connection.close()
    return result


def update(change: Callable):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    column_name, new_value, note_id = change()

    cursor.execute('UPDATE notes SET "{}" = ? WHERE ID = ?'.format(column_name), (new_value, note_id))
    connection.commit()
    connection.close()


def delete(delete: Callable):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    note_id = delete()

    cursor.execute('DELETE FROM notes WHERE ID = ?', (note_id,))

    connection.commit()
    connection.close()

