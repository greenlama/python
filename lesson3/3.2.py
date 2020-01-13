def my_func(name, surname, year, city, email, phone):
    print(
        f'Имя - {name}, Фамилия - {surname}, год рождения - {year}, город проживания - {city}, email - {email}, телефон - {phone}')
print(my_func(name=input('Введите имя: '), surname=input('Введите фамилию: '), year=input('Введите год рождения: '),
              city=input('Введите город проживания: '), email=input('Введите email: '),
              phone=input('Введите телефон: ')))
