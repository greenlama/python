def my_func(var_1, var_2, var_3):
    """ Возвращает сумму двух наибольших из трех введенных чисел

    Позиционные параметры:
    var_1, var_2, var_3 -- введенные числа

    """
    # Переводим кортеж в список
    args_list = [var_1, var_2, var_3]
    # Убираем из списка наименьшее число
    args_list.remove(min(args_list))
    # Возвращаем сумму оставшихся чисел
    return sum(args_list)
print(my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')),
              int(input('Введите третье число: '))))