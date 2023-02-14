import DB
import UI

# TODO: команды showall, deleteall
# TODO: инициализатор БД с проверкой существования БД
# TODO: try-except и with для CRUD, вынести коннект к БД в отдельную функцию
# TODO: допилить поиск через LIKE (что бы не подставлять % на вводе)
# TODO: уведомления о результате операции (update, del)


while True:
    print("Введите команду или нажмите Enter для получения справки: ", end="")
    current_command = input()
    match current_command:
        case "exit":
            break
        case "":
            UI.help()
        case "add":
            UI.add_result_view(DB.create(UI.add))
        case "find":
            UI.find_result_view(DB.read(UI.find))
        case "change":
            DB.update(UI.change)
        case "del":
            DB.delete(UI.delete)
