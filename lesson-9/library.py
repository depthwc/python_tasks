class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"
    


class Member:
    MAX_BORROWED_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= Member.MAX_BORROWED_BOOKS:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

    def __str__(self):
        borrowed_titles = ', '.join([book.title for book in self.borrowed_books])
        return f"{self.name} (Borrowed: {borrowed_titles or 'None'})"
    

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException(f"Book '{title}' not found.")

    def borrow_book(self, member_name, title):
        member = self._get_member(member_name)
        book = self.find_book(title)

        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed.")
        
        member.borrow_book(book)
        book.is_borrowed = True
        print(f"{member_name} successfully borrowed '{book.title}'.")

    def return_book(self, member_name, title):
        member = self._get_member(member_name)
        book = self.find_book(title)

        if book in member.borrowed_books:
            member.return_book(book)
            book.is_borrowed = False
            print(f"{member_name} returned '{book.title}'.")
        else:
            print(f"{member_name} did not borrow '{book.title}'.")

    def _get_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        raise ValueError(f"Member '{name}' not found.")

    def list_books(self):
        print("Library Books:")
        for book in self.books:
            print(" -", book)

    def list_members(self):
        print("Library Members:")
        for member in self.members:
            print(" -", member)


            
if __name__ == "__main__":
    library = Library()

    # Adding books
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("Moby Dick", "Herman Melville"))  # added for borrow limit test

    # Adding members
    alice = Member("Alice")
    bob = Member("Bob")
    library.add_member(alice)
    library.add_member(bob)

    # Valid borrow
    library.borrow_book("Alice", "1984")

    # Attempt to borrow already borrowed book
    try:
        library.borrow_book("Bob", "1984")
    except BookAlreadyBorrowedException as e:
        print("Exception:", e)

    # Alice borrows two more books
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "The Great Gatsby")

    # Alice tries to borrow a 4th book that actually exists
    try:
        library.borrow_book("Alice", "Moby Dick")
    except MemberLimitExceededException as e:
        print("Exception:", e)

    # Try to borrow a nonexistent book
    try:
        library.borrow_book("Alice", "Some Book")
    except BookNotFoundException as e:
        print("Exception:", e)

    # Return book and let Bob borrow it
    library.return_book("Alice", "1984")
    library.borrow_book("Bob", "1984")

    # Final status
    library.list_books()
    library.list_members()
