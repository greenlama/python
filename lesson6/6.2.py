class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def total_mass(self):
        print('Общая масса асфальта: ', int(mass._length * mass._width * 25 * 5 / 1000), 'тонн')

mass = Road(int(input('Введите длину покрытия: ')), int(input('Введите ширину покрытия: ')))
mass.total_mass()