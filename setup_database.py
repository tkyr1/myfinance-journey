# this script sets up our sqlite database for week 1-3
import sqlite3

# connect to the database (this will create the file if it doesnt exist)
conn = sqlite3.connect('university.db')

# create a 'cursor' to execute commands
c = conn.cursor()

# create the 'students' table
# triple quotes let us write a multi-line command
c.execute('''
    create table if not exists students (
        id integer primary key,
        student_name text not null,
        grade integer
    )
''')

# some student data to insert
students_to_add = [
    (1, 'john smith', 88),
    (2, 'jane doe', 92),
    (3, 'peter jones', 78),
    (4, 'susan williams', 65),
    (5, 'david brown', 95),
    (6, 'emily davis', 88),
    (7, 'michael miller', 72),
    (8, 'sarah wilson', 89),
    (9, 'chris moore', 99),
    (10, 'jessica taylor', 70)
]

# insert the data into the table
c.executemany('insert or ignore into students values (?,?,?)', students_to_add)

# save (commit) the changes and close the connection
conn.commit()
conn.close()

print("database 'university.db' created and populated successfully.")