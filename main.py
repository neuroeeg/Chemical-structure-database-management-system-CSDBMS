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
            if i[field] == item: #Мб заменить на аналог IN
                for j in i.items():
                    print(j[0], ': ', j[1], sep='')
                print()

def insert(item = list()): #Инструмент добавления новых элементов. item - информация, которую добавляем.
    work_list = []
            
    with open('benzimidazole.csv', encoding='utf-8-sig') as file:
        rows = csv.DictReader(file, delimiter=',')
        for row in rows:
            work_list.append(row)
        print(len(work_list))
        print(work_list[0], '\n', work_list[-1])
        file.close()

    with open('benzimidazole.csv', 'w', encoding='utf-8-sig') as file:
        columns = ['Автор', 'Шифр', 'IUPAC', 'SMILES', 'Молекулярная масса', 'Принадлежность', 'Источник_1', 'Активность_1', 'Величина_1', 'Источник_2', 'Активность_2', 'Величина_2', 'Источник_3', 'Механизм', 'Источник_4']#И здесь, и в файле нужно сделать названия уникальными
        new_item = {k:v for k, v in zip(columns, item)}
        print(len(work_list))
        print(work_list[0], '\n', work_list[-1])
        work_list.append(new_item)
        print(len(work_list))
        print(work_list[0], '\n', work_list[-1])
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in work_list:                     # запись строк
            writer.writerow(row)
        file.close()
        print('Информация добавлена')

def change(id, field, new_item): #Пока что менять адресно не получится. нужно что-то вроде уникального id для каждой отдельной строки
    pass

def delete(id, field): #Пока что удалять адресно не получится. нужно что-то вроде уникального id для каждой отдельной строки
    pass

task = input('Выберите номер задачи:\n\t1. Найти вещество\n\t2. Найти вещество (продвинутый поиск)\n\t3. Добавить вещество\n\t4. Изменить значение (пока не релизовано)\n\t5. Удалить значение (пока не реализовано)\n')

if task == '1':
    search_item = input('Введите искомое значение: ')
    search(search_item)
        
if task == '2':
    search_field = input('Введите поле поиска: ')
    search_item = input('Введите искомое значение: ')
    advanced_search(search_field, search_item)

if task == '3':
    print('Введите через запятую значения полей в следующем порядке: Автор, Шифр, IUPAC, SMILES, Молекулярная масса, Принадлежность, Источник, Активность, Величина, Источник, Активность, Величина, Источник, Механизм, Источник.\n Если значение отсутствует или неизвестно, напечатайте на его месте пробел')
    new_str = input().split(', ')
    insert(new_str)
