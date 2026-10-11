
import unittest
from library_system.book import Book


class TestBook(unittest.TestCase):

    def test_book_creation(self):
        book = Book("Python Basics", "John", "101")
        self.assertEqual(book.title, "Python Basics")
        self.assertTrue(book.available)

    def test_checkout_book(self):
        book = Book("Python Basics", "John", "101")
        success, message = book.check_out("M01")
        self.assertTrue(success)
        self.assertFalse(book.available)

    def test_return_book(self):
        book = Book("Python Basics", "John", "101")
        book.check_out("M01")
        success, message = book.return_book()
        self.assertTrue(success)
        self.assertTrue(book.available)

    def test_book_to_dict(self):
        book = Book("Python Basics", "John", "101")
        data = book.to_dict()
        self.assertEqual(data["isbn"], "101")


if __name__ == "__main__":
    unittest.main()
      
