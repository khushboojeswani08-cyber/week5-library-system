
import unittest
from library_system.member import Member


class TestMember(unittest.TestCase):

    def test_member_creation(self):
        member = Member("Aman", "M01")
        self.assertEqual(member.name, "Aman")
        self.assertEqual(member.member_id, "M01")

    def test_borrow_book(self):
        member = Member("Aman", "M01")
        success, message = member.borrow_book("101")
        self.assertTrue(success)
        self.assertIn("101", member.borrowed_books)

    def test_return_book(self):
        member = Member("Aman", "M01")
        member.borrow_book("101")
        success, message = member.return_book("101")
        self.assertTrue(success)
        self.assertNotIn("101", member.borrowed_books)


if __name__ == "__main__":
    unittest.main()
