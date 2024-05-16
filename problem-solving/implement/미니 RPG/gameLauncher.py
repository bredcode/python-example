from player import Player
from monster import Monster
from cipher import Cipher
import time

MODE_DEV = "DEV"
MODE_NORMAL = "NORMAL"
GAME_MODE = MODE_NORMAL

def sleep(second):
    if GAME_MODE == MODE_DEV:
        time.sleep(0)
    else:
        time.sleep(second)

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
        if not self.player:
            name = input("캐릭터 이름을 입력해주세요 : ")
            self.player = Player(name, GAME_MODE)

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
                    print("몬스터가 나타났다!")
                    monster = Monster()
                    monster.displayInfo()
                    sleep(3)
                    while True:
                        print("플레이어의 공격 차례입니다.")
                        sleep(1)
                        self.player.attack(monster)
                        if monster.isDead():
                            print("몬스터가 죽었습니다!")
                            break
                        sleep(2)
                        print("몬스터의 공격 차례입니다.")
                        sleep(1)
                        monster.attack(self.player)
                        if self.player.isDead():
                            print("플레이어가 죽었습니다!")
                            print("GAME OVER")
                            self.exit()
                            break
                        sleep(2)
                case "2":
                    self.save()
                case "3":
                    self.exit()
                case _: # default
                    continue
        return

    def save(self):
        playerData = {
            "name": self.player.name,
            "hp": self.player.hp,
            "atk": self.player.atk 
        }
        password = input("암호를 입력해주세요: ")
        saveData = Cipher().encrypt(playerData, password)
        with open('saveData.json', 'w') as file:
            file.write(saveData)
        return

    def load(self):
        password = input("암호를 입력해주세요: ")
        try:
            with open('saveData.json', 'r') as file:
                saveData = file.read()
                playerData = Cipher().decrypt(saveData, password)
                self.player = Player(playerData["name"], playerData["hp"], playerData["atk"])
                self.play()
        except FileNotFoundError:
            print("[ERROR] 저장된 파일이 없습니다.")
        except Exception:
            print("[ERROR] 암호가 틀렸습니다.")
        return

    def exit(self):
        exit(0)


def main():
    gameLauncher = GameLauncher()
    gameLauncher.run()

if __name__ == "__main__":
    main()