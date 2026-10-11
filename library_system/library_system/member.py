
class Member:
    """Represents a library member."""

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.max_books = 5

    def borrow_book(self, isbn):
        if len(self.borrowed_books) >= self.max_books:
            return False, "Borrowing limit reached."

        if isbn in self.borrowed_books:
            return False, "This book is already borrowed."

        self.borrowed_books.append(isbn)
        return True, "Book added to borrowed list."

    def return_book(self, isbn):
        if isbn not in self.borrowed_books:
            return False, "This book is not in your borrowed list."

        self.borrowed_books.remove(isbn)
        return True, "Book returned successfully."

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(data["name"], data["member_id"])
        member.borrowed_books = data.get("borrowed_books", [])
        return member

    def __str__(self):
        return (
            f"Member: {self.name} | ID: {self.member_id} | "
            f"Books borrowed: {len(self.borrowed_books)}"
        )
