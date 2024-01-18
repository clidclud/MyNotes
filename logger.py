from data import *

def user_command():
    print('Меню:\n'
          '1. Создать заметку\n'
          '2. Открыть список заметок\n'
          '3. Выход\n')

def input_note():
    id = id_data()
    title = title_data()
    text = text_data()
    date_of_creation = date_of_creation_data()
    date_of_change = date_of_change_data()
    print('\nЗаметка сохранена\n')
    return f'{id}\n{title}\n{text}\n{date_of_creation}\n{date_of_change}\n\n'

def add_note():
    note = input_note()
    with open('my_notes.json', 'a', encoding='utf-8') as data:
        data.write(note)

def list_of_notes():
    with open('my_notes.json', 'r', encoding='utf-8') as data:
        print(data.read())