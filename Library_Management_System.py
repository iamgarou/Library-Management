class Library:
    def __init__(self):
        # Attempt to create the library_books.txt file. If it exists, do nothing.
        try:
            open("library_books.txt", "x")
        except FileExistsError:
            pass

    def library_add_book(self, book_name):
        # Add a new book to the library if it doesn't already exist
        with open("library_books.txt", "r") as lib_books:
            lib_books_lis = [book.title().strip() for book in lib_books]
            if book_name.title().strip() in lib_books_lis:
                print("\nThis Book is already available in the Library.")
            else:
                with open("library_books.txt", "a") as lib_books:
                    lib_books.write(f"{book_name.title().strip()}\n")
                    print(f"{book_name} has been added in the library.")

    def lib_books_list(self):
        # Display all books currently in the library
        print("\nAll Books:")
        with open("library_books.txt", "r") as lib_books:
            for no, book in enumerate(lib_books, start=1):
                print(f"{no}. {book}", end="")

    def lib_detail(self):
        # Show statistics about the library's books
        total_lib_books = 0
        lib_avail_books = 0
        lib_unavail_books = 0
        with open("library_books.txt", "r") as lib_books:
            for book in lib_books:
                total_lib_books += 1
                if "Is Taken By" in book:
                    lib_unavail_books += 1
                else:
                    lib_avail_books += 1

        print(f"\nTotal Library Books: {total_lib_books}")
        print(f"Total Available Books: {lib_avail_books}")
        print(f"Total Unavailable Books: {lib_unavail_books}")


class Book_users(Library):
    def __init__(self, name):
        self.name = name  # Store the user's name
        self.no_of_books = 0  # Initialize the count of books borrowed
        # Create a file to track this user's borrowed books
        try:
            open(f"{self.name}_books.txt", "x")
        except FileExistsError:
            pass

    def add_book(self, book_name):
        # Allow the user to borrow a book if it's available
        with open("library_books.txt", "r") as lib_books:
            all_lib_books = [book.title().strip().strip("\n") for book in lib_books]

        # Check if the book is already borrowed
        for book in all_lib_books:
            if f"{book_name.title().strip()} Is Taken By" in book:
                return print(f"\n{book}")

        # If the book is available, borrow it
        if book_name.title().strip() in all_lib_books:
            with open(f"{self.name}_books.txt", "a") as my_books:
                my_books.write(f"{book_name.title().strip()}\n")
            # Update the library record to mark the book as borrowed
            with open("library_books.txt", "w") as lib_books:
                for book in all_lib_books:
                    if book_name.title().strip() == book.title().strip():
                        lib_books.write(f"{book_name.title().strip()} Is Taken By {self.name}.\n")
                    else:
                        lib_books.write(f"{book.title().strip()}\n")
            
            return print(f"\n{book_name.title().strip()} is issued to {self.name}.")
        
        else:
            return print("\nThis Book is not available in this library.")

    def book_list(self):
        # Display all books borrowed by the user
        print(f"\n{self.name} All Books:")
        with open(f"{self.name}_books.txt", "r") as my_books:
            for no, book in enumerate(my_books, start=1):
                print(f"{no}. {book.title()}", end="")

    def book_counts(self):
        # Count and display the total number of books borrowed by the user
        with open(f"{self.name}_books.txt", "r") as my_books:
            for _ in my_books:
                self.no_of_books += 1
        print(f"\nTotal no. of books {self.name} has is {self.no_of_books}")

    def book_return(self, book_name):
        # Allow the user to return a borrowed book
        with open(f"{self.name}_books.txt", "r") as my_books:
            my_book_list = [book.title().strip().strip("\n") for book in my_books]
        if book_name.title().strip() in my_book_list:
            for book in my_book_list:
                if book_name.title().strip() != book:
                    # Rewrite the user's book file without the returned book
                    with open(f"{self.name}_books.txt", "w") as my_books:
                        my_books.write(f"{book}\n")

            # Update the library to reflect the returned book
            with open("library_books.txt", "r") as lib_books:
                all_lib_books = [book.title().strip().strip("\n") for book in lib_books]
                with open("library_books.txt", "w") as lib_books:
                    for book in all_lib_books:
                        if book_name.title().strip() in book:
                            lib_books.write(f"{book_name.title().strip()}\n")
                        else:
                            lib_books.write(f"{book}\n")
                    print(f"\n{book_name.title().strip()} is returned to the library.")
        else:
            print("\nYou don't have any book with this name.")
