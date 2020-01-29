from abc import ABC, abstractmethod

class Cloth(ABC):
    def __init__(self, V, H):
        self.v = V
        self.h = H

    @abstractmethod
    def coat_count(self):
        pass

    @abstractmethod
    def suit_count(self):
        pass

    @property
    def decor(self):
        return f"Общий расход ткани: {(round(self.v / 6.5, 2) + 0.5) + (2 * self.h + 0.3)}"

class Count(Cloth):
    def coat_count(self):
        print(f"Расход ткани на пальто: {round(self.v / 6.5, 2) + 0.5}")

    def suit_count(self):
        print(f"Расход ткани на костюм: {2 * self.h + 0.3}")


V = int(input('Введите размер: '))
H = int(input('Введите рост: '))
cnt = Count(V, H)
cnt.coat_count()
cnt.suit_count()
print(cnt.decor)