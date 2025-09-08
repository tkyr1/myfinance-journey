select
    students.student_name,
    courses.course_name
from
    students
inner join
    enrollments on students.id = enrollments.student_id
inner join
    courses on enrollments.course_id = courses.course_id;