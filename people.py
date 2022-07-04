class Person():
    """Создаём человека"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Получаем описание человека"""
        description = self.name + ", ему " + str(self.age) + " года, его рост " + str(self.height) + ", его вес " + str(self.weight)
        print("Нового человека зовут: " + description)

    def get_weight(self):
        """Получение веса человека"""
        print("Вес нашего человека: " + str(self.weight))

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg

class Warrior(Person):
    """Создаём класс воин"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получение заряда ярости"""
        print("Заряд ярости равен: " + str(self.rage))


    def description_person(self):
        """Переопределение метода родителя"""
        description = self.name + ", ему " + str(self.age) + " года, его рост " + str(self.height) + ", его заряд ярости " + str(self.rage)
        # print("Нового человека зовут: " + description)
        return description

warrior = Warrior("Конан", 32, 200)
# warrior.get_rage()
# warrior.update_weight(200)
# warrior.description_person()
print("Нового человека зовут: " + warrior.description_person())


man = Person("Иван", 32, 178)
# man.get_rage
# man.description_person()
# # man.weight = 110
# man.update_weight(130)
# man.get_weight()