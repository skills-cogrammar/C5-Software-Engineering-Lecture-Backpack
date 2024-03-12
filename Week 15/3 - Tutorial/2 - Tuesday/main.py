"""
LIBRARY MANAGER
-   Add Books: Allow librarians to add new books to the library system 
    with details such as title, author, genre, quantity, etc.
-   Update Books: Enable librarians to update existing book details 
    like quantity, availability, etc.
-   Remove Books: Allow librarians to remove books from the library system.
-   Borrow Books: Allow library members to borrow books from the library.
-   Return Books: Enable library members to return borrowed books.
-   View Books: Display the current list of books available in the library.
-   Search Books: Implement a search functionality to find books by title, author, genre, etc.
-   Manage Members: Allow librarians to manage library members, including 
    adding new members and updating member details.
"""
from members import *
from library import Library
from books import Book


def create_book():
    title = input("Please enter the title of the book: ")
    author = input("Please enter the author of the book: ")
    genre = input("Please enter the genre of the book: ")
    quantity = input("Please enter the quantity of the book: ")
    return Book(title, author, genre, quantity)


def get_num_input(prompt):
    user_input = input(prompt)
    if user_input.isdigit():
        return int(user_input)
    else:
        return None


members = MemberList()
members.add_member(Member("Jake", "jake12", "jake@gmail.com"))
members.add_member(Member("Joyce", "joy123", "joyce@gmail.com"))
members.add_member(Member("Ashley", "ashley11", "ash@gmail.com"))
library = Library(members)
library.add_book(Book("To Kill a Mockingbird","Harper Lee","Fiction", 3))
library.add_book(Book("1984","George Orwell","Dystopian Fiction", 2))
library.add_book(Book("The Catcher in the Rye","J.D. Salinger","Coming-of-age Fiction", 3))
library.add_book(Book("Pride and Prejudice","Jane Austen","Romance", 5))
library.add_book(Book("The Great Gatsby","F. Scott Fitzgerald","Classic Literature", 3))

MENU = """1. View Books
2. Add Book
3. Remove Book
4. Update Book
5. Borrow Book
6. Return Book
7. Search Book
8. Manage Members

0. Quit"""

while True:
    print("Please select an option below: ")
    print(MENU)
    user_choice = input(": ")

    if user_choice == "1":
        library.view_books()
        input("Press enter to continue.")

    elif user_choice == "2":
        new_book = create_book()
        library.add_book(new_book)

    elif user_choice == "3":
        print("Please choose a book to remove below: ")
        library.view_books()
        while True:
            user_index = get_num_input(": ")
            if isinstance(user_index, int):
                break
            print("Invalid input.")
        library.remove_book_by_index(user_index)
        print("Book has been removed.")

    # Add option 4
        
    elif user_choice == "5":
        member_id = input("Please enter borrower's member ID: ")
        member = library.get_members_list().get_member(member_id)
        print("Please choose a book to borrow: ")
        library.view_books()
        while True:
            user_index = get_num_input(": ")
            if isinstance(user_index, int):
                break
            print("Invalid input.")
        book = library[user_index]
        member.borrow_book(book)

    elif user_choice == "6":
        member_id = input("Please enter borrower's member ID: ")
        member = library.get_members_list().get_member(member_id)
        member.display_borrowed_books()
        member.return_all_books()
        print(f"All books returned by {member.name}.")

    


