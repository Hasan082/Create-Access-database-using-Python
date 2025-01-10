import sqlite3

# CREATE A DATABASE
conn = sqlite3.connect('instructor.db')
cursor_obj = conn.cursor()

# DROP TABLE IF EXIST
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")
# CREATE TABLE SQL QUERY
table = """
CREATE TABLE IF NOT EXISTS INSTRUCTOR (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    FNAME VARCHAR(30) NOT NULL,
    LNAME VARCHAR(30) NOT NULL,
    CITY VARCHAR(30),
    CCODE CHAR(2)
);
"""
# Execute the SQL statement using the cursor object
cursor_obj.execute(table)

# push data to database
insert_data = """INSERT INTO INSTRUCTOR (FNAME, LNAME, CITY, CCODE) VALUES ('Md', 'Hasan' , 'Pangsha', '10'), ('Mollika', 'Mukta' , 'Lakmoni', 
'11'), ('Faria', 'Maahi' , 'Dhaka', '12');"""
cursor_obj.execute(insert_data)

# Commit the changes (important for data integrity)
conn.commit()
# Close the connection
conn.close()
