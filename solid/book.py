from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, author: str, content: str):
        self.title = title
        self.author = author
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class PaperFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.title}\n{book.author}\n{book.content[:4]}\n"


class WebFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.title}"


class WholeContent(BaseFormatter): #formatter
    def format(self, book: Book)-> str:
        return f"{book.content}"


class Printer:
    def __init__(self, formatter: BaseFormatter):
        self.formatter = formatter

    def get_book(self, book: Book) -> str:
        return self.formatter.format(book)


book = Book("Zaglavie", "Avtoryt", "1234 56 78 9!@№$%%€§")
ps = Printer(PaperFormatter())
pb = Printer(WebFormatter())
print(Printer(WholeContent()).get_book(book))
print(ps.get_book(book))
print(pb.get_book(book))




