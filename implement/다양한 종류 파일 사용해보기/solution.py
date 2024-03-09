# '../assets/kitten_poetry.txt' 파일을 읽어서 마지막에 "파이썬 프로그래밍" 문구 추가 후 저장
poetry_path = './assets/kitten_poetry.txt'
custom_poetry_path = './assets/custom_kitten_poetry.txt'

# 파일 읽기
with open(poetry_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 내용 수정
content += "\n역시 파이썬이 최고다냥"

# 수정된 내용을 새 파일에 저장
with open(custom_poetry_path, 'w', encoding='utf-8') as file:
    file.write(content)

"""
# 또는 "a"를 통해 파일 끝에 내용 추가
with open(poetry_path, 'a', encoding='utf-8') as file:
    file.write("\n역시 파이썬이 최고다냥")
"""

import qrcode

# QR 코드 생성
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# QR 코드에 추가할 데이터 (수정된 시)
with open(custom_poetry_path, 'r', encoding='utf-8') as file:
    text = file.read()

qr.add_data(text)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# QR 코드 이미지를 화면에 표시
img.show()

# QR 코드 이미지를 파일로 저장 (선택 사항)
# img.save("../assets/kitten_poetry_qr.png")
