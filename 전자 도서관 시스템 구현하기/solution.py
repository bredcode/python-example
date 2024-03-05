import random

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.pages = random.randint(100, 1000)

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{self.title} 책이 대출되었습니다.")
        else:
            print(f"죄송합니다. {self.title}는 이미 대출 중입니다.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.title} 책이 반납되었습니다.")
        else:
            print(f"{self.title} 책은 대출되지 않았습니다.")

class EBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"[e-book] {self.title}이 대출되었습니다.\n페이지 수: {self.pages}")
        else:
            print(f"죄송합니다. '{self.title}'은 이미 대출 중입니다.")
            
eBook = EBook("홍길동전", "홍길동")
eBook.borrow_book()
eBook.borrow_book()
eBook.return_book()
eBook.return_book()
