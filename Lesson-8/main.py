import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from game import game

save_info("Старт")

try:
    command = sys.argv[1]
except IndexError:
    print("Необходиммо ввести команду или набери 'help' ")
else:
    if command == "list":
        get_list()
    elif command == "create_file":
        try:
            name = sys.argv[2]
        except IndexError:
            print("Необходиммо ввести имя файла")
        else:
            create_file(name)
    elif command == "create_folder":
        try:
            name = sys.argv[2]
        except IndexError:
            print("Необходиммо ввести имя каталога")
        else:
            create_folder(name)
    elif command == "delete_file":
        try:
            name = sys.argv[2]
        except FileNotFoundError:
            print("Нет такой папки(файла), проверьте имя.")
        except IndexError:
            print("Необходиммо ввести имя папки(файла)")
        else:
            delete_file(name)
    elif command == "copy":
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except FileNotFoundError:
            print("Нет такой папки(файла), проверьте имя.")
        except IndexError:
            print("Необходиммо ввести имя папки(файла)")
        else:
            copy_file(name, new_name)
    elif command == "change":
        try:
            name = sys.argv[2]
        except IndexError:
            print("Необходиммо ввести имя каталога")
        except FileNotFoundError:
            print("Нет такой папки(файла), проверьте имя.")
        else:
            change_dir(name)
    elif command == "game":
        game()
    elif command == "help":
        print("list - список файлов и папок")
        print("create_file - создание файла")
        print("create_folder - создание каталога")
        print("delete_file - удаление католога(файла)")
        print("copy - создание копии каталога(файла)")

    save_info("Конец")