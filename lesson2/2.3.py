""" Решение через словарь
month_number = input("Введите номер месяца (1-12): ")
while int(month_number) < 1 or int(month_number) > 12:
    month_number = input('Введите корректный номер месяца (1-12): ')
season = {'1': "зима", '2': "зима", '3': 'весна', '4': 'весна', '5': 'весна', '6': 'лето', '7': 'лето', '8': 'лето', '9': 'осень', '10': 'осень', '11': 'осень', '12': 'зима'}
print("Сейчас", season.get(month_number))
"""

# Решение через списки
month_number = input("Введите номер месяца (1-12): ")
while int(month_number) < 1 or int(month_number) > 12:
    month_number = input('Введите корректный номер месяца (1-12): ')
season = ['зима', 'весна', 'лето', 'осень']
months = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
i = 0
while i < 4:
    if int(month_number) in months[i]:
        print("Сейчас", season[i])
        break
    i += 1