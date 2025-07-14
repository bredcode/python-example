### 전자 도서관 시스템 구현하기

#### 과제 배경

당신은 작은 마을의 도서관을 디지털화하기 위한 프로젝트에 참여하고 있습니다. 프로젝트의 목표 중 하나는 도서 및 전자책(e-book)의 대출 및 반납 시스템을 구현하는 것입니다. 여러분의 작업은 파이썬을 사용하여 이 시스템을 개발하는 것입니다.

#### 과제 요구사항

1.  **도서(Book) 클래스 구현**: 모든 도서의 기본이 되는 클래스를 구현해야 합니다. 각 책은 제목(`title`), 저자(`author`), 대출 상태(`is_borrowed`), 그리고 페이지 수(`pages`)를 속성으로 가집니다. 페이지 수는 100에서 1000 페이지 사이의 임의의 값으로 설정되어야 합니다. 또한, 도서 대출(`borrow_book`) 및 반납(`return_book`) 메소드를 구현해야 합니다.
2.  **전자책(EBook) 클래스 구현**: `Book` 클래스를 상속받아 `EBook` 클래스를 구현합니다. `EBook` 클래스에서는 책의 페이지 수를 설정할 때 `random` 패키지를 사용해야 합니다. 추가적으로, `EBook` 클래스는 도서 대출 시 전자책임을 나타내는 특별한 메시지를 출력해야 합니다.

#### 구현해야 할 코드

여러분은 아래의 요구 사항에 맞게 `Book` 클래스와 `EBook` 클래스를 구현해야 합니다.

- `Book` 클래스는 초기화 시 제목(`title`)과 저자(`author`)를 입력받아야 합니다. 이 클래스는 도서가 대출 가능한 상태인지 확인하고, 대출 상태를 관리할 수 있는 메소드를 포함해야 합니다.
- `EBook` 클래스는 `Book` 클래스를 상속받으며, 페이지 수(`pages`)는 100에서 1000 사이의 임의의 값으로 설정됩니다. 이 설정은 클래스가 인스턴스화될 때 자동으로 이루어져야 합니다.
- 도서 대출(`borrow_book`) 메소드는 대출 시도 시 책의 대출 가능 여부를 확인하고, 적절한 메시지를 출력해야 합니다. 이미 대출된 도서를 대출하려고 시도할 경우, 오류 메시지를 출력합니다.
- 반납(`return_book`) 메소드는 책의 반납을 처리하고, 적절한 메시지를 출력합니다.

#### 제출 방법

- 제출하신 코드는 위의 요구 사항을 모두 충족해야 합니다.
- 코드를 작성한 후, 아래의 예시처럼 실행하여 예상되는 출력을 확인하세요.

#### 예시 출력

- { } 속 내용은 클래스 생성 시 기입한 내용들로 표기

```
[e-book] {책이름}이 대출되었습니다.
페이지 수: {랜덤 페이지 수} // ex) 665
죄송합니다. {책이름}은 이미 대출 중입니다.
{책이름}이 반납되었습니다.
{책이름}은 대출되지 않았습니다.
```

---

#### Hard

```python
import random

class Book:
  # Book 클래스 작성

class EBook(Book):
  # EBook 클래스 작성

eBook = EBook("홍길동전", "홍길동")
eBook.borrow_book()
eBook.borrow_book()
eBook.return_book()
eBook.return_book()
```

<br/><br/><br/><br/><br/>
<br/><br/><br/><br/><br/>

---

### Easy

```python
import random

class Book:
    def __init__(self, title, author):
        # 아래 = 뒤에 필요한 내용 작성
        self.title =
        self.author =
        self.is_borrowed =
        self.pages =


    def borrow_book(self):
        # 대출 로직

    def return_book(self):
        # 반납 로직

class EBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)

    def borrow_book(self):
       # 반납 로직

eBook = EBook("홍길동전", "홍길동")
eBook.borrow_book()
eBook.borrow_book()
eBook.return_book()
eBook.return_book()
```
