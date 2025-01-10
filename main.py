import sqlite3

# CREATE A DATABASE
conn = sqlite3.connect('instructor.db')
cursor_obj = conn.cursor()

# DROP TABLE IF EXIST
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")
# CREATE TABLE SQL QUERY
table = """
CREATE TABLE IF NOT EXISTS INSTRUCTOR (
    ID INTEGER PRIMARY KEY NOT NULL,
    FNAME VARCHAR(30) NOT NULL,
    LNAME VARCHAR(30) NOT NULL,
    CITY VARCHAR(30),
    CCODE CHAR(2)
);
"""
# PASS QUERY TO EXECUTE
cursor_obj.execute(table)
conn.commit()
conn.close()
