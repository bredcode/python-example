class Object():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def displayInfo(self, objType):
        print(f"[{objType} 정보]")
        print(f"이름: {self.name}")
        print(f"체력: {self.hp}")
        print(f"공격력: {self.damage}")

    def attack(self):
        return self.damage

    def takeDamage(self, damage):
        self.hp -= damage
        return

    def isDead(self):
        return self.hp <= 0