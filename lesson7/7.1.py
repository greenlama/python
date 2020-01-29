import random
class Matrix:
    def __init__(self, mx):
        self.mx=mx

    def __add__(self, other):
        result=[]
        for i in range(len(self.mx)):
            sum_str = []
            for j in range(len(self.mx[0])):
                sum_str.append(self.mx[i][j] + other.mx[i][j])
            result.append(sum_str)
        return Matrix(result)

    def __str__(self):
        for el in self.mx:
            for i in el:
                print(f"{i}   ", end='')
            print('\n')
        return f''

def matrix_creation(str, stolb):
    mx = []
    while str != 0:
        j = stolb
        mx_str = []
        while j != 0:
            mx_str.append(random.randint(1, 10))
            j-=1
        mx.append(mx_str)
        str-=1
    return mx


str = int(input('Введите количество строк: '))
stolb = int(input('Введите количество столбцов: '))
matrix1 = Matrix(matrix_creation(str, stolb))
matrix2 = Matrix(matrix_creation(str, stolb))
print(matrix1)
print(matrix2)
print(matrix1+matrix2)