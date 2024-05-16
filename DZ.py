# Шаг 3: Модифицируйте класс Fighter
#  • Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
#  • Добавьте метод changeWeapon(), который позволяет изменить оружие бойца.
class Fighter():
    def __init__(self, oruzie):
        self.oruzie = oruzie

    def changeOruzie(self):
        change 

class Monster():
    pass


from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return  "Удар мечом"

class  Bow(Weapon):
    def attack(self):
        return "Выстрел грянул, стрела кружит"








