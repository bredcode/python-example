from player import Player
from monster import Monster
import time

class GameLauncher():
    def __init__(self):
        self.player = None
        return
    def run(self):
        while True:
            self.displayLauncher()
            select = input("원하는 번호를 입력해주세요 : ")
            match(select):
                case "1":
                    self.play()
                case "2":
                    self.load()
                case "3":
                    self.exit()
                case _: # default
                    continue

    def displayLauncher(self):
        print("===== 미니 RPG =====")
        print("=    1. 새 게임    =")
        print("=    2. 불러오기   =")
        print("=    3. 게임종료   =")
        print("====================")

    def play(self):
        name = input("캐릭터 이름을 입력해주세요 : ")
        self.player = Player(name)

        while True:
            self.player.displayInfo()
            print("===================")
            print("=    1. 사냥하기   =")
            print("=    2. 저장하기   =")
            print("=    3. 게임종료   =")
            print("====================")

            select = input("원하는 번호를 입력해주세요 : ")
            match(select):
                case "1":
                    monster = Monster()
                    print("몬스터가 나타났다!")
                    monster.displayInfo()
                    # time.sleep(3)
                    while True:
                        print("플레이어의 공격 차례입니다.")
                        # time.sleep(2)
                        self.player.attack(monster)
                        if monster.isDead():
                            print("몬스터가 죽었습니다!")
                            break
                        print("몬스터의 공격 차례입니다.")
                        # time.sleep(2)
                        monster.attack(self.player)
                        if self.player.isDead():
                            print("플레이어가 죽었습니다!")
                            print("GAME OVER")
                            self.exit()
                            break
                case "2":
                    self.save()
                case "3":
                    self.exit()
                case _: # default
                    continue
        return
    def save(self):

        return
    def load(self):

        return
    def exit(self):
        exit(0)


def main():
    gameLauncher = GameLauncher()
    gameLauncher.run()

if __name__ == "__main__":
    main()