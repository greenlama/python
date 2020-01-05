my_list = [7, 5, 3, 3, 2]
new_el = int(input("Введите новый элемент рейтинга (целое положительное число): "))
print('Старый рейтинг:', my_list)
my_list.reverse()  # Сделаем реверс списка для вставки элемента с имеющимся значением
i = 0
while i < len(my_list):
    if new_el <= my_list[i]:  # Если новый элемент <= текущему, вставляем на место, смещяя список вправо
        my_list.insert(i, new_el)
        break
    elif i == len(my_list) - 1:  # Если список прошли, а новый элемент больше любого имеющегося, добавляем его в конец
        my_list.append(new_el)
        break
    i += 1
my_list.reverse()
print('Новый рейтинг:', my_list)