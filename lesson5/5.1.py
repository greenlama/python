str = '1'
while True:
    str = input('Введите текст (или нажмите на Enter без текста для выхода): ')
    if str != '':
        with open("5.1.txt", 'a') as f_obj:
            f_obj.write(str+'\n')
    else:
        break