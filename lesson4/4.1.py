'''Запуск через командную строку с параметрами: python 4.1.py выработка_в_час ставка_в_час премия'''
from sys import argv
script, vir_in_hour, stavka_in_hour, premia = argv
def zp_count(vir_in_hour, stavka_in_hour, premia):
    zp = int(vir_in_hour) * int(stavka_in_hour) + int(premia)
    return zp
print('Сотрудник заработал', zp_count(vir_in_hour, stavka_in_hour, premia))