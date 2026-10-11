
import json
import os
from book import Book
from member import Member


class Library:
    """Manages books and members."""

    def __init__(self, data_dir="data"):
        self.books = {}
        self.members = {}
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

    def add_book(self, book):
        if book.isbn in self.books:
            return False, "Book already exists."

        self.books[book.isbn] = book
        return True, "Book added successfully."

    def register_member(self, member):
        if member.member_id in self.members:
            return False, "Member already exists."

        self.members[member.member_id] = member
        return True, "Member registered successfully."

    def search_books(self, query):
        query = query.lower()
        return [
            book for book in self.books.values()
            if query in book.title.lower()
            or query in book.author.lower()
            or query in book.isbn.lower()
        ]

    def borrow_book(self, isbn, member_id):
        book = self.books.get(isbn)
        member = self.members.get(member_id)

        if not book:
            return False, "Book not found."
        if not member:
            return False, "Member not found."
        if not book.available:
            return False, "Book is not available."

        success, message = member.borrow_book(isbn)
        if not success:
            return False, message

        success, message = book.check_out(member_id)
        if not success:
            member.return_book(isbn)
            return False, message

        return True, message

    def return_book(self, isbn, member_id):
        book = self.books.get(isbn)
        member = self.members.get(member_id)

        if not book or not member:
            return False, "Book or member not found."
        if book.borrowed_by != member_id:
            return False, "This book was not borrowed by this member."

        member.return_book(isbn)
        return book.return_book()

    def save_data(self):
        with open(os.path.join(self.data_dir, "books.json"), "w") as f:
            json.dump(
                [b.to_dict() for b in self.books.values()],
                f, indent=4
            )

        with open(os.path.join(self.data_dir, "members.json"), "w") as f:
            json.dump(
                [m.to_dict() for m in self.members.values()],
                f, indent=4
            )

    def load_data(self):
        books_file = os.path.join(self.data_dir, "books.json")
        members_file = os.path.join(self.data_dir, "members.json")

        if os.path.exists(books_file):
            with open(books_file, "r") as f:
                for item in json.load(f):
                    book = Book.from_dict(item)
                    self.books[book.isbn] = book

        if os.path.exists(members_file):
            with open(members_file, "r") as f:
                for item in json.load(f):
                    member = Member.from_dict(item)
                    self.members[member.member_id] = member
