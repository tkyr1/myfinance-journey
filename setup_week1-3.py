# this script adds course and enrollment data to our database.
import sqlite3

conn = sqlite3.connect('university.db')
c = conn.cursor()

# create a courses table
c.execute('''
    create table if not exists courses (
        course_id text primary key,
        course_name text not null
    )
''')

# create an enrollments table (a "linking" table)
c.execute('''
    create table if not exists enrollments (
        enrollment_id integer primary key,
        student_id integer,
        course_id text,
        foreign key (student_id) references students (id),
        foreign key (course_id) references courses (course_id)
    )
''')

# add some courses
courses_to_add = [
    ('cs101', 'intro to computer science'),
    ('econ101', 'principles of economics'),
    ('phys101', 'fundamentals of physics')
]
c.executemany('insert or ignore into courses values (?,?)', courses_to_add)

# enroll some students in courses
enrollments_to_add = [
    (1, 1, 'cs101'),     # john smith in cs101
    (2, 2, 'cs101'),     # jane doe in cs101
    (3, 2, 'econ101'),   # jane doe in econ101
    (4, 5, 'phys101'),   # david brown in phys101
    (5, 9, 'econ101'),   # chris moore in econ101
    (6, 9, 'phys101')    # chris moore in phys101
]
c.executemany('insert or ignore into enrollments values (?,?,?)', enrollments_to_add)

conn.commit()
conn.close()

print("database 'university.db' has been updated with courses and enrollments.")