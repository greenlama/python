from itertools import count, cycle
from random import randint

realisation = 0
while realisation != 1 and realisation != 2:
    realisation = int(input('Реализации итераторов:\n 1 - Итератор, генерирующий целые числа, начиная с указанного.\n '
                            '2 - Итератор, повторяющий элементы некоторого списка, определенного заранее.\n'
                            'Ваш выбор: '))
if realisation == 1:
    start = 0
    stop = 0
    while start < 1:
        start = int(input('Введите целочисленное значение больше нуля: '))
    while stop <= start:
        stop = int(input('Введите конечное целочисленное значение (больше стартового): '))
    for el in count(start):
        if el > stop:
            break
        else:
            print(el)
else:
    cycles = 0
    while cycles < 1:
        my_list = [randint(1, 99) for i in range(int(input("Введите количество элементов списка: ")))]
        cycles = int(input('Введите количество выводов элементов: '))
    for el in cycle(my_list):
        if cycles == 0:
            break
        print(el)
        cycles -= 1
