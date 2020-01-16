def my_func(var_1, var_2):
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        return 'Деление на 0!'
print(my_func(int(input('Введите первое число: ')), int(input('Введите второе число: '))))