stroka = input("Введите строку из нескольких слов: ")
li = stroka.split()
for ind, el in enumerate(li, 1):
    if len(el) <= 10:
        print(ind, el)
    else:
        print(ind, el[0:10])