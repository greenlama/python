class Cell:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return f'Результат сложения двух клеток: {self.amount + other.amount}'

    def __sub__(self, other):
        if (self.amount - other.amount) >= 0:
            return f'Результат вычитания двух клеток: {self.amount - other.amount}'
        else:
            return f'Разность количества ячеек двух клеток меньше нуля'

    def __mul__(self, other):
        return f'Результат умножения двух клеток: {self.amount * other.amount}'

    def __truediv__(self, other):
        return f'Результат деления двух клеток: {int(self.amount / other.amount)}'

    def make_order(self, cell_row):
        self.cell_row=cell_row
        self.str = ''
        if self.amount % self.cell_row == 0:
            for i in range(self.amount // self.cell_row):
                for j in range(self.cell_row):
                    self.str = self.str + "*"
                self.str = self.str + '\n'
        else:
            for i in range(self.amount // self.cell_row):
                for j in range(self.cell_row):
                    self.str = self.str + "*"
                self.str = self.str + '\n'
            for i in range(self.amount % self.cell_row):
                self.str = self.str + "*"
            self.str = self.str + '\n'
        return f'Ячейки по рядам:\n{self.str}'


cell1 = Cell(int(input('Введите количество ячеек первой клетки: ')))
cell2 = Cell(int(input('Введите количество ячеек второй клетки: ')))
acts = 0
while acts != 6:
    acts = int(input('\nВыберите действие:\n1 - Сложение клеток\n2 - Вычитание клеток\n3 - Умножение клеток\n4 - Деление клеток\n5 - Организовать ячейки по рядам\n6 - Выход\nВаш выбор: '))
    if acts == 1:
        print(cell1 + cell2)
    elif acts == 2:
        print(cell1 - cell2)
    elif acts == 3:
        print(cell1 * cell2)
    elif acts == 4:
        print(cell1 / cell2)
    elif acts == 5:
        print(cell1.make_order(int(input('Введите количество ячеек в ряду для первой клетки: '))))
        print(cell2.make_order(int(input('Введите количество ячеек в ряду для второй клетки: '))))