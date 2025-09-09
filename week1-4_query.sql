select
    course_id,
    count(student_id) as number_of_students
from
    enrollments
group by
    course_id having count(student_id) > 1