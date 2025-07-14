class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"죄송합니다. '{self.title}'은 이미 대출 중입니다.")
        else:
            self.is_borrowed = True
            print(f"'{self.title}'이 대출되었습니다.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}'이 반납되었습니다.")
        else:
            print(f"'{self.title}'은 대출되지 않았습니다.")

book1 = Book("해리 포터")

book1.borrow()        # '해리 포터'이 대출되었습니다.
book1.borrow()        # 죄송합니다. '해리 포터'은 이미 대출 중입니다.
book1.return_book()   # '해리 포터'이 반납되었습니다.
book1.return_book()   # '해리 포터'은 대출되지 않았습니다.
