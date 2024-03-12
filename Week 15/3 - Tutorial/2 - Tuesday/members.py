class MemberList:

    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def get_member(self, member_id):
        for member in self.members:
            if member.id == member_id:
                return member
        return None
    
    def display_members(self):
        for i, member in enumerate(self.members):
            print(i, member.name, member.id)


class Member:

    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.is_available():
            book.decrease_quantity(1)
            self.borrowed_books.append(book)
        else:
            print(f"{book.get_title()} is not available")

    def return_book(self, book):
        book.increase_quantity(1)
        self.borrowed_books.remove(book)

    def return_all_book(self):
        for book in self.borrowed_books:
            self.return_book(book)


    def display_borrowed_books(self):
        for i, book in enumerate(self.borrowed_books):
            print(i, book, sep=" - ")

    def get_borrowed_books(self):
        return self.borrowed_books
