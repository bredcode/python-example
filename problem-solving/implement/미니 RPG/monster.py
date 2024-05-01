from object import Object
import random

names = ["슬라임", "오크", "좀비", "고블린"]

class Monster(Object):
    def __init__(self):
        name = random.choice(names)
        hp = random.randint(10, 20)
        damage = random.randint(1, 5)
        super().__init__(name, hp, damage)
    
    def displayInfo(self, type = None):
        super().displayInfo("몬스터")

    def attack(self):
        return self.damage

    def takeDamage(self, obj):
        self.hp -= obj.attack()
        print(f"{obj.name}에게 {obj.damage}의 피해를 입었습니다!")
        self.displayInfo()
        return