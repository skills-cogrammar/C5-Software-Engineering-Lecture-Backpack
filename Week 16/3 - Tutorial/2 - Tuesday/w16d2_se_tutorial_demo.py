#------------------------------------------------------------------------------------------------
# - Create a program that can be used by a bookstore clerk. The program should allow the clerk to:
#   * add new books to the database
#   * update book information
#   * delete books from the database
#   * search the table to find a specific book.
# 
# - Create a database called bookstore and a table called books. The table can have the following structure:
#   id      Title                                       Author              Qty
#   3001    A Tale of Two Cities                        Charles Dickens     30
#   3002    Harry Potter and the Philosopher's Stone    J.K. Rowling        40
#   3003    The Lion, the Witch and the Wardrobe        C. S. Lewis         25
#   3004    The Lord of the Rings                       J.R.R Tolkien       37
#   3005    Alice in Wonderland                         Lewis Carroll       12
#
# - Populate the table with the above values. You can also add your own values if you wish.
# - The program should present the user with the following menu:
#       1. Enter book
#       2. Update book
#       3. Delete book
#       4. Search books
#       0. Exit
#
# - The program should perform the function that the user selects. The implementation of these functions 
#   is left up to you, but a demonstration of the topics we have covered in the last module should be shown.
#
#   ===  Remember that this can be changed for any stock management functionality.
#   ===  You can also incorporate some of the Task Manager concepts

#===================================== Libraries =====================================
# Tabulate function allows us to print records in table format.
from tabulate import tabulate
# Import to allow Python to run SQL Queries.
import sqlite3

#===================================== Functions =====================================
def access_tbl():
    '''
    This function will create the books table if it does not exist.
    '''
    print("===> Access books table")
    try: 
        cursor = db.cursor() 
        # Test if this table exists else create a table called books_tbl with id as the primary key,
        # and Title must have a value.
        cursor.execute('''CREATE TABLE IF NOT EXISTS
                            books_tbl(id INTEGER PRIMARY KEY, 
                                    title TEXT NOT NULL ON CONFLICT IGNORE, 
                                    author TEXT,
                                    qty INTEGER)''')
        db.commit()
# Catch  exception for CREATE TABLE errors.
    except Exception as error_msg:
        db.rollback()
        print()
        print(f"--> Create Table: {error_msg} ...\n")
        exit()
#===================================== End access_tbl() =====================================


def pop_tbl():
    '''
    This function will populate the books table with initial records read from file inventory_reset.txt
    '''
    print("===> Populate the books table")
    '''
    Read in each line of the inventory_reset.txt and move it into a tuple and insert the 
    info into the books_tbl.
    '''

#===================================== End pop_tbl() =====================================


def view_all_books():
    '''
    This function will select all the records in the table and display them with a break continue flow.
    '''
    cursor = db.cursor() 

    # Display all the books in the table.
    try:
        cursor.execute('''SELECT * FROM books_tbl''')
        results = cursor.fetchall()
        # To display 5 records at a time, set View_pause_int = 5.
        view_pause_int = 5
 
        if len(results) > 0:
            print()
            print("=========================== Books in the eBookStore ===========================\n")
            # book_tbl_nlst is a nested list with first instance being the headers for our table.
            book_tbl_nlst = [["Id", "Title", "Author", "Quantity"]]

            for row_num, row in enumerate(results):
                table_row = (row[0], row[1], row[2], row[3])
                book_tbl_nlst.append(table_row)

                # Pause the view for every {view_pause_int} rows so it does not run off the screen. 
                # This can easily be adjusted to 10 (change view_pause_int value) depending on the screen conditions.
                # We are not showing continuation option or doing the below if-statement if our
                # last record is on a multiple of {view_pause_int} display.
                if (row_num+1) % view_pause_int == 0 and (row_num+1) != len(results):
                    # Calculate start of display.
                    view_start_int = (row_num + 1) - (view_pause_int - 1)
                    print(tabulate(book_tbl_nlst, headers = 'firstrow'))
                    print(f"================================= Books {view_start_int} to {row_num + 1} =================================")
                    # reset book_tbl_nlst with first instance being the headers for our next screen display.
                    book_tbl_nlst = [["Id", "Title", "Author", "Quantity"]]
                    print()
                    go_response = input("<Enter> for next rows or type M to return to Menu: ").lower()
                    print()

                    if go_response == 'm':
                        break
                
                # When the last display is less than or exactly 5 rows, display the last books with this if statement.
                if row_num == (len(results)-1):
                    # Calculate start of display.
                    # For this one we calculate the last record displayed and then add 1 for start of next display.
                    view_start_int = ((row_num + 1) - ((row_num + 1) % view_pause_int)) + 1    
                    print(tabulate(book_tbl_nlst, headers = 'firstrow'))
                    print(f"================================= Books {view_start_int} to {row_num + 1} =================================")
        
        else:
            # if no records were found with the SELECT * statement, then display below message.
            print()
            print("--> There are no books listed in the ebookstore!")
            print("--> Use Menu Option 6 to load default inventory!")

    # Catch  exception errors for the SELECT * query or the fetchall()
    except Exception as error_msg:
        print(f"--> read_all_books: {error_msg} ...\n")
