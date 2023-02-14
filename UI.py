from typing import Callable
def help():
    print("""Доступные команды:
                add - добавить заметку,
               find - поиск по произвольному параметру,
             change - изменить заметку,
                del - удалить заметку,
               exit - выйти из программы.""")


def add():
    print("Введите заголовок: ", end="")
    title = input()
    print("Введите текст: ", end="")
    content = input()
    return title, content


# TODO: Сделать уведомлениям вывод ID созданной заметки.
def add_result_view(success: bool):
    if not success:
        print("""Не удалось создать заметку.
                 Возможно, файла базы данных удален, перемещен, переименован или заблокирован.""")
    else:
        print("Заметка создана.")


def find():
    print("""Для поиска доступны следующие ключи:
             1 - ID,
             2 - заголовок
             3 - текст
             4 - дата создание
             5 - время создания""")
    key = 0
    while key not in ["1", "2", "3", "4", "5"]:
        print("Введите ключ (1-5) для поиска: ", end="")
        key = input()
    translation_dict = {
        "1": "ID",
        "2": "title",
        "3": "content",
        "4": "creation_date",
        "5": "creation_time"
    }
    search_key = translation_dict.get(key)

    print("Введите значение: ", end="")
    search_value = input()

    return search_key, search_value


def find_result_view(results: list):
    if len(results) == 0:
        print("В базе данных не найдено записей соответствующих заданным параметрам поиска.")
    for note in results:
        print(f"""ID: {note[0]},\nЗаголовок: {note[1]},\nТекст: {note[2]},\nДата и время создания: {note[3]}, {note[4]}. 
                """)


def change():
    print("Введите ID заметки для изменения: ", end="")
    id = input()

    print("""Для изменения доступны следующие ключи:
             1 - заголовок,
             2 - текст.""")
    key = 0
    while key not in ["1", "2"]:
        print("Введите ключ (1-2) для изменения: ", end="")
        key = input()
    translation_dict = {
        "1": "title",
        "2": "content",
    }
    column_name = translation_dict.get(key)

    print("Введите новое значение выбранного ключа: ", end="")
    new_value = input()

    return column_name, new_value, id


def delete():
    print("Введите ID заметки для удаления: ", end="")
    id = input()
    return id
