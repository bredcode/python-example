# 1. 전체 파일 내용을 한 번에 읽기
print("\n1. 전체 파일 내용을 한 번에 읽기")
with open('../assets/kitten.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# 2. 파일 내용을 줄 단위로 읽기
print("\n2. 파일 내용을 줄 단위로 읽기")
with open('../assets/kitten.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip()) # strip() 함수를 사용하여 줄바꿈 문자를 제거합니다.

# 3. 파일 내용을 줄 단위로 리스트에 저장하기
print("\n3. 파일 내용을 줄 단위로 리스트에 저장하기")
with open('../assets/kitten.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines() # 파일의 모든 줄을 읽어서 리스트로 반환합니다.
    print(lines)

# 4. 파일 내용을 한 번에 읽은 후, 줄 단위로 처리하기
print("\n4. 파일 내용을 한 번에 읽은 후, 줄 단위로 처리하기")
with open('../assets/kitten.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    lines = content.splitlines()  # 파일 내용을 줄바꿈 기준으로 분리하여 리스트로 만듭니다.
    for line in lines:
        print(line)
