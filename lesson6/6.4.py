import random

class Car:
    def __init__(self, speed, color, name, is_polis=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polis = is_polis
        if self.is_polis:
            print(f"\nМашина: {self.name}\nЦвет: {self.color}\nПолицейская: да\n")
        else:
            print(f"\nМашина: {self.name}\nЦвет: {self.color}\nПолицейская: нет\n")
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        print('Машина повернула', direction)
    def show_speed(self):
        print(f'Скорость: {self.speed * 10} км/ч')
class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    def show_speed(self):
        if self.speed*10 > 60:
            print(f'Скорость {self.speed*10} км/ч. Внимание! Превышение скорости!')
        else:
            print(f'Скорость: {self.speed * 10} км/ч')
class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    def show_speed(self):
        if self.speed * 10 > 40:
            print(f'Скорость {self.speed * 10} км/ч. Внимание! Превышение скорости!')
        else:
            print(f'Скорость: {self.speed * 10} км/ч')
class PolisCar(Car):
    def __init__(self, speed, color, name, is_polis):
        super().__init__(speed, color, name, is_polis)

def actions(act):
    acts = 0
    while acts != 5:
        acts = int(input('\nВыберите действие:\n1 - Показать скорость\n2 - Двигаться\n3 - Остановиться\n4 - Повернуть\n5 - Выход\nВаш выбор: '))
        if acts == 2:
            act.go()
        elif acts == 1:
            act.show_speed()
        elif acts == 3:
            act.stop()
        elif acts == 4:
            dirct = int(input('Куда поворачиваем?\n1 - Налево\n2 - Направо\nВаш выбор: '))
            if dirct == 1:
                direction = 'налево'
            elif dirct == 2:
                direction = 'направо'
            act.turn(direction)


car_names = ['Audi', 'BMW', 'Mercedes', 'Volkswagen', 'Toyota', 'Mitsubishi', 'Lada']
car_colors = ['белый', 'красный', 'черный', 'серебристый', 'синий', 'желтый']
choice=0
while choice != 5:
    choice=int(input('Выберите тип машины:\n1 - TownCar\n2 - SportCar\n3 - WorkCar\n4 - PoliceCar\n5 - Выход\nВаш выбор: '))
    if choice == 1:
        car_town = TownCar(random.randint(1, 12), random.choice(car_colors), random.choice(car_names))
        actions(car_town)
    elif choice == 2:
        car_sport = SportCar(random.randint(1, 12), random.choice(car_colors), random.choice(car_names))
        actions(car_sport)
    elif choice == 3:
        car_work = WorkCar(random.randint(1, 12), random.choice(car_colors), random.choice(car_names))
        actions(car_work)
    elif choice == 4:
        car_polis = PolisCar(random.randint(1, 12), random.choice(car_colors), random.choice(car_names), True)
        actions(car_polis)
    elif choice == 5:
        break
