## 미니 RPG 구현하기

python을 배우고 나서 간단한 프로젝트를 해보기 위해 미니 RPG 게임을 만들어보고자 한다.

프로젝트는 간단하게 플레이어와 몬스터를 만들고, 턴제 방식으로 서로 공격하는 과정을 거치도록 하는 게임이다.

이때 플레이어의 체력이 0 이하가 되면 게임이 끝나도록 한다.

구체적인 기능들은 아래 내용을 참고하여 조건에 맞게 프로젝트를 구현해보자.

### 구현 단계

1. 게임을 시작하기 위해 `GameLauncher` 라는 클래스를 생성하고자 한다.

- gameLauncher.py 파일을 생성
- 아래와 같이 gameLauncher.py를 작성

  ```python
  class GameLauncher():
      # code 구현

  def main():
      # code 구현

  if __name__ == "__main__":
      main()
  ```

2. GameLauncher 클래스 내 displayLauncher 함수를 작성한다.

- displayLauncher 함수는 다음과 같은 형태의 출력이 되도록 한다.

```text
===== 미니 RPG =====
=    1. 새 게임    =
=    2. 불러오기   =
=    3. 게임종료   =
====================
```

3. GameLauncher 클래스 내 run이라는 함수를 작성하여 게임을 실행할 수 있는 기반을 만든다.

- run 함수는 다음과 같은 형태로 작성한다.
- 앞서 작성한 displayLauncher() 함수를 호출한다.
- `원하는 번호를 입력해주세요 : `라는 안내와 함께 select라는 변수에 값을 받는다.
- "1"이면 play "2"면 load "3"이면 exit 함수를 호출고 그 외의 값인 경우 (case가 \_ 인 경우가 그 외의 값을 의미) 무시하도록 한다.
- 이때, play, load, exit는 GameLauncher 내 함수로 만들고 아무 로직 없이 return만 해두도록 한다.
- python에는 switch / case문이 아닌 match / case문이 존재한다. 위 조건을 처리할 때, 이를 활용해보자.
- 그 후 위 로직은 `3. 게임종료` 가 호출되기전까지 무한 반복된다.

4. 간단한 exit 함수부터 구현한다.

- python 프로그램을 runtime에서 어떻게 코드로 종료할 수 있는지 검색하여 작성해보자.

5. 이제 main 함수에서 GameLauncher을 생성하여 run함수를 실행하여 여러 버튼을 누르고 마지막으로 3번을 누르면 종료가 되는지 해보자.

6. play 함수를 구현하기 전, player와 monster 객체를 구현하고자 한다.

   (아래 내용 진행 전, object.py, player.py, monster.py 생성)

- player, monster는 이름(name), 체력(hp), 공격력(atk) 라는 변수를 가진 object 라는 클래스를 상속받는다.

- object 클래스는 다음과 같은 함수를 가지고 있고, 아래 조건에 맞게 작성해보자.

```python
class Object():
    def __init__(self, name, hp, atk):
      # 멤버변수로 name, hp, atk를 생성하고 각 인자 값을 대입

    def displayInfo(self, objType):
      # 다음과 같은 형태를 출력
      [{objType} 정보]
      이름: {이름}
      체력: {현재 체력}
      공격력: {현재 공격력}

    def attack(self):
      # 현재 공격력(atk)를 리턴

    def takeDamage(self, atk):
      # 현재 체력에서 상대에게 받은 공격력(atk)을 차감

    def isDead(self):
      # 체력이 0 이하면 true, 그게 아니면 false
```

6. Player 클래스를 구현하고자 한다.

- Player 클래스는 Object를 상속받는다.
- player은 생성자에서 name 인자만 받고, 부모 클래스의 생성자에게 이름 name, 체력 100, 공격력 10 의 파라미터를 전달해준다.

- displayInfo 함수를 생성한다. 이때 부모 클래스에서 objType를 처리하기에 Player 클래스에서는 objType을 기본값으로 None을 받도록 하고 부모 함수를 호출하여 "플레이어"라는 파라미터를 보내도록 한다.
  - 힌트: 부모의 displayInfo("플레이어")
- attack라는 함수는 자기 자신의 atk를 리턴하도록 한다.

