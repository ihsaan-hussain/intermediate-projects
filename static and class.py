class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
        else:
            print(f'The book {self.title} is currently not available')

    def return_book(self):
        self.available = True
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.borrow()
                print(f"You have borrowed '{title}'.")
                return
        print(f'The book {self.title} is currently not available')

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.return_book()
                print(f"You have returned '{title}'.")
                return
            print(f"The book '{title}' was not borrowed.")
            
    def list_available_books(self):
        available_books = [book for book in self.books if book.available]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)
    
    @classmethod
    def create_with_books(cls, books):
        library = cls()
        for book in books:
            library.add_book(book)
        return library

    @staticmethod
    def is_book_available(book):
        return book.available

if __name__ == "__main__":
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    library = Library.create_with_books([book1, book2, book3])

    print("Available books:")
    library.list_available_books()

    library.borrow_book("1984")

    print("\nAvailable books after borrowing '1984':")
    library.list_available_books()

    library.return_book("1984")

    print("\nAvailable books after returning '1984':")
    library.list_available_books()

    print("\nIs '1984' available?")
    print(Library.is_book_available(book1))