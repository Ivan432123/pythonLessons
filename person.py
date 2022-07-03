# ООП, классы

class Person():
    """"Модель человека"""

    def __init__(self, name, age):
        """Инициализация атрибутов человека - имя, возраст"""
        self.name = name
        self.age = age
        print('Человек создан')

    def sing(self):
        """Просим человека спеть"""
        print(self.name + " поёт")

    def dance(self):
        """Просим человека станцевать"""
        print(self.name + " танцует")


man = Person("Иван", 30)
women = Person("Кристина", 28)
# print(man.name)

man.dance()
women.sing()