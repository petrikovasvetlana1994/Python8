from data_create import name_data, surname_data, adress_data, phone_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком варианте записать данные?\n\n"
                    f"1 Вариант:\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{adress}\n\n"
                    f"2 Вариант:\n"
                    f"{name};{surname};{phone};{adress}\n\n"
                    f"Выберите номер варината: "))

    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print('Успешно!!')




    



def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
        data_first = file.readlines()
        data_first_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_second.append(''.join(data_first[j:i]))
                j = i
        data_first = data_first_second
        print(''.join(data_first))



    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
        data_second = list(file.readlines())

        print(*data_second)
    
    return data_first, data_second



# изменение данных

def put_data():
    var = int(input('Введите номер файла для изменения: '))
    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))
    if var == 1:
        with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
            note = int(input('\nУкажите номер записи для изменения: '))
            list = file.readlines()
            new_list = []
            count = 1
            i = 0
            while i < len(list):
                if count != note:
                    if list[i] != '\n':
                        new_list.append(f'{list[i]}')
                        i += 1
                    else:
                        new_list.append('\n')
                        count += 1
                        i += 1
                else:
                    new_list.extend([name_data() + '\n', surname_data() + '\n', phone_data() + '\n', adress_data() + '\n', '\n'])
                    count += 1
                    i += 5

        with open('data_first_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_list:
                file.write(i)
    if var == 2:
        with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            note = int(input('\nУкажите номер записи для изменения: '))
            list = file.readlines()
            new_list = []
            count = 1
            i = 0
            while i < len(list):
                if count != note:
                    if list[i] != '\n':
                        new_list.append(f'{list[i]}')
                        i += 1
                    else:
                        new_list.append('\n')
                        count += 1
                        i += 1
                else:
                    new_list.append(f'{name_data()};{surname_data()};{phone_data()};{adress_data()}\n')
                    count += 1
                    i += 1
        
        with open('data_second_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_list:
                file.write(i)

        
            '''data_first = data_first[:n] + [f'{name}\n{surname}\n{phone}\n{adress}\n'] + data_first[n+1:]'''

# удаление данных

def delete_data():
    file_num = int(input(f'Укажите файл:\n'
                        f'1 - 1 файл\n'
                        f'2 - 2 файл\n'))
    
    if file_num != 1 and file_num != 2:
        file_num = int(input(f'Укажите файл:\n'
                        f'1 - 1 файл\n'
                        f'2 - 2 файл\n'))

    if file_num == 1:
        with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
            note = int(input('\nУкажите номер записи, которую Вы хотите удалить: '))
            list = file.readlines()
            new_list = []
            count = 1
            i = 0
            while i < len(list):
                if count != note:
                    if list[i] != '\n':
                        new_list.append(f'{list[i]}')
                        i += 1
                    else:
                        new_list.append('\n')
                        count += 1
                        i += 1
                else:
                    count += 1
                    i += 5
                
        with open('data_first_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_list:
                file.write(i)

    if file_num == 2:
        with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            note = int(input('\nУкажите номер записи, которую Вы хотите удалить: '))
            list = file.readlines()
            new_list = []
            count = 1
            i = 0
            while i < len(list):
                if count != note:
                    if list[i] != '\n':
                        new_list.append(f'{list[i]}')
                        i += 1
                    else:
                        new_list.append('\n')
                        count += 1
                        i += 1
                else:
                    count += 1
                    i += 2
            
        with open('data_second_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_list:
                file.write(i)