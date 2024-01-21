from NoteManager import NoteManager

if __name__ == "__main__":
    note_manager = NoteManager()

    while True:
        print("\n1. Добавить заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Сохранить заметки в файл")
        print("6. Загрузить заметки из файла")
        print("0. Выйти")

        choice = input("Выберите действие (0-6): ")

        if choice == '1':
            title = input("Введите заголовок: ")
            body = input("Введите текст заметки: ")
            note_manager.add_note(title, body)
            print("Заметка добавлена успешно!")

        elif choice == '2':
            notes = note_manager.list_notes()
            for note in notes:
                print(note)

        elif choice == '3':
            note_id = int(input("Введите номер заметки для редактирования: "))
            note = note_manager.get_note_by_id(note_id)
            if note:
                title = input("Введите новый заголовок: ")
                body = input("Введите новый текст заметки: ")
                note_manager.edit_note(note_id, title, body)
                print("Заметка успешно отредактирована!")
            else:
                print("Заметка не найдена.")

        elif choice == '4':
            note_id = int(input("Введите номер заметки для удаления: "))
            if note_manager.delete_note(note_id):
                print("Заметка успешно удалена!")
            else:
                print("Заметка не найдена.")

        elif choice == '5':
            filename = input("Введите имя файла для сохранения: ")
            note_manager.save_to_json(filename)
            print("Заметки успешно сохранены в файл.")

        elif choice == '6':
            filename = input("Введите имя файла для загрузки: ")
            note_manager.load_from_json(filename)
            print("Заметки успешно загружены из файла.")

        elif choice == '0':
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите действие от 0 до 6.")