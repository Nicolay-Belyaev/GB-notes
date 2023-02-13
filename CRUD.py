import datetime
import sqlite3


def create(add):
    title, content = add()
    sqlite_connection = sqlite3.connect('database.sqlite')
    cursor = sqlite_connection.cursor()
    now = datetime.datetime.now()

    values = (title, content, str(now.date()), str(now.time())[0:5])
    sql_request = "INSERT INTO notes (title, content, creationdate, creationtime) VALUES (?, ?, ?, ?)"
    cursor.execute(sql_request, values)
    sqlite_connection.commit()

    sqlite_connection.close()


def read(find):
    sqlite_connection = sqlite3.connect('database.sqlite')
    cursor = sqlite_connection.cursor()
    search_key, search_value = find()

    # Небезопасный метод, но оказывается нельзя так просто (как со значениями, values) подставить идентификаторы.
    # Приходится выкручиваться.
    cursor.execute('SELECT * FROM notes WHERE "{}" LIKE ?'.format(search_key), (search_value,))

    result = cursor.fetchall()
    sqlite_connection.close()
    return result


def update(change):
    sqlite_connection = sqlite3.connect('database.sqlite')
    cursor = sqlite_connection.cursor()
    column_name, new_value, note_id = change()

    cursor.execute('UPDATE notes SET "{}" = ? WHERE ID = ?'.format(column_name), (new_value, note_id))
    sqlite_connection.commit()
    sqlite_connection.close()


def delete(delete):
    sqlite_connection = sqlite3.connect('database.sqlite')
    cursor = sqlite_connection.cursor()
    note_id = delete()

    cursor.execute('DELETE FROM notes WHERE ID = ?', (note_id,))

    sqlite_connection.commit()
    sqlite_connection.close()

