from object import Object

class Player(Object):
    def __init__(self, name):
        super().__init__(name, 100, 10)

    def displayInfo(self, objType = None):
        super().displayInfo("플레이어")
