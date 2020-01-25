import json

def read_file(file_name):
    with open(file_name, 'r', encoding="utf8") as f_obj:
        content = '1'
        print('Содержимое файла:')
        sr_prib = 0
        prib_dic = {}
        while len(content) != 0:
            content = f_obj.readline().split()
            if len(content) != 0:
                prib = int(content[2])-int(content[3])
                prib_dic.update({content[0]: prib})
                if prib >= 0:
                    sr_prib = sr_prib + prib
            else:
                itog = [prib_dic, dict(average_profit=sr_prib)]
                break
    with open("5.7.json", "w", encoding="utf8") as write_json:
        json.dump(itog, write_json, ensure_ascii=False)

read_file(file_name='5.7.txt')