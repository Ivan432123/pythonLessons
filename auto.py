class Auto():
    """Модель авто"""

    def __init__(self, model, year):
        """Инициализация атрибутов авто"""
        self.model = model
        self.year = year
        # print("Автомобиль куплен")

    def good(self):
        """Отличное состояние авто """
        print(self.model + " в отличном состоянии")

    def avg(self):
        """Среднее состояние авто """
        print(self.model + " в среднем состоянии")

    def bad(self):
        """Плохое состояние авто """
        print(self.model + " в плохом состоянии")

auto = Auto("Honda", 1997)
auto_1 = Auto("Mazda", 1999)
auto_2 = Auto("Merzedes-Benz", 2003)
auto_3 = Auto("Audi", 2000)
# print(auto.model)

auto.good()
auto_1.bad()
auto_2.good()
auto_3.avg()