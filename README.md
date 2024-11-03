# Library-Management
Library Management System
This Python program implements a Library Management System, enabling the management of books for both the library and its users. The system allows users to borrow, return, and track books, while providing library administrators with essential book inventory features.

Features
Library Class
Initialization:

Creates a library_books.txt file to store all available books.
If the file already exists, it does not create a new one.
Add Book (library_add_book):

Adds new books to the library.
Checks for duplicates (case-insensitive) before adding.
Usage:
python
Copy code
lib = Library()
lib.library_add_book("The Great Gatsby")
List Books (lib_books_list):

Displays all books currently in the library.
Usage:
python
Copy code
lib.lib_books_list()
Library Details (lib_detail):

Shows statistics: total books, available books, and unavailable books (currently borrowed).
Usage:
python
Copy code
lib.lib_detail()
Book Users Class
Inherits from the Library class.

Initialization:

Creates a user-specific file named {username}_books.txt to track borrowed books.
Borrow Book (add_book):

Allows users to borrow books, marking them as taken in library_books.txt.
Checks if the book is already borrowed and informs the user.
Usage:
python
Copy code
user = Book_users("Alice")
user.add_book("The Great Gatsby")
List Borrowed Books (book_list):

Displays all books borrowed by the user.
Usage:
python
Copy code
user.book_list()
Count Borrowed Books (book_counts):

Counts and displays the total number of books borrowed by the user.
Usage:
python
Copy code
user.book_counts()
Return Book (book_return):

Allows users to return borrowed books, updating both their records and the library’s inventory.
Usage:
python
Copy code
user.book_return("The Great Gatsby")
Example Usage
Here’s a step-by-step example of how to use the system:

python
Copy code
# Step 1: Create a library instance
lib = Library()

# Step 2: Add books to the library
lib.library_add_book("The Great Gatsby")
lib.library_add_book("1984")

# Step 3: List all books in the library
lib.lib_books_list()

# Step 4: Create a user instance
user = Book_users("Alice")

# Step 5: User borrows a book
user.add_book("The Great Gatsby")

# Step 6: List all books borrowed by the user
user.book_list()

# Step 7: Count the number of books the user has borrowed
user.book_counts()

# Step 8: Return the borrowed book
user.book_return("The Great Gatsby")

# Step 9: View library details after the book return
lib.lib_detail()
Conclusion
This Library Management System provides a clear and organized way to manage books and user interactions. It effectively demonstrates file handling, user input, and basic object-oriented programming concepts in Python.
