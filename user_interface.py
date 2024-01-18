from logger import *
def user_interface():
    with open('my_notes.json', 'a', encoding='utf-8'): # создаем файл если его нет
        pass
    while user_command != '3':
        user_command()
        command = input('Введите номер операции: ')
        while command not in ('1', '2', '3'):
            print('\nОшибка: Неккоректный ввод')
            user_command()
            command = input('Введите номер операции: ')
        match command:
            case '1': add_note()
            case '2': list_of_notes()
            case '3': exit()



