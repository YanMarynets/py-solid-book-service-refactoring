from abc import ABC, abstractmethod

from app.book import Book


class PrintBook(ABC):
    @abstractmethod
    def print_book(self, book: Book):
        pass


class PrintConsole(PrintBook):
    def print_book(self, book: Book):
        print(book.title)
        print(book.content)


class PrintReverse(PrintBook):
    def print_book(self, book: Book):
        print(book.title)
        print(book.content[::-1])