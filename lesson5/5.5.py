from random import randint

def create_file(count):
    my_str = ''
    while count != 0:
        my_str = my_str + ' ' + str(randint(1, 50))
        count -= 1
    try:
        with open('5.5.txt', 'w', encoding="utf8") as new_file:
            new_file.write(my_str)
    except IOError:
        print("Произошла ошибка ввода-вывода!")

def count_sum():
    with open('5.5.txt', 'r', encoding="utf8") as my_file:
        print('Содержимое файла:', my_file.readline())
        my_file.seek(0)
        li = my_file.readline().split()
        my_sum = 0
        for el in li:
            my_sum = my_sum + int(el)
        print('Сумма чисел в файле:', my_sum)

create_file(randint(1, 20))
count_sum()