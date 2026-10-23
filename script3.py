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
from operator import contains
from pprint import pprint
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

users = [
    {"id": 1, "name": "Anna", "age": 25, "email": "anna@mail.com"},
    {"id": 2, "name": "Ivan", "age": 17, "email": "ivanmail.com"},
    {"id": 3, "name": "", "age": 31, "email": "kate@mail.com"},
    {"id": 4, "name": "Petr", "age": -5, "email": "petr@mail.com"},
    {"id": 5, "name": "Maria", "age": 42, "email": "maria@mail.com"},
    {"id": 6, "name": "Alex", "age": 150, "email": "alexmail.com"},
    {"id": 7, "name": "", "age": 131, "email": "kate22@mail.com"},
    {"id": 8, "name": "Kirill", "age": 29, "email": ""}
]

wrongData = []
for user in users:
     if user.get('name') == "" :
         Aaa = {'id': user.get('id'),
                'name': user.get('name')}
         wrongData.append(Aaa)
     if 120 < user.get('age') or user.get('age') < 0:
        if [user.get('id') for item in wrongData if item.get('id') == user.get('id')] == []:
            Aoo = {'id': user.get('id'), 'age': user.get('age')}
            wrongData.append(Aoo)
        else:
            for item in wrongData:
              if item['id'] == user.get('id'):
                 item['age'] = user.get('age')
     if "@" not in user.get('email'):
         if [user.get('id') for item in wrongData if item.get('id') == user.get('id')] == []:
             AAo = {'id': user.get('id'), 'email': user.get('email')}
             wrongData.append(AAo)
         else:
             for item in wrongData:
                 if item['id'] == user.get('id'):
                     item['email'] = user.get('email')






#выводим записи с ошибками
for strW in wrongData:
     print(strW, end="\n")
#всего записей
print(f'всего записей = {len(users)}')
#сколько записей с ошибками
print(f'всего записей с ошибками = {wrongData.__len__()}')
#корректных записей
print(f'всего записей = {users.__len__() - wrongData.__len__()}')