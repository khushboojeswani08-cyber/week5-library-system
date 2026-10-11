
# Library Management System

## Project Overview
A Library Management System developed using Python Object-Oriented Programming (OOP). It helps manage books, library members, borrowing, and returning books.

## Features
- Add new books to the library
- Register library members
- Search books by title, author, or ISBN
- Borrow and return books
- Track book availability and due dates
- Detect overdue books
- Save and load records using JSON files

## Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- JSON
- Unit Testing

## Project Structure
```text
week5-library-system/
├── main.py
├── library_system/
│   ├── __init__.py
│   ├── book.py
│   ├── member.py
│   └── library.py
├── data/
│   ├── books.json
│   └── members.json
├── tests/
│   ├── test_book.py
│   └── test_member.py
└── README.md
```

## How to Run
1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run:

```bash
python main.py
```

## How to Run Tests
Run the following command from the project directory:

```bash
python -m unittest discover -s tests
```

## Learning Outcomes
- Understanding classes and objects
- Using methods and constructors
- Managing relationships between books and members
- Saving and loading data using JSON
- Writing unit tests

## Author
Khushboo Jeswani
