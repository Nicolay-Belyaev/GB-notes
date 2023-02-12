import CRUD
import UI


current_command = ""
while True:
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
            print()

