def my_func(*args):
    """ Суммирует введенные через пробел числа

    Позиционный параметр:
    args -- введенные через пробел числа

    """
    # Преобразуем разбитый по разделителю-пробелу кортеж в строку
    str = args[0].split()
    global sum, exit
    # Суммируем элементы строки, преобразовав их в int
    for el in str:
        try:
            sum += int(el)
        # Обработка исключения преобразования в int не числового символа
        except ValueError:
            exit = False
            break
    if exit:
        print('Cумма введенных чисел:', sum)
    else:
        print('Итоговая сумма введенных чисел:', sum)


exit = True
sum = 0
while exit:
    my_func(input('Введите строку чисел, разделенных пробелами: '))
