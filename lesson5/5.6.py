def read_file(file_name):
    with open(file_name, 'r', encoding="utf8") as f_obj:
        content = '1'
        dic = {}
        print('Содержимое файла:')
        while len(content) != 0:
            content = f_obj.readline().split()
            num = 0
            if len(content) != 0:
                print(content)
                for el in content:
                    try:
                        num = num + int(el[0:el.index('(')])
                    except:
                        continue
            else:
                break
            dic.update({content[0]: num})
    print('Результат:\n', dic)

read_file(file_name='5.6.txt')
