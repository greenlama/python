def my_func(var_1, var_2):
    """ Возведение в отрицательную степень

    Позиционные параметры:
    var_1 -- число, возводимое в степень
    var_2 -- отрицательная степень

    """
    choice=input("Решение через ** - введите '1'. Решение через цикл - введите '2'. Введите выбранный способ решения: ")
    if choice == '1':
        # Решение через **
        return var_1 ** var_2
    elif choice == '2':
        #Решение через цикл
        delitel = 1
        while var_2 != 0:
            delitel = delitel * var_1
            var_2 += 1
        return 1 / delitel
    else:
        print('Вы выбрали несуществующий способ решения!')
print(my_func(int(input('Введите первое число (действительное положительное): ')), int(input('Введите второе число (целое отрицательное): '))))