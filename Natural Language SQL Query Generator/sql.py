import sqlite3

# Connect to the SQLite database named 'student.db'.
# If 'student.db' does not exist, SQLite will create it automatically.
connection = sqlite3.connect('student.db')

# Create a cursor object to execute SQL commands and interact with the database.
cursor = connection.cursor()

# Define the SQL statement for creating a new table named STUDENT.
# The table will have four columns:
# - NAME: Stores the student's name (VARCHAR, max 25 characters).
# - CLASS: Stores the class name (VARCHAR, max 25 characters).
# - SECTION: Stores the section name (VARCHAR, max 25 characters).
# - MARKS: Stores the student's marks (INTEGER).
table_info = '''
CREATE TABLE STUDENT(
    NAME VARCHAR(25), 
    CLASS VARCHAR(25), 
    SECTION VARCHAR(25), 
    MARKS INT
);
'''

# Execute the table creation statement.
# This will create the STUDENT table if it doesn't already exist.
cursor.execute(table_info)

# Insert records into the STUDENT table with sample student data.
# Each INSERT statement adds a new row with the following values:
# - NAME, CLASS, SECTION, and MARKS for each student.
cursor.execute('''INSERT INTO STUDENT VALUES('Ali', 'Data Structure', 'A', 0)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Usman', 'Data Science', 'B', 100)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Bilal', 'DEVOPS', 'A', 60)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Akram', 'DEVOPS', 'B', 80)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Ahmad', 'Data Science', 'A', 70)''')

# Retrieve and display all records from the STUDENT table.
print("The inserted records are:")

# Execute a SELECT statement to fetch all rows from the STUDENT table.
data = cursor.execute('''SELECT * FROM STUDENT''')

# Loop through each row in the result set and print it.
for row in data:
    print(row)

# Commit the transaction to save any changes made to the database.
connection.commit()

# Close the database connection to free resources.
connection.close()
