# Use `fetchone` method to get a single tuple from the result
id = 12

# Note the , in (id,) when only 1 ? in query
cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
student = cursor.fetchone()

print(student)

# Use `fetchall` method to get all of the results that match our query.
cursor.execute("SELECT name, grade FROM students")
students = cursor.fetchall()

for row in students:
    print(f"Name: {row[0]}, Surname: {row[1]}")

print(students)

# Just like file handling, we can 
# use the `with` statement to handle the state of the db connection for us.
try:
    # Open database connection using context manager
    with sqlite3.connect('students_db.db') as db:
        cursor = db.cursor()

        # Execute some SQL queries that may raise an error
        cursor.execute('SELECT * FROM non_existing_table')
        rows = cursor.fetchall()

except sqlite3.OperationalError as e:
    print("An error occurred:", e)

# The database connection is automatically closed even if an error occurred
    