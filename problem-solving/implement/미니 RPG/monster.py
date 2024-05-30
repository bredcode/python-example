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

    def dropMoney(self):
        return random.randint(10, 100)