#===================================== End read_all_books() =====================================


def capture_book():
    '''
    This function will allow the user to capture new books.
    '''
    '''
    Request info from user and validate info. Then insert into database.
    Check for duplications.
    '''
    print("===> Capture book")    
#===================================== End capture_book() =====================================


def update_book():
    '''
    This function will allow the user to update the data on a book, like the quantity available or 
    typing errors on the title or author.
    '''
    '''
    Create another submenu

    '''
    print("===> Update book")

#===================================== End update_tbl() =====================================


def delete_book():
    '''
    This function will allow a user to remove a book from the table. We will use the Id to 
    remove an item and this can be found with a view all or search function.
    '''
    ''' Select record first to see if it exists and then delete with appropriate msg.'''
    print("===> Delete book")

#===================================== End delete_book() =====================================


def search_book():
    '''
     This function will search for a book from the table using the book id, title, author or limited stock.
    '''

    print("===> Search books")

    # Create a menu that chooses the search method.
    # Initialise menu option variable with any value outside of menu options.
    sub_menu_int = 10

    # Repeat search options until user exit the menu with integer 0 input.
    while sub_menu_int != 0:
        valid_option = False
        # Display search submenu until user input valid option.
        while not valid_option:
            # Use try: except: to catch menu option error.
            try: 
                print()
                print("=============== Search MENU ==================")
                print("1. Search by Id")
                print("2. Search by Title")
                print("3. Search by Author")
                print("4. Search for limited stock")
                print("0. Exit Search")
                print("==============================================\n")
                sub_menu_int = int(input("Please choose a menu option (e.g. 0 to 4) > "))
                
                if sub_menu_int >= 0 and sub_menu_int < 5:
                    valid_option = True
                else:
                    print("--> That was not a valid option. Please try again ...")
    
            # Catch exception for when input is not integer.
            except ValueError:
                print("--> That was not a valid option. Please try again ...")

        cursor = db.cursor()    

        # Sub-Menu option to search by title.
        """
        elif sub_menu_int == 2: # book_ttl  
            print()
            book_ttl = input("Enter a title for your search - partials also ok: ")

            # If the user input is not blank.
            if book_ttl != "":
                try:
                    # Search for Title
                    cursor.execute('''SELECT * FROM books_tbl 
                                        WHERE title LIKE ?''', ('%{}%'.format(book_ttl),))
                    results = cursor.fetchall()

                    # If we found at least 1 record.
                    if len(results) > 0:
                        print()
                        print("======================== Title Search in the eBookStore ========================\n")
                        # book_tbl_nlst is a nested list with first instance being the headers for our table.
                        book_tbl_nlst = [["Id", "Title", "Author", "Quantity"]]

                        # Run through the instances and enter them into the display list.
                        for row in result:
                            table_row = (row[0], row[1], row[2], row[3])
                            book_tbl_nlst.append(table_row)

                        print(tabulate(book_tbl_nlst, headers = 'firstrow'))
                        print("===============================================================================")
                    else:
                        print(f"--> No titles containing >{book_ttl}< in the ebookstore!\n")

                # Catch the exception for SELECT * and fetchall errors.
                except Exception as error_msg:
                    print(f"--> Search Title: {error_msg} ...\n")

            else:
                print("--> You did not enter any characters ...")   
            """     
