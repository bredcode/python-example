from object import Object

class Player(Object):
    def __init__(self, name, hp = 100, atk = 10):
        super().__init__(name, hp, atk)

    def displayInfo(self, objType = None):
        super().displayInfo("플레이어")
