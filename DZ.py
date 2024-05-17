from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return  "Удар мечом"

class  Bow(Weapon):
    def attack(self):
        return ", выстрел грянул, стрела кружит"


class Fighter():
    def __init__(self, oruzie):
        self.oruzie = oruzie

    def changeOruzie(self, smena_or):
        self.oruzie = smena_or

    def attack(self):
        return self.oruzie.attack()

class Monster():
    def __init__(self):
        pass


def battle(voin, monster):
    print("Воин выбирает", voin.oruzie.name)
    print("Воин наносит", voin.attack())
    print("Монстр побежден!")

def schet(chisla):
    for i in range(chisla):
        print(i+1)



sword = Sword("Дюрандаль")
bow  = Bow("Гандива")
fighter = Fighter(sword)
monster = Monster()

battle(fighter, monster)

print(f"\n     Считаем до пяти, и монстр воскреснет с уменеем биться против меча ")

schet(5)
print("\n")

fighter.changeOruzie(bow)
battle(fighter, monster)

