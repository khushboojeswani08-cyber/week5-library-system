
from library_system.book import Book
from library_system.member import Member
from library_system.library import Library


def main():
    library = Library()
    library.load_data()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Search Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View All Books")
        print("7. Save and Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Book title: ").strip()
            author = input("Author name: ").strip()
            isbn = input("ISBN: ").strip()
            year_text = input("Publication year (optional): ").strip()
            year = int(year_text) if year_text.isdigit() else None

            success, message = library.add_book(
                Book(title, author, isbn, year)
            )
            print(message)

        elif choice == "2":
            name = input("Member name: ").strip()
            member_id = input("Member ID: ").strip()
            _, message = library.register_member(
                Member(name, member_id)
            )
            print(message)

        elif choice == "3":
            query = input("Search title, author or ISBN: ").strip()
            results = library.search_books(query)

            if results:
                for book in results:
                    print(book)
            else:
                print("No books found.")

        elif choice == "4":
            isbn = input("Book ISBN: ").strip()
            member_id = input("Member ID: ").strip()
            _, message = library.borrow_book(isbn, member_id)
            print(message)

        elif choice == "5":
            isbn = input("Book ISBN: ").strip()
            member_id = input("Member ID: ").strip()
            _, message = library.return_book(isbn, member_id)
            print(message)

        elif choice == "6":
            if library.books:
                for book in library.books.values():
                    print(book)
            else:
                print("No books in the library.")

        elif choice == "7":
            library.save_data()
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
          
