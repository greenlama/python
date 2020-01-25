def read_file(file_name):
    with open(file_name, 'r', encoding="utf8") as f_obj:
        content = '1'
        dic = {'One': "Один", 'Two': "Два", 'Three': "Три", 'Four': "Четыре"}
        while len(content) != 0:
            content = f_obj.readline().split()
            if len(content) != 0:
                try:
                    with open('5.4_2.txt', 'a', encoding="utf8") as new_file:
                        new_file.writelines(f"{dic.get(content[0])} {content[1]} {content[2]}\n")
                except IOError:
                    print("Произошла ошибка ввода-вывода!")
            else:
                break

read_file(file_name='5.4_1.txt')
