class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
    def get_full_name(self):
        print(f"Имя: {self.name}, фамилия: {self.surname}, должность: {self.position}")
    def get_total_income(self):
        print(f"Общий доход: {int(self._income.get('wage'))+int(self._income.get('bonus'))}")

person = Position(input('Введите имя: '), input('Введите фамилию: '), input('Введите должность: '), {'wage': input('Введите оклад: '), 'bonus': input('Введите бонус: ')})
person.get_full_name()
person.get_total_income()
