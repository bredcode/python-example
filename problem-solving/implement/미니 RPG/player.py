from object import Object

class Player(Object):
    def __init__(self, mode, name, hp = 100, atk = 10):
        self.money = 0
        if mode == "DEV":
            super().__init__(name, 20, 5)
        else:
            super().__init__(name, hp, atk)


    def displayInfo(self, objType = None):
        super().displayInfo("플레이어")

    def getMoney(self, money):
        self.money += money