class Stationery:
    def __init__(self, name):
        self.title = name

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print(f'\n{self.title} рисует ручкой.\n')

class Pencil(Stationery):
    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print(f'\n{self.title} рисует карандашом.\n')

class Handle(Stationery):
    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print(f'\n{self.title} рисует маркером.\n')

choice=0
name=input('Введите ваше имя: ')
while choice != 4:
    choice= int(input('Чем будем рисовать?\n1 - Ручкой\n2 - Карандашом\n3 - Маркером\n4 - Выход\nВаш выбор: '))
    if choice==1:
        dr_pen=Pen(name)
        dr_pen.draw()
    elif choice==2:
        dr_pencil = Pencil(name)
        dr_pencil.draw()
    elif choice==3:
        dr_handle = Handle(name)
        dr_handle.draw()