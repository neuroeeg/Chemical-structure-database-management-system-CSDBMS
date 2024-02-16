import csv

def search(item):
    with open('benzimidazole.csv', encoding='utf-8') as file:
        rows = csv.DictReader(file)
        for i in rows:
            if item in i.values():
                for j in i.items():
                    print(j[0], ': ', j[1], sep='')
                print()

def advanced_search(field, item): #Инструмент поиска по базе. Первый аргумент - в каком поле ищем, второй - что ищем
    with open('benzimidazole.csv', encoding='utf-8') as file:
        rows = csv.DictReader(file) #Генератор списка словарей, каждый элемент - словарь, содержащий значения строки базы, т.е. об одном веществе. Т.к. генератор - потребляет мало памяти, т.е. масштабируется
        for i in rows:
            if i[field] == item: #Планируется заменить на r-строки для поиска неполных совпадений
                for j in i.items():
                    print(j[0], ': ', j[1], sep='')
                print()

def insert(item = list()): #Инструмент добавления новых элементов. item - информация, которую добавляем.
    work_list = []
            
    with open('benzimidazole.csv', encoding='utf-8-sig') as file: #Записывает информацию из файла в переменную функции в качестве копии. После выхода из функции, копия удаляется
        rows = csv.DictReader(file, delimiter=',')
        for row in rows:
            work_list.append(row)
        file.close()

    with open('benzimidazole.csv', 'w', encoding='utf-8-sig') as file: #Добавляет в переменную новую строку, после чего перезаписывает измененную таблицу в файл. Требует внести в новую строку значения всех столбцов. Ищу, как сделать автозамену. Один из кандидатов на переработку - мне не нравится, что файл перезаписывается, но других враиантов я пока не нашел.
        columns = ['id', 'Автор', 'Шифр', 'IUPAC', 'SMILES', 'Молекулярная масса', 'Принадлежность', 'Источник_1', 'Активность_1', 'Величина_1', 'Источник_2', 'Активность_2', 'Величина_2', 'Источник_3', 'Механизм', 'Источник_4']
        new_item = {k:v for k, v in zip(columns, item)}
        work_list.append(new_item)
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in work_list:
            writer.writerow(row)
        file.close()
        print('Информация добавлена')

def change(code, field=None, new_item=''): #Изменяет значения в строке как адресно - одну конкретную ячейку - так и массово, т.е. всю строку. Если не установлено поле, то меняется вся строка, кроме айди. Внести запрет на замену айди
    work_list = []
    columns = ['id', 'Автор', 'Шифр', 'IUPAC', 'SMILES', 'Молекулярная масса', 'Принадлежность', 'Источник_1', 'Активность_1', 'Величина_1', 'Источник_2', 'Активность_2', 'Величина_2', 'Источник_3', 'Механизм', 'Источник_4']
    
    with open('benzimidazole.csv', encoding='utf-8-sig') as file: #Аналогично функции добавления
        rows = csv.DictReader(file, delimiter=',')
        for row in rows:
            work_list.append(row)
        file.close()

    with open('benzimidazole.csv', 'w', encoding='utf-8-sig') as file: #Сперва заменяем значение поля/строки в переменной, потом - аналогично добавлению
        if field:
            for i in work_list:
                if i[id] == code:
                    i[field] = new_item
        else:
            for i in work_list:
                if i[id] == code:
                    i = new_item

        writer = csv.DictWriter(file, fieldnames=columns, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in work_list:
            writer.writerow(row)
        file.close()
        print('Информация изменена')

def delete(code, field): #Если не установлено поле, то удаляется вся строка, т.е. заменяется на None
    work_list = []
            
    with open('benzimidazole.csv', encoding='utf-8-sig') as file:
        rows = csv.DictReader(file, delimiter=',')
        for row in rows:
            work_list.append(row)
        file.close()

    with open('benzimidazole.csv', 'w', encoding='utf-8-sig') as file:
        columns = ['id', 'Автор', 'Шифр', 'IUPAC', 'SMILES', 'Молекулярная масса', 'Принадлежность', 'Источник_1', 'Активность_1', 'Величина_1', 'Источник_2', 'Активность_2', 'Величина_2', 'Источник_3', 'Механизм', 'Источник_4']

        if field:
            for i in work_list:
                if i['id'] == code:
                    i[field] = None
        else:
            new_item = {k:None for k in columns}
            for i in work_list:
                if i['id'] == code:
                    i = new_item

        writer = csv.DictWriter(file, fieldnames=columns, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in work_list:
            writer.writerow(row)
        file.close()
        print('Информация удалена')

task = input('Выберите номер задачи:\n\t1. Найти вещество\n\t2. Найти вещество (продвинутый поиск)\n\t3. Добавить вещество\n\t4. Изменить значение\n\t5. Удалить значение (пока не реализовано)\n')

if task == '1':
    search_item = input('Введите искомое значение: ')
    search(search_item)
        
if task == '2':
    search_field = input('Введите поле поиска: ')
    search_item = input('Введите искомое значение: ')
    advanced_search(search_field, search_item)

if task == '3':
    print('Введите через запятую значения полей в следующем порядке: id, Автор, Шифр, IUPAC, SMILES, Молекулярная масса, Принадлежность, Источник, Активность, Величина, Источник, Активность, Величина, Источник, Механизм, Источник.\nЕсли значение отсутствует или неизвестно, напечатайте на его месте пробел')#Возможно, стоит сделать ввод в несколько строк
    new_str = input().split(', ')
    insert(new_str)
    
if task == '4': #Work in progress
    print('Введите id строки, которую планируете изменять, и название поля, если намерены менять конкретно его. В случае если поле не указано, будет изменена вся запись, соответственно, необходимо указать параметры для всех полей')
