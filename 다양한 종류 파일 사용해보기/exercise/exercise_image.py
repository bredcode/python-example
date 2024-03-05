"""
Pillow는 파이썬에서 가장 인기 있는 이미지 처리 라이브러리 중 하나로, 
이미지를 로드, 처리, 저장하는 다양한 기능을 제공합니다. 
아래는 몇 가지 기본적인 사용 예제입니다.
"""

# 이미지 파일을 열고 보여줍니다.
from PIL import Image

image = Image.open('../assets/kitten.jpg')
image.show()


# 이미지를 90도 회전합니다.
from PIL import Image

image = Image.open('../assets/kitten.jpg')
rotated_image = image.rotate(90)
rotated_image.show()


# 이미지에 가우시안 블러 필터를 적용합니다.
from PIL import Image, ImageFilter

image = Image.open('../assets/kitten.jpg')
blurred_image = image.filter(ImageFilter.GaussianBlur(5))
blurred_image.show()


# 이미지의 일부분을 자릅니다. (x0, y0, x1, y1)
from PIL import Image

image = Image.open('../assets/kitten.jpg')
cropped_image = image.crop((50, 50, 200, 200))
cropped_image.show()


# 이미지를 다른 형식으로 저장합니다.
from PIL import Image

image = Image.open('../assets/kitten.jpg')
image.save('../assets/kitten.png')


# 이미지 파일을 삭제합니다.
import os

file_path = '../assets/kitten.png'
if os.path.exists(file_path): # 파일이 존재하는지 확인합니다.
    os.remove(file_path)
    print(f"{file_path} 파일이 삭제되었습니다.")
else:
    print(f"{file_path} 파일을 찾을 수 없습니다.")


# 이미지의 크기, 포맷, 모드 등의 정보를 출력합니다.
from PIL import Image

image = Image.open('../assets/kitten.jpg')
print(f"크기: {image.size}")
print(f"포맷: {image.format}")
print(f"모드: {image.mode}")