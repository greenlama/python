with open("5.2.txt", 'r') as f_obj:
    li = f_obj.readlines()
    print('Количество строк:', len(li))
    for ind, el in enumerate(li, 1):
        print('В строке', ind, '-', el.count(' ')+1, 'слов(a).')