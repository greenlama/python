num = int(input("Введите число: "))
if num < 10:
    print("Наибольшая цифра: ", num)
else:
    max = 1
    while num // 10 != 0:
        if num % 10 > max:
            max = num % 10
        elif num % 10 == 9:
            max = 9
            break
        num = num // 10
        if num // 10 == 0:
            if num > max:
                max = num
    print("Наибольшая цифра: ", max)