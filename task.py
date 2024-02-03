import datetime
file = open('table.txt', 'a+', encoding="utf-8")
while True:
    com = input()

    if com == 'add':
        name = input('Название заметки:')
        body = input('Заметка:')
        file.write(name + '|' + body + '|' + str(datetime.datetime.now()) + '\n')
        print('Заметка добавлена!')
    
    if com == 'all':
        print('Все заметки:')
        file.seek(0)
        for line in file:
            arr = line.split('|')
            print('----------------------------------')
            print('Название:', arr[0])
            print('Заметка:', arr[1])
            print('Дата:', arr[2])
    
    if com == 'find':
        name = input('Название заметки:')
        found = False
        file.seek(0)
        for line in file:
            if line.find(name + '|') == 0:
                arr = line.split('|')
                print('Найдена заметка!')
                print('Название:', arr[0])
                print('Заметка:', arr[1])
                print('Дата:', arr[2])
                found = True
                break

        if not found:
            print('Заметок с таким названием нет :(')

    if com == 'edit':
        name = input('Название заметки:')
        found = False
        file.seek(0)
        for line in file:
            if line.find(name + '|') == 0:
                found = True
                body = input('Новый текст заметки:')
                f = open('table.txt', 'r', encoding="utf-8")
                file_text = f.read()
                f.close()
                f = open('table.txt', 'w', encoding="utf-8")
                f.write(file_text.replace(line, name + '|' + body + '|' + str(datetime.datetime.now()) + '\n'))
                f.close()
                print("Заметка успешно отредактирована!")
                break

        if not found:
            print('Заметок с таким названием нет :(\nВоспользуйтесь командой "add".')

    if com == 'del':
        name = input('Название заметки:')
        found = False
        file.seek(0)
        for line in file:
            if line.find(name + '|') == 0:
                found = True
                f = open('table.txt', 'r', encoding="utf-8")
                file_text = f.read()
                f.close()
                f = open('table.txt', 'w', encoding="utf-8")
                f.write(file_text.replace(line, ''))
                f.close()
                print("Заметка успешно удалена!")
                break

        if not found:
            print('Заметок с таким названием нет :(')

    if com == 'exit':
        break
file.close()