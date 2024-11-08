Library Management System (Updated Version)
This Python program implements a Library Management System (LMS), allowing both library administrators and users to manage books. It includes the ability to borrow, return, and track books, while also providing essential inventory management features for the library.

Features
Library Class
Initialization:

Creates a library_books.txt file to store all available books in the library. If the file already exists, it doesn't create a new one.
Methods:

library_add_book(self, book_name):

Adds new books to the library inventory, ensuring that there are no duplicates (case-insensitive).
Checks if the book is already available or borrowed by someone.
If the book is available, it adds it to the library_books.txt file.
Usage:

python
Copy code
lib = Library()
lib.library_add_book("The Great Gatsby")
lib_books_list(self):

Lists all the books currently in the library (whether available or unavailable).
Usage:

python
Copy code
lib.lib_books_list()
lib_detail(self):

Displays library statistics: total number of books, available books, and unavailable books (currently borrowed).
Usage:

python
Copy code
lib.lib_detail()
Book Users Class
The Book_users class inherits from the Library class and adds functionalities specific to users, such as borrowing and returning books.

Initialization:

Creates a user-specific file (named {username}_books.txt) to track borrowed books.
If the user’s file does not exist, it is created automatically.
Methods:

add_book(self, book_name):

Allows a user to borrow a book, marking it as taken in library_books.txt and adding it to the user's borrowed books list in {username}_books.txt.
It checks if the book is already borrowed (either by the user or another) before issuing it.
Usage:

python
Copy code
user = Book_users("Alice")
user.add_book("The Great Gatsby")
book_list(self):

Displays all the books borrowed by the user.
Usage:

python
Copy code
user.book_list()
book_counts(self):

Counts and displays the total number of books the user has borrowed.
Usage:

python
Copy code
user.book_counts()
book_return(self, book_name):

Allows users to return borrowed books. It updates both the user's record and the library's inventory.
Usage:

python
Copy code
user.book_return("The Great Gatsby")
Example Usage
Here’s a step-by-step example demonstrating how to use the Library Management System:

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
Key Updates and Features
Preventing Duplicate Book Entries:

In the library_add_book method, the program now checks if the book is already present in the library (case-insensitive), and it also verifies if a book has already been borrowed by someone. This prevents the addition of duplicate books.
Example:

python
Copy code
lib.library_add_book("The Great Gatsby")
If "The Great Gatsby" is already in the library or borrowed, it will not be added again.

Improved Borrowing Logic:

When a user attempts to borrow a book using add_book(), the program checks if the book is available and not already borrowed by another user. If the book is already borrowed, the program will inform the user and prevent borrowing.
Example:

python
Copy code
user.add_book("The Great Gatsby")
Book Return Functionality:

The book_return() method has been updated to ensure that when a book is returned, the user’s borrowed books list ({username}_books.txt) and the library’s inventory (library_books.txt) are both updated correctly.
This method now ensures the proper update of the library’s inventory after a book is returned, making the book available again.
Example:

python
Copy code
user.book_return("The Great Gatsby")
Improved Data Integrity:

When a book is returned, the book_return() method checks that the user is actually borrowing the book before attempting to return it. This ensures that a book can only be returned if the user has previously borrowed it.
Included Files
library_books.txt: A file that contains the list of available books in the library. If the file doesn’t exist, it is created automatically when the library instance is initialized.
{username}_books.txt: A user-specific file that tracks the books borrowed by each user. If it doesn’t exist, it is created when the user instance is initialized.
Conclusion
This Library Management System provides a straightforward and organized way to manage books and user interactions in a library setting. It includes file handling, user input, and basic object-oriented programming principles. The system now also ensures that book borrowing and returning are accurately managed with proper data integrity
