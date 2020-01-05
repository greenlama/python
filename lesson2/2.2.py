li = []
answer = True
while answer == True:
    el = input("Введите элемент списка: ")
    li.append(el)
    choise = input("Введите n для прекращения ввода или любой другой символ для продолжения: ")
    if choise == "n":
        answer = False
print("Изначальный список: ", li)
i = 0
if len(li) // 2 == 1:  # для списков длиной 2-3 элемента
    li[0], li[1] = li[1], li[0]
elif len(li) // 2 >= 2:
    while i < (len(li) // 2) * 2:
        li[i], li[i + 1] = li[i + 1], li[i]
        i += 2
print("Окончательный список: ", li)