"""

# ========== Write the code to do the following tasks:

- Create a table called students.
- Insert the following new rows into the students table:
  id  name                grade
  55  Carl Davis          61
  66  Dennis Fredrickson  88
  77  Jane Richards       78
  12  Peyton Sawyer       45
  2   Lucas Brooke        99
- Select all records with a grade between 60 and 80.
- Change Carl Davis’s grade to 65.
- Delete Dennis Fredrickson’s row.
- Change the grade of all people with an id below than 55.

"""

# ==========  Import Libraries ==========
import sqlite3

import sqlite3

# ==========  MAIN LOGIC - Database Manipulation with sqlite3  =============
try:
    # Open or create a file that contains a sqlite3 database.
    # Be sure to create the folder before the time.  
    # <connect> only creates files and not folders.
    db = sqlite3.connect('student_db.db')      # OR connect('data/student_db.db')

    # Get a cursor object to run queries. 
    cursor = db.cursor() 

    # Test if this table exists else create a table called students 
    # with id as the primary key and name must have a value.
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                        students(id INTEGER PRIMARY KEY, 
                                           name TEXT NOT NULL ON CONFLICT IGNORE, 
                                           grade INTEGER)''')
    db.commit()

    # Set the values in a list/tuple.
    python_grades_ = [(55,'Carl Davis',61),(66,'Dennis Fredrickson',88),
                      (77,'Jane Richards',78),(12,'Peyton Sawyer',45),
                      (2,'Lucas Brooke',99)]

    # Insert new rows into the students table. 
    # Replace duplicate key insertions.
    cursor.executemany('''INSERT OR REPLACE INTO students(id, name, grade) 
                       VALUES(?,?,?)''', python_grades_)
    cursor.execute('''SELECT * FROM students''')

    """
    # Inserting a single record 
    # IF AUTOINCREMENT added to PRIMARY KEY table creation.
 
    name = "Andres"
    grade = 60

    # Insert 
    cursor.execute("INSERT INTO student(name, grade) VALUES (?, ?)", 
    (name, grade))

    # Commit the change
    db.commit()

    # ELSE 

    id = 99
    name = "Andres"
    grade = 60

    # Insert 
    cursor.execute("INSERT INTO student(id, name, grade) VALUES (?, ?, ?)", 
                        (id, name, grade))

    # Commit the change
    db.commit()
    """
    cursor.execute('''SELECT * FROM students''')

    print ()
    print ("********* Table after creation and record inserts **********\n")
    for row in cursor:
        print (f"Student: {row[0]} Name: {row[1]} Grade: {row[2]}")
    
    # Select all records with a grade between 60 and 80.
    cursor.execute('''SELECT * FROM students 
                        WHERE grade BETWEEN ? AND ?''', (60, 80))

    # Display the rows in the select result.
    print ()
    print ("********* Records with a grade between 60 and 80 **********\n")
    for row in cursor:
        print (f"Student: {row[0]} Name: {row[1]} Grade: {row[2]}")

    # Change Carl Davis’s grade to 65.
    cursor.execute('''UPDATE students SET grade = ? 
                   WHERE name = ? ''', (65, 'Carl Davis'))
    db.commit()

    # Display update result for Charl Davis.
    cursor.execute('''SELECT * FROM students 
                        WHERE name = ?''', ('Carl Davis',))

    # Though there is only 1 record here to display and the function 
    # fetchone() could have been used, I chose to use the -for row in cursor- 
    # option as to be consistant with the display format. 
    print ()
    print ("********* Updated record for Charl Davis **********\n")
    for row in cursor:
        print (f"Student: {row[0]} Name: {row[1]} Grade: {row[2]}")

    # Delete Dennis Fredrickson’s row.
    # Note the , in (id,) when only 1 ? in query
    cursor.execute('''DELETE FROM students WHERE name = ? ''', 
                   ('Dennis Fredrickson',))
    db.commit()

    # Table after deleting Denis Fredrickson.
    cursor.execute('''SELECT * FROM students''')
    
    print ()
    print ("********* Table after deleting Dennis Fredrickson **********\n")
    for row in cursor:
        print (f"Student: {row[0]} Name: {row[1]} Grade: {row[2]}")
    
    # Change the grade of all people with an id below than 55.
    # As we can see this instruction does not make sense.  Let's rephrase into 
    # something logical. We will change the grade of all people with an 
    # id below 55; change grade to 80.
    cursor.execute('''UPDATE students SET grade = ? 
                   WHERE id < ? ''', (80, 55))
    db.commit()

    # Table after updating grade to 80 for all with id < 55.
    cursor.execute('''SELECT * FROM students''')
    
    print ()
    print ("********* Grade changed to 80 for IDs less than 55 **********\n")
    for row in cursor:
        print (f"Student: {row[0]} Name: {row[1]} Grade: {row[2]}")

    print ()
# Catch the exception
except Exception as error_msg:
    # Roll back any change if something goes wrong.
    db.rollback()
    raise error_msg

finally:
    # Close the db connection
    db.close()

# =============================
# Just like file handling, we can use the `with` statement 
# to handle the state of the db connection for us.
"""
Instead of 
db = sqlite3.connect('student_db')  
and
db.close()
use
with sqlite3.connect('student_db.db') as db:  
"""
with sqlite3.connect('student_db.db') as db:   

    result = db.cursor().execute("SELECT * FROM students")
    print(result.fetchall())
