
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return (
            f"Book Name: {self.title}\n"
            f"Author Name: {self.author}\n"
            f"Book ID: {self.book_id}\n"
            f"Status: {status}"
        )


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return (
            f"Member Name: {self.name} || Member ID: {self.member_id}"
        )


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_books(self, book):
        if any(b.book_id == book.book_id for b in self.books):
            print("A book with this ID already exists.")
            return

        self.books.append(book)
        print("Book added to the library.")

    def add_member(self, member):
        if any(m.member_id == member.member_id for m in self.members):
            print("Member with same ID exists.")
            return

        self.members.append(member)
        print("Member registered.")

    def show_book(self):
        if not self.books:
            print("No books in library.")
            return

        for book in self.books:
            print(book)
            print("-" * 30)

    def show_members(self):
        if not self.members:
            print("No members registered yet.")
            return

        for member in self.members:
            print(member)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if book is None:
            print("Book not found.")
            return

        if member is None:
            print("Member not found.")
            return

        if not book.is_available:
            print("Book is already borrowed.")
            return

        book.is_available = False
        member.borrowed_books.append(book)
        print(f"{book.title} borrowed successfully.")

    def return_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if book is None:
            print("Book not found.")
            return

        if member is None:
            print("Member not found.")
            return

        if book not in member.borrowed_books:
            print("This member has not borrowed this book.")
            return

        member.borrowed_books.remove(book)
        book.is_available = True
        print(f"{book.title} returned successfully.")

    def show_borrowed_books(self, member_id):
        member = self.find_member(member_id)

        if member is None:
            print("Member not found.")
            return

        if not member.borrowed_books:
            print("This member has no borrowed books.")
            return

        print(f"Books borrowed by: {member.name}:")
        for book in member.borrowed_books:
            print(f"{book.title} (ID: {book.book_id})")


def main():
    library = Library()

    while True:
        print("\n=== Library Management System ===")
        print("1. Add book")
        print("2. Register member")
        print("3. Show all books")
        print("4. Show all members")
        print("5. Borrow book")
        print("6. Return book")
        print("7. Show a member's borrowed books")
        print("8. Exit")

        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 8.")
            continue

        match option:
            case 1:
                title = input("Book Name: ").strip()
                author = input("Author: ").strip()
                book_id = input("Book ID: ").strip()

                if not title or not author or not book_id:
                    print("Book name, author, and ID cannot be empty.")
                    continue

                library.add_books(Book(title, author, book_id))

            case 2:
                name = input("Name: ").strip()
                member_id = input("Member ID: ").strip()

                if not name or not member_id:
                    print("Name and member ID cannot be empty.")
                    continue

                library.add_member(Member(name, member_id))

            case 3:
                library.show_book()

            case 4:
                library.show_members()

            case 5:
                book_id = input("Book ID: ").strip()
                member_id = input("Member ID: ").strip()
                library.borrow_book(book_id, member_id)

            case 6:
                book_id = input("Book ID: ").strip()
                member_id = input("Member ID: ").strip()
                library.return_book(book_id, member_id)

            case 7:
                member_id = input("Member ID: ").strip()
                print("-" * 15)
                library.show_borrowed_books(member_id)
                print("-" * 15)

            case 8:
                print("Thank you for using the library.")
                break

            case _:
                print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
