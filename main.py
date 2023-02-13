import CRUD
import UI

# TODO: инициализатор БД с проверкой существования БД
# TODO: try-execpt и with для CRUD, вынести коннект к БД в отдельную функцию
# TODO: пересчитывать поле ID при удалении записей
# TODO: допилить поиск через LIKE (что бы не подставлять % на вводе)
# TODO: уведомления об результате операции.


while True:
    print("Введите команду или нажмите Enter для получения справки: ", end="")
    current_command = input()
    match current_command:
        case "exit":
            break
        case "":
            UI.help()
        case "add":
            CRUD.create(UI.add)
        case "find":
            print(CRUD.read(UI.find))  # TODO: сделать красивый вывод
        case "change":
            CRUD.update(UI.change)
        case "del":
            CRUD.delete(UI.delete)
