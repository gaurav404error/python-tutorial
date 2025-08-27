class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print("Book ID already exists!")
        else:
            self.books[book_id] = Book(book_id, title, author)
            print(f"Book '{title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print(f"\nBooks in {self.name}:")
            for book in self.books.values():
                print(book)

    def issue_book(self, book_id):
        if book_id not in self.books:
            print("Book not found!")
        elif self.books[book_id].is_issued:
            print("Sorry, this book is already issued.")
        else:
            self.books[book_id].is_issued = True
            print(f"You have issued '{self.books[book_id].title}'")

    def return_book(self, book_id):
        if book_id not in self.books:
            print("Book not found!")
        elif not self.books[book_id].is_issued:
            print("This book was not issued.")
        else:
            self.books[book_id].is_issued = False
            print(f"'{self.books[book_id].title}' has been returned successfully!")


# ---------- DEMO ----------
library = Library("Python Public Library")

# Add Books
library.add_book(1, "Python Basics", "Guido van Rossum")
library.add_book(2, "OOP in Python", "Bjarne Stroustrup")
library.add_book(3, "Data Science Handbook", "Jake VanderPlas")

# Display Books
library.display_books()

# Issue Book
library.issue_book(2)
library.issue_book(2)  # Trying again

# Return Book
library.return_book(2)

# Display Books Again
library.display_books()
