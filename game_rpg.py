print("== ANALISIS 1 ==")

class HeroA1:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

hero1 = HeroA1("Layla", 100, 15)
hero1.hp = 500  
print(hero1.hp)

print("== ANALISIS 2 ==")

class HeroA2:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.hp -= self.attack_power
        print(f"HP {lawan.name}: {lawan.hp}")

hero1 = HeroA2("Layla", 100, 15)
hero2 = HeroA2("Zilong", 120, 20)
hero1.serang(hero2)

      
print("== ANALISIS 3 ==")

class HeroA3:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class MageA3(HeroA3):
    def __init__(self, name, hp, mana):
        # super().__init__(name, hp)  
        self.mana = mana

    def info(self):
        print(self.name)

try:
    eudora = MageA3("Eudora", 80, 100)
    eudora.info()
except Exception as e:
    print("ERROR:", e)

print("== ANALISIS 4 ==")

class HeroA4:
    def __init__(self, name, hp):
        self.name = name
        self.__hp = hp

hero1 = HeroA4("Layla", 100)

print("Akses paksa HP:", hero1._HeroA4__hp)


print("== ANALISIS 5 ==")

from abc import ABC, abstractmethod

class GameUnit(ABC):
    @abstractmethod
    def serang(self):
        pass

class HeroA5(GameUnit):
    pass  # tidak mengimplementasikan serang()

try:
    hero = HeroA5()
except Exception as e:
    print("ERROR:", e)


print("== ANALISIS 6 ==")

class HeroA6:
    def __init__(self, name):
        self.name = name

    def serang(self):
        print("Hero menyerang")

class MageA6(HeroA6):
    def serang(self):
        print(f"{self.name} (Mage) melempar bola api")

class ArcherA6(HeroA6):
    def serang(self):
        print(f"{self.name} (Archer) menembak panah")

class HealerA6(HeroA6):
    def serang(self):
        print(f"{self.name} menyembuhkan teman")

pasukan = [
    MageA6("Eudora"),
    ArcherA6("Miya"),
    HealerA6("Estes")
]

for pahlawan in pasukan:
    pahlawan.serang()
