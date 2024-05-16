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

4. save와 load 함수는 정의만 해둔 채, 우선은 로직 없이 return해둔다.

5. 간단한 exit 함수부터 구현한다.

- python 프로그램을 runtime에서 어떻게 코드로 종료할 수 있는지 검색하여 작성해보자.

6. 이제 main 함수에서 GameLauncher을 생성하여 run함수를 실행하여 여러 버튼을 누르고 마지막으로 3번을 누르면 종료가 되는지 해보자.

7. play 함수를 구현하기 전, player와 monster 객체를 구현하고자 한다.

   (아래 내용 진행 전, object.py, player.py, monster.py 생성)

- player, monster는 이름(name), 체력(hp), 공격력(atk) 라는 멤버 변수를 가진 object 라는 클래스를 상속받는다.

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

    def takeDamage(self, target):
      # 현재 체력에서 상대(target)에게 받은 공격력(atk)을 차감
      # {target의 name}에게 {target의 atk}의 피해를 입었습니다! 출력
      # displayInfo 출력

    def attack(self, target):
      # 타겟에게 피해를 입힘 (takeDamage 사용)

    def isDead(self):
      # 체력이 0 이하면 true, 그게 아니면 false
```

8. Player 클래스를 구현하고자 한다.

- Player 클래스는 Object를 상속받는다.
- player은 생성자에서 name 인자만 받고, 부모 클래스의 생성자에게 이름 name, 체력 100, 공격력 10 의 파라미터를 전달해준다.

  - 이때 Player에서 값들을 할당하지 않고 반드시 부모 클래스의 생성자를 호출한다.

- displayInfo 함수를 생성한다. 이때 부모 클래스에서 objType를 처리하기에 Player 클래스에서는 objType을 기본값으로 None을 받도록 하고 부모 함수의 displayInfo를 호출하여 "플레이어"라는 파라미터를 보내도록 한다.
  - 힌트: 부모의 displayInfo("플레이어")

9. Monster 클래스를 구현하고자 한다.

- monster.py의 전역변수로 names라는 리스트를 생성하고 `"슬라임", "오크", "좀비", "고블린"`의 값이 들어가도록 해준다.

- Monster 클래스는 Object를 상속받는다.
- monster 생성자는 다음과 같다.

  - 이름 name은 random 모듈을 import하여 random 모듈 내의 choice 함수를 이용하여 names 중 하나를 선택하여 대입해준다.
  - 체력 hp는 random 모듈의 randint를 이용하여 `10 ~ 20` 사이 값이 구성되게 해준다.
  - 공격력 atk는 random 모듈의 randint를 이용하여 `1 ~ 5` 사이 값이 구성되개 해준다.
  - 위 값들을 부모 클래스의 생성자에게 전달해주어 Monster 객체를 생성한다.

    - 이때 Player에서 값들을 할당하지 않고 반드시 부모 클래스의 생성자를 호출한다.

  - displayInfo 함수를 생성한다. 이때 부모 클래스에서 objType를 처리하기에 Monster 클래스에서는 objType을 기본값으로 None을 받도록 하고 부모 함수의 displayInfo를 호출하여 "몬스터"라는 파라미터를 보내도록 한다.

    - 힌트: 부모의 displayInfo("몬스터")

10. gameLauncher의 play 함수 구현하기

- play 함수는 게임이 실행되는 부분이다.
- 첫번째로 GameLauncher의 멤버변수로 player을 None으로 생성해준다.
- 만약 player를 아직 생성하지 않은 경우 `캐릭터 이름을 입력해주세요 : `라는 안내와 함께 name 변수에 값을 받은 뒤 Player에 name 파라미터를 전달하여 객체를 생성해준다.

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

- 리팩토링 되어야할 사항
  - Player와 Monster의 체력이 음수 출력이 될 수 있다. 체력이 음수가 되는 경우 0을 출력하게 해주자.

11. save 함수 구현하기

- 플레이어의 상태를 저장하는 부분
- 현재 가지고 있는 name, hp, atk를 저장하고자 한다.
- 다음 순서에 따라 save 함수를 구현해본다.
  - name, hp, atk를 하나의 dict 변수에 저장한다.
  - json 모듈의 json.dumps를 이용하여 dict를 str 형태로 변환해준다.
  - 변환된 str 데이터를 `saveData.json`에 저장한다.

12. load 함수 구현하기

- 플레이어의 상태를 불러오는 부분
- 저장된 플레이어의 정보를 가져오고자 한다.
- 다음 순서에 따라 load 함수를 구현해본다.

  - `saveData.json` 파일을 열어 파일 내 데이터를 읽고 변수에 저장한다.
  - json 모듈의 json.loads를 이용하여 해당 str 형태의 데이터를 dict 형태로 변환해준다.
  - Player 클래스를 생성하며 해당 불러온 파일의 name, hp, atk를 생성자에 넣어준다.
  - play를 통해 게임을 진행시킨다.

- 주의사항: `saveData.json`이 없는 경우 데이터를 불러오면 에러가 발생한다. 이때 파일이 없는 경우 `[ERROR] 저장된 파일이 없습니다.`라는 에러를 출력하도록 하자 (hint: except FileNotFoundError)

- 리팩토링 되어야할 사항
  - Player가 현재 name만 받도록 되어있다. 위 내용을 만족시킬 수 있도록 변경해보자.
  - play를 하면 항상 플레이어를 새로 생성하고 게임을 진행한다. 불러온 경우에는 새로 생성하지 않도록 해보자

13. 해킹하기

- 플레이어의 정보를 해킹해보고자 한다.
- 체력을 1000, 공격력을 100으로 조작하여 데이터를 해킹해본다.

14. 정보보안 강화하기

- 아래와 같은 cipher.py 파일을 생성하고, 예제를 통해 어떻게 사용하는지 확인해본다.
- 아래 모듈은 dict를 암호화 시켜 파일의 조작을 막을 수 있고, 암호를 알아야만 복호화 할 수 있도록 설계되어있다.
- 아래 파일을 실행하기 위해서는 `pip install cryptography`을 통해 사전에 모듈을 설치하여야 한다.

  ```python
  # pip install cryptography
  from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
  from cryptography.hazmat.primitives.ciphers.aead import AESGCM
  import os
  import base64
  import json

  class Cipher():
    # 키 생성 함수
    def generate_key(self, password, salt):
        kdf = Scrypt(
            salt=salt,
            length=32,
            n=2**14,
            r=8,
            p=1,
        )
        key = kdf.derive(password.encode())
        return key

    # 암호화 함수
    def encrypt(self, message, password):
        salt = os.urandom(16)
        key = self.generate_key(password, salt)
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)

        # 딕셔너리를 JSON 문자열로 변환
        message_str = json.dumps(message)

        encrypted_message = aesgcm.encrypt(nonce, message_str.encode(), None)
        return base64.b64encode(salt + nonce + encrypted_message).decode()

    # 복호화 함수
    def decrypt(self, encrypted_message, password):
        decoded_message = base64.b64decode(encrypted_message.encode())
        salt = decoded_message[:16]
        nonce = decoded_message[16:28]
        ciphertext = decoded_message[28:]
        key = self.generate_key(password, salt)
        aesgcm = AESGCM(key)
        decrypted_message = aesgcm.decrypt(nonce, ciphertext, None)

        # JSON 문자열을 딕셔너리로 변환
        return json.loads(decrypted_message.decode())

  """
  # 예제
  cipher = Cipher()
  password = "your_password"
  message = {"name": "John", "age": 30}
  message = json.dumps(message)
  encrypted_message = cipher.encrypt(message, password)
  print(f"Encrypted: {encrypted_message}")

  decrypted_message = cipher.decrypt(encrypted_message, password)
  print(f"Decrypted: {decrypted_message}")
  """
  ```

15. save 시 파일 암호화하기

- 저장 파일을 암호화한다.
- save 함수를 호출 할 때, `암호를 입력해주세요: `와 함께 암호를 입력받도록 하고, 암호화할 때 암호와 함께 암호화한다.

16. load 시 파일 복호화하기

- 저장 파일을 복호화한다.
- load 함수를 호출 할 때, `암호를 입력해주세요: `와 함께 암호를 입력받도록 하고, 복호화할 때 암호화 함께 복호화한다.
- except Exception을 추가하여 암호가 틀렸을 경우 `[ERROR] 암호가 틀렸습니다.`가 호출되도록 한다.

17. 리팩토링 진행하기

- 현재 `object.py`의 `displayInfo` 함수에 `self.displayInfo(self.name)`로 되어있다. 이때 그럼 self.name이 출력되어야 할 것 같은데 왜 "플레이어" 혹은 "몬스터" 가 출력되는지 생각해보자.
- self.name을 지워도 출력이 잘 되는 이유를 생각해보자.

18. 개발자 모드

- 개발자 모드를 통해 개발 중 게임과 실제 플레이 게임을 구분해보고자 한다.
- `gameLauncher.py` 상단에 `GAME_MODE` 전역변수를 만들고 MODE_DEV = "
  DEV", MODE_NORMAL = "NORMAL" 상수를 만들어본다.
- 그리고 GameLauncher 클래스 상단에 second 인자를 받는 `sleep` 함수를 다음과 같이 만든다.
  - GAME_MODE가 DEV면, time.sleep(0) 그게 아니면 time.sleep(second)로 설정되게 한다.
- 아래의 위치에 모두 sleep 함수를 설정해준다.
  ```python
  print("몬스터가 나타났다!")
  monster = Monster()
  monster.displayInfo()
  sleep(3)
  ...
  print("플레이어의 공격 차례입니다.")
  sleep(1)
  ...
  sleep(2)
  print("몬스터의 공격 차례입니다.")
  sleep(1)
  ...
  if self.player.isDead():
    print("플레이어가 죽었습니다!")
    print("GAME OVER")
    self.exit()
    break
  sleep(2)
  ```
- play 함수에서 Player를 만들 때, GMAE_MODE 인자를 보내주고, Player 생성자에서 `mode`가 `dev`면 `hp = 20, atk = 5`로, 그게 아니면 기존대로 설정되게 해준다.
