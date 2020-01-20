with open("5.3.txt", 'r', encoding="utf8") as f_obj:
    li = f_obj.readlines()
    li = [line.rstrip() for line in li]
    print('Сотрудники, получающие менее 20000:')
    zp = 0
    for str in li:
        str_li = str.split()
        if float(str_li[1]) < float(20000):
            print(str)
        zp = zp + float(str_li[1])
    print(f'Средняя зарплата составляет {zp / len(li):.2f}')