7. takeDamage 함수를 구현한다.

- takeDamage 인자는 obj를 받는다.
- 내부 로직은 상대방(obj)의 공격력 만큼 플레이어 체력을 차감한다.
- 그리고 `{상대방 이름}에게 {상대방 공격력}의 피해를 입었습니다!`를 출력한다.
- 마지막으로 displayInfo 함수를 호출하여 플레이어 정보를 보여준다.

8. Monster 클래스를 구현하고자 한다.

- monster.py의 전역변수로 names라는 리스트를 생성하고 `"슬라임", "오크", "좀비", "고블린"`의 값이 들어가도록 해준다.

- Monster 클래스는 Object를 상속받는다.
- monster 생성자는 다음과 같다.

  - 이름 name은 random 모듈을 import하여 random 모듈 내의 choice 함수를 이용하여 names 중 하나를 선택하여 대입해준다.
  - 체력 hp는 random 모듈의 randint를 이용하여 `10 ~ 20` 사이 값이 구성되게 해준다.
  - 공격력 atk는 random 모듈의 randint를 이용하여 `1 ~ 5` 사이 값이 구성되개 해준다.
  - 위 값들을 부모 클래스의 생성자에게 전달해주어 Monster 객체를 생성한다.

- displayInfo 함수를 생성한다. 이때 부모 클래스에서 objType를 처리하기에 Monster 클래스에서는 objType을 기본값으로 None을 받도록 하고 부모 함수를 호출하여 "몬스터"라는 파라미터를 보내도록 한다.

  - 힌트: 부모의 displayInfo("몬스터")

- attack라는 함수는 자기 자신의 atk를 리턴하도록 한다.

9. takeDamage 함수를 구현한다.

- takeDamage 인자는 obj를 받는다.
- 내부 로직은 상대방(obj)의 공격력 만큼 몬스터 체력을 차감한다.
- 그리고 `{상대방 이름}에게 {상대방 공격력}의 피해를 입었습니다!`를 출력한다.
- 마지막으로 displayInfo 함수를 호출하여 몬스터 정보를 보여준다.

10. gameLauncher의 play 함수 구현하기

- play 함수는 게임이 실행되는 부분이다.
- 첫번째로 GameLauncher의 멤버변수로 player을 None으로 생성해준다.
- 그다음 `캐릭터 이름을 입력해주세요 : `라는 안내와 함께 name 변수에 값을 받은 뒤 Player에 name 파라미터를 전달하여 객체를 생성해준다.

- 그 후 아래와 같은 로직의 순서를 구현한다. 이때 아래 로직은 `3. 게임종료` 가 호출되기전까지 무한 반복된다.

  - player의 displayInfo를 호출한다.
  - 다음과 같은 형태를 출력해준다.

  ```text
  ===================
  =    1. 사냥하기   =
  =    2. 저장하기   =
  =    3. 게임종료   =
  ====================
  ```

  - 그다음 `원하는 번호를 입력해주세요 : ` 라는 안내와 함께 select 변수에 값을 받는다.

  - select의 값이 "1"인 경우
    - `몬스터가 나타났다!` 를 출력 한 후, monster를 생성하고, monster의 정보를 출력한다.
    - `플레이어의 공격 차례 입니다.` 를 출력 한 후, monster에게 피해를 입힌다.
    - 만약 몬스터가 죽었다면(hp가 0이하라면) `몬스터가 죽었습니다!`를 출력한다.
    - 몬스터가 죽지 않았다면 `몬스터의 공격 차례입니다.`를 출력 한 후, player에게 피해를 입힌다.
    - 만약 플레이어가 죽었다면(hp가 0이하라면) `플레이어가 죽었습니다!`를 출력하고 `GAME OVER`을 출력하며 게임을 종료한다.
    - 둘중 하나가 죽을때까지 계속해서 반복진행되도록 만든다.
  - select의 값이 "2"인 경우
    - GameLauncher의 save 함수를 호출한다.
  - select의 값이 "3"인 경우
    - GameLauncher의 exit 함수를 호출한다.
  - 그 외의 값인 경우 (case가 \_ 인 경우가 그 외의 값을 의미)
    - 무시하도록 한다.
