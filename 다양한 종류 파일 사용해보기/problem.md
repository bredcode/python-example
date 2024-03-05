### 문제

당신은 매력적인 고양이 카페의 주인으로, 방문객들에게 고양이와 함께하는 시간을 더욱 특별하게 만들어주고 싶어 합니다.

하루는, 고양이들이 노는 모습을 보며 감성이 충만해져서, 고양이에 대한 시를 몇 편 적었습니다. 이 시들을 고객들과 공유하고 싶지만, 각 테이블에 시집을 두기에는 비용이 너무 많이 듭니다.

그래서 파이썬 프로그래밍의 힘을 빌려, 디지털 방식으로 시를 공유하기로 결심했습니다.

이를 위해, 고양이에 관한 시가 담긴 텍스트 파일을 QR 코드로 변환하여, 고객이 스마트폰으로 쉽게 읽을 수 있게 하려고 합니다.

#### 과제 내용

1.  `./assets/kitten_poetry.txt` 파일을 열어 고양이에 관한 시의 모음을 읽습니다. 이 파일에는 고양이들의 우아함과 장난기를 담은 여러 편의 시가 담겨 있습니다.
2.  읽은 시의 모음 끝에, 당신의 카페를 상징하는 문구인 `"역시 파이썬이 최고다냥"`을 추가합니다. 이 작업을 통해, 당신의 카페만의 특별한 메시지를 고객에게 전달하려 합니다.
3.  수정된 시 모음을 `./assets/custom_kitten_poetry.txt`로 저장합니다. 이 파일은 당신이 고객에게 제공하려는 디지털 시집의 원본이 됩니다.
4.  파이썬의 `qrcode` 라이브러리를 사용하여, 수정된 시 모음이 담긴 `custom_kitten_poetry.txt` 파일을 QR 코드로 변환합니다. 이 QR 코드는 카페 곳곳에 배치하여, 고객이 자신의 스마트폰으로 쉽게 스캔하고 읽을 수 있도록 할 예정입니다.
5.  마지막으로, 생성된 QR 코드를 화면에 표시하여, 정상적으로 작동하는지 확인합니다. 이 QR 코드는 곧 당신의 카페의 새로운 매력 포인트가 될 것입니다.

#### 필요한 도구

- `PIL` 라이브러리
- `qrcode` 라이브러리

* 위 두 라이브러리를 `pip install qrcode[pil]` 또는 `pip install qrcode pillow`를 통해 설치하세요

#### 구현 가이드

**QR 코드 생성 및 이미지 저장**

```python
import qrcode

# QR 코드 생성
qr = qrcode.QRCode(
  version=1,  # QR 코드의 버전 (1~40) 크기를 조절합니다.
  error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 보정 수준
  box_size=10,  # QR 코드 각 박스의 픽셀 크기
  border=4,  # QR 코드의 테두리 두께
)

# 텍스트 파일의 내용을 이용하여 QR 코드 생성
with open('./assets/custom_kitten_poetry.txt', 'r', encoding='utf-8') as file:
  text = file.read()
  qr.add_data(text)
  qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# QR 코드 이미지를 화면에 표시
img.show()

# QR 코드 이미지 저장 (선택적)
# img.save("../assets/kitten_poetry_qr.png")
```
