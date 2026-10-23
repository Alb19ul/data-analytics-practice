# This is a sample Python script.
import random

Aa = input('Введите ваше имя: ')
print(f'Привет, {Aa}!')
minN = 1
maxN = 5
Ao = random.randint(minN,maxN)
print(f' Число = {Ao}')

Aa_guess = input(f'Угадай число от {minN} до {maxN}, {Aa}: ')
print(f' тип данных = {type(Aa_guess)}')

if int(Aa_guess) == Ao:
    print(f'Угадала!')
else:
 print(f'Ничего, повезет в следующий раз! А загаданное число было {Ao}')