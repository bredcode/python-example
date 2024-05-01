from object import Object

class Player(Object):
    def __init__(self, name):
        super().__init__(name, 100, 10)

    def displayInfo(self, type = None):
        super().displayInfo("플레이어")

    def attack(self):
        return self.damage

    def takeDamage(self, obj):
        self.hp -= obj.attack()
        print(f"{obj.name}에게 {obj.damage}의 피해를 입었습니다!")
        self.displayInfo()
        return
