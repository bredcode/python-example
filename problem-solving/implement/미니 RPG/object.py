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

    def takeDamage(self, target):
        self.hp -= target.atk
        self.hp = max(self.hp, 0)
        print(f"{target.name}에게 {target.atk}의 피해를 입었습니다!")
        self.displayInfo(self.name)

    def attack(self, target):
        target.takeDamage(self)

    def isDead(self):
        return self.hp <= 0