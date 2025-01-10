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

show = """SELECT * FROM INSTRUCTOR;"""
cursor_obj.execute(show)
output_all = cursor_obj.fetchall()
for row in output_all:
    print(row)

# NOW FETCH LIMIT NUMBER OF DATA
cursor_obj.execute(show)
OUTPUT_LIMIT = cursor_obj.fetchmany(2)
print(OUTPUT_LIMIT)

# FETCH FIRST NAME ONLY
f_name_statement = """SELECT FNAME FROM INSTRUCTOR"""
cursor_obj.execute(f_name_statement)
output_all_f_name = cursor_obj.fetchall()
print(output_all_f_name)

# UPDATE ROW VALUE NOW
update_statement = """UPDATE INSTRUCTOR SET CITY='DHAKA' WHERE FNAME='Mollika';"""
cursor_obj.execute(update_statement)

# NOW SHOW UPDATE DATA
cursor_obj.execute(show)
output_all_update = cursor_obj.fetchall()
print(output_all_update)

# Now Retrieve data into Pandas




# Commit the changes (important for data integrity)
conn.commit()
# Close the connection
conn.close()
