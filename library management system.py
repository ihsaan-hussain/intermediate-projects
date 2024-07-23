class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies
    
    @classmethod
    def from_dict(cls, book_dict):
        return cls(
            title=book_dict['title'],
            author=book_dict['author'],
            isbn=book_dict['isbn'],
            available_copies=book_dict['available_copies']
        )
    
    @staticmethod
    def is_valid_isbn(isbn):
        # A simple ISBN validation (length check)
        return len(isbn) in [10, 13]

class Member:
    def __init__(self, name, member_id, borrowed_books=None):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
    
    @classmethod
    def from_dict(cls, member_dict):
        return cls(
            name=member_dict['name'],
            member_id=member_dict['member_id'],
            borrowed_books=member_dict.get('borrowed_books', [])
        )
    
    @staticmethod
    def is_valid_member_id(member_id):
        # A simple member ID validation (starts with 'M' and followed by digits)
        return member_id.startswith('M') and member_id[1:].isdigit()

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    @classmethod
    def add_book_from_dict(cls, book_dict):
        book = Book.from_dict(book_dict)
        cls.books.append(book)
    
    @staticmethod
    def generate_member_id():
        import random
        return f"M{random.randint(10000, 99999)}"
    
    def add_book(self, book):
        if Book.is_valid_isbn(book.isbn):
            self.books.append(book)
        else:
            print("Invalid ISBN.")
    
    def add_member(self, member):
        if Member.is_valid_member_id(member.member_id):
            self.members.append(member)
        else:
            print("Invalid Member ID.")
    
    def borrow_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        
        if member and book and book.available_copies > 0:
            member.borrowed_books.append(book.title)
            book.available_copies -= 1
            print(f"{member.name} borrowed {book.title}.")
        else:
            print("Cannot borrow book.")
    
    def return_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        
        if member and book and book.title in member.borrowed_books:
            member.borrowed_books.remove(book.title)
            book.available_copies += 1
            print(f"{member.name} returned {book.title}.")
        else:
            print("Cannot return book.")
    
    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available Copies: {book.available_copies}")
    
    def display_members(self):
        for member in self.members:
            print(f"Name: {member.name}, Member ID: {member.member_id}, Borrowed Books: {', '.join(member.borrowed_books)}")

# Example usage:
library = Library()

# Add a book from dictionary
book_dict = {
    'title': 'The Great Gatsby',
    'author': 'F. Scott Fitzgerald',
    'isbn': '9780743273565',
    'available_copies': 5
}
library.add_book(Book.from_dict(book_dict))

# Add a member from dictionary
member_dict = {
    'name': 'John Doe',
    'member_id': 'M12345',
    'borrowed_books': []
}
library.add_member(Member.from_dict(member_dict))

# Borrow a book
library.borrow_book('M12345', '9780743273565')

# Display all books
library.display_books()

# Display all members
library.display_members()

# Return a book
library.return_book('M12345', '9780743273565')

# Display all books again
library.display_books()

# Display all members again
library.display_members()