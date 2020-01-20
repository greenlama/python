from random import randint
old_list = [randint(1, 99) for i in range(int(input("Введите количество элементов изначального списка: ")))]
print('Исходный список: ', old_list)
new_list = [old_list[i] for i in range(1, len(old_list)) if old_list[i] > old_list[i-1]]
print('Результат: ', new_list)