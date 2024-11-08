import re

# Library class that handles library-wide operations
class Library:
    def __init__(self):
        # Try to create a library_books.txt file if it doesn't exist
        try:
            open("library_books.txt", "x").close()
        except FileExistsError:
            pass  # If file already exists, do nothing

    # Method to add a book to the library's inventory
    def library_add_book(self, book_name):
        # Open the library_books.txt file and read all the books into a list
        with open("library_books.txt", "r") as lib_books:
            lib_books_lis = [book.title().strip() for book in lib_books]
            
            # Check if the book is already available or borrowed (contains "Is Taken By")
            if book_name.title().strip() in lib_books_lis or re.search(f"{book_name.title().strip()} Is Taken By .*", " ".join(lib_books_lis)) != None:
                print("\nThis Book is already available in the Library.")
            else:
                # Add the book to the library_books.txt file if not already present
                with open("library_books.txt", "a") as lib_books:
                    lib_books.write(f"{book_name.title().strip()}\n")
                    print(f"{book_name} has been added in the library.")

    # Method to list all books in the library
    def lib_books_list(self):
        print("\nAll Books:")
        # Open the library_books.txt and print each book
        with open("library_books.txt", "r") as lib_books:
            for no, book in enumerate(lib_books, start=1):
                print(f"{no}. {book}", end="")

    # Method to display library statistics: total books, available books, unavailable books
    def lib_detail(self):
        total_lib_books = 0
        lib_avail_books = 0
        lib_unavail_books = 0
        # Open the library_books.txt file to calculate book statistics
        with open("library_books.txt", "r") as lib_books:
            for book in lib_books:
                total_lib_books += 1
                # Count unavailable books (books marked as "Is Taken By")
                if "Is Taken By" in book:
                    lib_unavail_books += 1
                else:
                    lib_avail_books += 1

        # Print the calculated statistics
        print(f"\nTotal Library Books: {total_lib_books}")
        print(f"Total Available Books: {lib_avail_books}")
        print(f"Total Unavailable Books: {lib_unavail_books}")


# Book_users class inherits from Library and handles user-specific book operations
class Book_users(Library):
    def __init__(self, name):
        self.name = name
        self.no_of_books = 0
        # Create a user-specific file to track borrowed books (if it doesn't exist)
        try:
            open(f"{self.name}_books.txt", "x")
        except FileExistsError:
            pass  # If the file already exists, do nothing

    # Method to allow a user to borrow a book
    def add_book(self, book_name):
        # Open the library_books.txt file to check the availability of the book
        with open("library_books.txt", "r") as lib_books:
            all_lib_books = [book.title().strip().strip("\n") for book in lib_books]

        # Check if the book is already borrowed (contains "Is Taken By")
        for book in all_lib_books:
            if f"{book_name.title().strip()} Is Taken By" in book:
                return print(f"\n{book}")  # Inform the user that the book is already taken

        # If the book is available in the library
        if book_name.title().strip() in all_lib_books:
            # Add the book to the user's list of borrowed books
            with open(f"{self.name}_books.txt", "a") as my_books:
                my_books.write(f"{book_name.title().strip()}\n")
            # Update the library's inventory to mark the book as taken by the user
            with open("library_books.txt", "w") as lib_books:
                for book in all_lib_books:
                    if book_name.title().strip() == book.title().strip():
                        lib_books.write(f"{book_name.title().strip()} Is Taken By {self.name}.\n")
                    else:
                        lib_books.write(f"{book.title().strip()}\n")
            
            return print(f"\n{book_name.title().strip()} is issued to {self.name}.")
        
        else:
            return print("\nThis Book is not available in this library.")  # Book not found in the library

    # Method to list all books borrowed by the user
    def book_list(self):
        print(f"\n{self.name} All Books:")
        # Open the user's borrowed books file and print each book
        with open(f"{self.name}_books.txt", "r") as my_books:
            for no, book in enumerate(my_books, start=1):
                print(f"{no}. {book.title()}", end="")

    # Method to count the number of books borrowed by the user
    def book_counts(self):
        # Open the user's borrowed books file and count the books
        with open(f"{self.name}_books.txt", "r") as my_books:
            for _ in my_books:
                self.no_of_books += 1
        print(f"\nTotal no. of books {self.name} has is {self.no_of_books}")

    # Method to allow the user to return a borrowed book
    def book_return(self, book_name):
        # Open the user's borrowed books file to check if they have the book
        with open(f"{self.name}_books.txt", "r") as my_books:
            my_book_list = [book.title().strip().strip("\n") for book in my_books]
        # If the user has borrowed the book
        if book_name.title().strip() in my_book_list:
            # Remove the book from the user's borrowed books list
            for book in my_book_list:
                if book_name.title().strip() != book:
                    with open(f"{self.name}_books.txt", "w") as my_books:
                        my_books.write(f"{book}\n")

            # Open the library's inventory and return the book to the library
            with open("library_books.txt", "r") as lib_books:
                all_lib_books = [book.title().strip().strip("\n") for book in lib_books]
                with open("library_books.txt", "w") as lib_books:
                    for book in all_lib_books:
                        # If the book is found in the inventory, mark it as available again
                        if book_name.title().strip() in book:
                            lib_books.write(f"{book_name.title().strip()}\n")
                        else:
                            lib_books.write(f"{book}\n")
                    print(f"\n{book_name.title().strip()} is returned to the library.")
        else:
            print("\nYou don't have any book with this name.")  # Book was not borrowed by the user


# Create an instance of the Library class
school_library = Library()

# Create an instance of the Book_users class for a user named "your name"
your_name = Book_users("your name")
