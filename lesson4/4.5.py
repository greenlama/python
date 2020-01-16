from functools import reduce
def my_func(pr1, pr2):
    return pr1 * pr2
print('Очень длинный результат произведения четных чисел от 100 по 1000: ', reduce(my_func, [i for i in range(100, 1001) if i % 2 == 0]))