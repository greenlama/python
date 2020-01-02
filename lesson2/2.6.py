goods_base = []
answer = True
i = 1
while answer == True:
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    amount = int(input('Введите количество товара: '))
    ed = input('Введите единицы измерения товара: ')
    goods_base.append((i, dict(название=name, цена=price, количество=amount, eд=ed)))
    i += 1
    choise = input("Введите n для прекращения ввода или любой другой символ для продолжения: ")
    if choise == "n":
        answer = False
print('База товаров:', goods_base)
i = 0
name_li = []
price_li = []
amount_li = []
ei_li = []
while i < len(goods_base):
    goods_tuple = goods_base[i]
    goods_dict = goods_tuple[1]
    name_li.append(goods_dict.get('название'))
    price_li.append(goods_dict.get('цена'))
    amount_li.append(goods_dict.get('количество'))
    if goods_dict.get('eд') not in ei_li:
        ei_li.append(goods_dict.get('eд'))
    i +=1
analiz = {'название': name_li, 'цена': price_li, 'количество': amount_li, 'eд': ei_li}
print('Анализ базы товаров:', analiz)