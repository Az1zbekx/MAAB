class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if member is None:
            return
        book = self.find_book(book_title)
        if book.is_borrowed:
            raise BookAlreadyBorrowedException
        if len(member.borrowed_books) >= 3:
            raise MemberLimitExceededException
        book.is_borrowed = True
        member.borrowed_books.append(book)

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if member is None:
            return
        book = self.find_book(book_title)
        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
            book.is_borrowed = False

library = Library()

library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("Brave New World", "Aldous Huxley"))
library.add_book(Book("Fahrenheit 451", "Ray Bradbury"))
library.add_book(Book("The Alchemist", "Paulo Coelho"))

library.add_member(Member("Alice"))
library.add_member(Member("Bob"))

try:
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "Brave New World")
    library.borrow_book("Alice", "Fahrenheit 451")
    library.borrow_book("Alice", "The Alchemist")
except MemberLimitExceededException:
    print("MemberLimitExceededException")
except BookAlreadyBorrowedException:
    print("BookAlreadyBorrowedException")
except BookNotFoundException:
    print("BookNotFoundException")

try:
    library.borrow_book("Bob", "1984")
except MemberLimitExceededException:
    print("MemberLimitExceededException")
except BookAlreadyBorrowedException:
    print("BookAlreadyBorrowedException")
except BookNotFoundException:
    print("BookNotFoundException")

library.return_book("Alice", "1984")

try:
    library.borrow_book("Bob", "1984")
except MemberLimitExceededException:
    print("MemberLimitExceededException")
except BookAlreadyBorrowedException:
    print("BookAlreadyBorrowedException")
except BookNotFoundException:
    print("BookNotFoundException")

try:
    library.borrow_book("Bob", "Nonexistent Book")
except MemberLimitExceededException:
    print("MemberLimitExceededException")
except BookAlreadyBorrowedException:
    print("BookAlreadyBorrowedException")
except BookNotFoundException:
    print("BookNotFoundException")
