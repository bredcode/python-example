class Object():
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    
    def displayInfo(self, objType):
        print(f"[{objType} 정보]")
        print(f"이름: {self.name}")
        print(f"체력: {self.hp}")
        print(f"공격력: {self.atk}")

    def attack(self):
        return self.atk

    def takeDamage(self, atk):
        self.hp -= atk
        return

    def isDead(self):
        return self.hp <= 0