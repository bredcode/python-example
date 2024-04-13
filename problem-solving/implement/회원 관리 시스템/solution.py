class Member:
    def __init__(self, id, pw):
        self.id = id
        self.pw = pw

class MemberRegister:
    def __init__(self):
        self.member = {}

    def signUp(self, id, pw):
      if id in self.member:
        print(f"{id} is already exists.")
        return
      self.member[id] = pw
      print(f"{id} : sign up success!")

    def login(self, id, pw):
      isMember = id in self.member
      if isMember and self.member[id] == pw:
        print(f"{id} : login success!")
      elif isMember and self.member[id] != pw:
        print(f"invalid password")
      else:
        print(f"{id} does not exist.")

    def viewAllMembers(self):
      for [id, pwd] in self.member.items():
        print(f"ID: {id}")
        print(f"PWD: {pwd}")

    def deleteMember(self, id, pw):
      isMember = id in self.member
      if isMember and self.member[id] == pw:
        del self.member[id]
        print(f"{id} : delete success!")
      elif isMember and self.member[id] != pw:
        print(f"invalid password")
      else:
        print(f"{id} does not exist.")

def display():
  print("\n=====회원 관리 시스템=====")
  print("1. 회원 가입")
  print("2. 로그인")
  print("3. 회원 전체 조회")
  print("4. 회원 삭제")
  print("5. 종료")
  print("=========================\n")

memberRegister = MemberRegister()

while True:
  display()
  num = input("원하는 번호를 입력해 주세요 : ")

  if num == "1":
    print("[회원 가입]")
    id = input("ID : ")
    pw = input("PW : ")
    member = Member(id, pw)
    memberRegister.signUp(id, pw)

  elif num == "2":
    print("[로그인]")
    id = input("ID : ")
    pw = input("PW : ")
    memberRegister.login(id, pw)

  elif num == "3":
    print("[회원 전체 조회]")
    memberRegister.viewAllMembers()

  elif num == "4":
    print("[회원 삭제]")
    id = input("ID : ")
    pw = input("PW : ")
    memberRegister.deleteMember(id, pw)

  elif num == "5":
     break