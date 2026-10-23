# M1, M2, M3, M4, M5  = input(f'Введи пять чисел через пробел, а я их отсортирую: ').split()
#
# MassiveOfStr = [M1,M2,M3,M4,M5]
# MassiveOfNum = [int(item) for item in MassiveOfStr]
#
# MassiveOfNum.sort()
# print(f'Вот отсортированный массив: {MassiveOfNum}')



#обход цикла в цикле
i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1