#===================================== End search_book() =====================================


def reset_books_tbl():
    '''
     This function will reset the books table by removing all records and loading the records in the inventory_reset.txt file.
    '''
    cursor = db.cursor()    

    try:
        # Remove all rows in the books table.
        cursor.execute('''DELETE FROM books_tbl''')
        db.commit()
        pop_tbl()
    # Catch the exception for DELETE.
    except Exception as error_msg:
        # Roll back any change if something goes wrong.
        db.rollback()
        print()
        print(f"--> reset_books_tbl: {error_msg} ...")    
#===================================== End reset_books_tbl() =====================================

# ============  MAIN LOGIC - eBookStore Management  ===============

# Open or create a file that contains a sqlite3 database.
# Be sure to create any folder you want to place the database file in, before the time. 
# The sqlite3.connect only creates files and not folders.
try:
    db = sqlite3.connect('ebookstore_db')
except Exception as error_msg:
    print()
    print(f"--> Connect db: {error_msg} ...\n")
    exit()

# Make sure the table exists.
access_tbl()

# ------> For no books in eBookStore, choose menu option 6 to load initial inventory list.

#====================== Main Menu ======================
# Create a menu that executes each function above.
# Initialise menu option variable with any value outside of menu options.
menu_int = 10

while menu_int != 0:

    valid_option = False
    # Display bookstore menu until valid option is chosen.
    while not valid_option:
        # Use try: except: to catch menu option error.
        try: 
            print()
            print("========================== Bookstore MENU ==========================")
            print("1. View Books")
            print("2. Capture new book")
            print("3. Update details for a book")
            print("4. Remove a book")
            print("5. Search a book")
            print("6. Load/Reload database with default inventory list (Take Caution!)")
            print("0. Exit Program")
            print("====================================================================\n")

            menu_int = int(input("Please choose a menu option (e.g. 0 to 6) > "))

            # If the user entered an available menu integer option then exit the while not valid_option:
            if menu_int >= 0 and menu_int <= 6:
                valid_option = True
            else:
                print("--> That was not a valid option. Please try again ...")
    
        # Catch the exception for an input that is not integer.
        except ValueError:
            print("--> That was not a valid option. Please try again ...")

#====================== End Main Menu ======================

#==================== Menu Options Logic ===================   

    # Menu option to view the books.
    if menu_int == 1:
        view_all_books()

    # Menu option to capture a new book.
    elif menu_int == 2:
        capture_book()

    # Menu option to update details for a book.
    elif menu_int == 3:
        update_book()

    # Menu option to remove a book from the system.
    elif menu_int == 4:
        delete_book()

    # Menu option to search for a book.
    elif menu_int == 5:
        search_book()

    # Menu option to reset the database.
    elif menu_int == 6:
        print()
        print("--> This will remove all books and load books from the inventory_reset.txt file.")
        print("--> Make sure the inventory_reset.txt file is in the same folder as the *.py file.\n")

        valid_reset = False
        # Repeat input request until input first character is upper or lower case y or n. 
        while not valid_reset:
            reset_opt = input("---> Are you sure you want to reset the ebookstore books list? (Answer Y or N) > ").lower()

            if reset_opt == "": # Input is None.
                reset_opt = " "

            if reset_opt [0] == 'y':
                reset_books_tbl()
                valid_reset = True
            elif reset_opt [0] == "n":
                print()
                print("--> Back to Main Menu without resetting the ebookstore books list!")
                valid_reset = True
            else: 
                print()
                print("--> Invalid input.")

    elif menu_int == 0:
        # Close the db connection
        db.close()
        print()
        print("Goodbye!\n")

# =================  END PROGRAM LOGIC HERE  ====================