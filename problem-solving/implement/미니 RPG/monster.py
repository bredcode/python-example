from object import Object
import random

names = ["슬라임", "오크", "좀비", "고블린"]

class Monster(Object):
    def __init__(self):
        name = random.choice(names)
        hp = random.randint(10, 20)
        atk = random.randint(1, 5)
        super().__init__(name, hp, atk)
    
    def displayInfo(self, objType = None):
        super().displayInfo("몬스터")

    def attack(self):
        return self.atk

    def takeDamage(self, obj):
        self.hp -= obj.attack()
        print(f"{obj.name}에게 {obj.atk}의 피해를 입었습니다!")
        self.displayInfo()
        return