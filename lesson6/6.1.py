import time
class TrafficLight:
    __color = 'Красный'
    def running(self):
        i=3*int(input('Введите количество циклов: '))
        while i != 0:
             if TrafficLight._TrafficLight__color == 'Красный':
                 print(f"\033[31m{TrafficLight._TrafficLight__color}")
                 time.sleep(7)
                 TrafficLight._TrafficLight__color = 'Желтый'
             elif TrafficLight._TrafficLight__color == 'Желтый':
                 print(f"\033[33m{TrafficLight._TrafficLight__color}")
                 time.sleep(2)
                 TrafficLight._TrafficLight__color = 'Зеленый'
             elif TrafficLight._TrafficLight__color == 'Зеленый':
                 print(f"\033[32m{TrafficLight._TrafficLight__color}")
                 time.sleep(7)
                 TrafficLight._TrafficLight__color = 'Красный'
             i -= 1
light = TrafficLight()
light.running()