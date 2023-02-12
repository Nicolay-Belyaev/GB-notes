import CRUD
import UI

# инициализатор БД с проверкой существования БД
# вынести ui-функции в отдельный файл
# try-execpt и with для CRUD, вынести коннект к БД в отдельную функцию

current_command = ""
while True:
    print("Введите команду или нажмите Enter для получения справки: ", end="")
    current_command = input()
    match current_command:
        case "exit":
            break
        case "":
            print("""Доступные команды:\n"
                        add - добавить заметку,\n 
                       find - поиск по произвольную параметру,\n 
                     change - изменить заметку,\n
                        del - удалить заметку""")
        case "add":
            print("Введите заголовок: ", end="")
            title = input()
            print("Введите текст", end="")
            content = input()
            CRUD.create(title, content)
        case "find":
            print("""Для поиска доступны следующие ключи:\n
                     1 - ID,\n
                     2 - заголовок\n
                     3 - текст\n
                     4 - дата создание\n
                     5 - время создания""")
            key = 0
            while key not in [1, 2, 3, 4, 5]:
                print("Введите ключ (1-5) для поиска: ")
                key = input()
            translation_dict = {
                1: "ID",
                2: "title",
                3: "content",
                4: "creationdate",
                5: "creationtime"
            }
            search_key = translation_dict.get(key)
            print("Введите значение: ")
            search_value = input()
            CRUD.read(search_key, search_value)
        case "change":
            print("Введите ID заметки для изменения: ", end="")
            ID = input()
            print("""Для изменения доступны следующие ключи:\n
                     1 - заголовок,
                     2 - текст""")
            key = 0
            while key not in [1, 2]:
                print("Введите ключ (1-2) для изменения: ")
                key = input()
            translation_dict = {
                1: "title",
                2: "content",
            }
            column_name = translation_dict.get(key)
            print("Введите новое значение выбранного ключа: ")
            new_value = input()
            CRUD.update(column_name, new_value, ID)
        case "del":
            print("Введите ID заметки для удаления: ", end="")
            ID = input()
            CRUD.delete(ID)
