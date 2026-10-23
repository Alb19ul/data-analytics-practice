#Задача. Проверка данных по следующим правилам
#Правила:
# 1. name не должно быть пустым.
# 2. age должно быть от 0 до 120 включительно.
# 3. В email должен присутствовать символ @.
# 4. Для каждой неправильной записи вывести её id и найденные ошибки.
# 5. В конце вывести:
#    - сколько всего записей;
#    - сколько корректных;
#    - сколько с ошибками.

#
# 5. Предлагаю небольшое усложнение
# Не меняя исходные данные, попробуй переписать программу с двумя дополнительными требованиями:
# 1. Не использовать вложенные циклы для поиска ошибок по id.
# 2. Добавить в конце статистику по типам ошибок:
# Всего записей: 7
# Корректных: 2
# С ошибками: 5
#
# Пустое имя: 2
# Неверный возраст: 3
# Неверный email: 2
#
#
# Обрати внимание: сумма количества ошибок может быть больше количества некорректных записей.
# И ещё один вопрос для размышления: что произойдёт с твоей программой, если у пользователя вообще отсутствует ключ age или вместо числа там окажется строка "25"?

#добавление типа ошибки missing_value, invalid_type, out_of_range, missing_field.

users = [
    {"id": 1, "name": "Anna", "age": 25, "email": "anna@mail.com"},
    {"id": 2, "name": "Ivan", "age": 17, "email": "ivanmail.com"},
    {"id": 3, "name": "", "age": 31, "email": "kate@mail.com"},
    {"id": 4, "name": "Petr", "age": -5, "email": "petr@mail.com"},
    {"id": 5, "name": "Maria", "age": 42, "email": "maria@mail.com"},
    {"id": 6, "name": "Alex", "age": 150, "email": "alexmail.com"},
    {"id": 7, "name": "", "age": 131, "email": "kate22@mail.com"},
    {"id": 8, "name": "Kirill", "age": 29, "email": ""},
    {"id": 9, "age": 31, "email": 'gfkdjkg@mail.com'},
    {"id": 10, "name": "Helena", "age": 26, "email": "Helena@mail.com"},
    {"id": 11, "age": "34"},
    {"id": 12, "name": "Ekaterina", "email": "anna@mail.com"}
]

wrong_data = []
for user in users:
    incorrect_String = {}
    if 'name' not in user:
        print('имени нет в словаре')
    elif user.get('name') == "" :
        incorrect_String['id'] = user.get('id')
        incorrect_String['name'] = user.get('name')
    if 'age' not in user:
        print('возраста нет в словаре')
    elif not isinstance (user.get('age'),int) or (120 < user.get('age') or user.get('age')) < 0:
        incorrect_String.update({'id':user.get('id'),'age':user.get('age')})
    if 'email' not in user:
        print('почтового адреса нет в словаре')
    elif "@" not in user.get('email'):
        incorrect_String.update({'id': user.get('id'), 'email': user.get('email')})

    #if incorrect_String!={}:
    if incorrect_String:
        #print(incorrect_String)
        wrong_data.append(incorrect_String)


#выводим записи с ошибками - для тестирования!
for strW in wrong_data:
     print(strW, end="\n")


#всего записей
print(f'всего записей = {len(users)}')
#сколько записей с ошибками
print(f'всего записей с ошибками = {len(wrong_data)}')
#корректных записей
print(f'всего записей без ошибок = {len(users) - len(wrong_data)}')


n,a,m = 0,0,0
for data in wrong_data:
    if 'name' in data:
        n += 1
    if 'age' in data:
        a += 1
    if 'email' in data:
        m +=1
# Пустое имя: 2
print(f'записей с пустым именем  = {n}')
# Неверный возраст: 3
print(f'записей с неверным возрастом  = {a}')
# Неверный email: 2
print(f'записей с некорректным email  = {m}')