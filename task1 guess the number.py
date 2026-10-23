# Задание упражнения:
# 1. Напишите функцию (guessing_game), которая не принимает аргументы.
# 2. При вызове функция выбирает случайное целое число от 0 до 100 (включительно).
# 3. Затем попросите пользователя угадать, какое число было выбрано.
# 4. Каждый раз, когда пользователь будет вводить значение, программа будет показывать одно из следующих сообщений:
    # — Слишком большое
    # — Слишком маленькое
    # — То, что нужно
# 5. Если пользователь угадает число, программа завершит свою работу. В противном случае пользователю предложат
# повторить попытку.
# 6. Программа завершается только после того, как пользователь угадал.



#подключение к базе и sql запрос как пример
import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=(localdb)\\MSSQLLocalDB;"
    "DATABASE=AdventureWorks2025;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

cursor = connection.cursor()

cursor.execute(""" 
    SELECT TOP 10
        FirstName,
        LastName
    FROM Person.Person
""")

for row in cursor.fetchall():
    print(row.FirstName, row.LastName)

connection.close()