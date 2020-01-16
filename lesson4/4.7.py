from math import factorial
def fact(n):
    my_list = range(1, n+1)
    for i in my_list:
        yield factorial(i)
n = 0
while n < 1:
    n = int(input('Введите число: '))
for el in fact(n):
    print(el)