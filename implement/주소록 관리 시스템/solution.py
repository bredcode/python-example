import os
import shutil

CONTACTS_DIR = "contacts"

def show_menu():
    print("===== 주소록 관리 프로그램 =====")
    print("1. 연락처 추가")
    print("2. 연락처 검색")
    print("3. 연락처 수정")
    print("4. 연락처 삭제")
    print("5. 주소록 폴더 삭제")
    print("6. 종료")
    print("==============================")

def add_contact():
    name = input("이름을 입력하세요: ")
    phone = input("전화번호를 입력하세요: ")
    email = input("이메일을 입력하세요: ")

    if not os.path.exists(CONTACTS_DIR):
        os.makedirs(CONTACTS_DIR)

    contact_file = os.path.join(CONTACTS_DIR, f"{name}.txt")
    with open(contact_file, "w", encoding="utf-8") as f:
        f.write(f"이름: {name}\n전화번호: {phone}\n이메일: {email}\n")
    print("연락처가 추가되었습니다.")

def search_contact():
    search_name = input("검색할 이름을 입력하세요: ")
    contact_file = os.path.join(CONTACTS_DIR, f"{search_name}.txt")

    if os.path.exists(contact_file):
        with open(contact_file, "r", encoding="utf-8") as f:
            print(f"{search_name}의 연락처 정보:")
            print(f.read())
    else:
        print("해당하는 연락처를 찾을 수 없습니다.")

def modify_contact():
    search_name = input("수정할 연락처의 이름을 입력하세요: ")
    contact_file = os.path.join(CONTACTS_DIR, f"{search_name}.txt")

    if os.path.exists(contact_file):
        print(f"{search_name}의 현재 연락처 정보:")
        with open(contact_file, "r", encoding="utf-8") as f:
            print(f.read())

        phone = input("새로운 전화번호를 입력하세요: ")
        email = input("새로운 이메일을 입력하세요: ")

        with open(contact_file, "w", encoding="utf-8") as f:
            f.write(f"이름: {search_name}\n전화번호: {phone}\n이메일: {email}\n")
        print("연락처가 수정되었습니다.")
    else:
        print("해당하는 연락처를 찾을 수 없습니다.")

def delete_contact():
    search_name = input("삭제할 연락처의 이름을 입력하세요: ")
    contact_file = os.path.join(CONTACTS_DIR, f"{search_name}.txt")

    if os.path.exists(contact_file):
        os.remove(contact_file)
        print("연락처가 삭제되었습니다.")
    else:
        print("해당하는 연락처를 찾을 수 없습니다.")

def delete_address_book():
    confirm = input("정말로 주소록 폴더를 삭제하시겠습니까? (y/n): ")
    if confirm.lower() == 'y':
        try:
            shutil.rmtree(CONTACTS_DIR, ignore_errors=True)
            print("주소록 폴더가 삭제되었습니다.")
        except Exception as e:
            print(f"주소록 폴더 삭제 중 오류가 발생했습니다: {e}")
    else:
        print("주소록 폴더 삭제를 취소합니다.")

def main():
    while True:
        show_menu()
        choice = input("작업을 선택하세요: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            modify_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            delete_address_book()
        elif choice == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()
