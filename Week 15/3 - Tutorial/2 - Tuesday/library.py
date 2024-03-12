class Library:

    def __init__(self, member_list):
        self.__member_list = member_list
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        self.__books.remove(book)

    def remove_book_by_index(self, index):
        self.__books.pop(index)

    def view_books(self):
        for i, book in enumerate(self.__books):
            print(i, book)

    def search_book(self, book_title):
        for book in self.__books:
            if book.get_title() == book_title:
                return book
        else:
            print(f"{book_title} not found!")

    def __getitem__(self, index):
        return self.__books[index]
    
    def get_members_list(self):
        return self.__member_list

    