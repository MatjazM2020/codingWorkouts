select 
x.student_id,
student_name, 
x.subject_name,
coalesce(number,0) as attended_exams
from
(select
student_id, 
student_name, 
subject_name 
from 
Students
cross join 
Subjects) as x
left join 
(select 
student_id,
subject_name, 
count(subject_name) as number
from 
Examinations
group by 
subject_name, 
student_id
) as y
on x.student_id = y.student_id and 
x.subject_name = y.subject_name 
order by student_id, subject_name

/*
table: Students
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.


table: Subjects
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.

table: Examinations
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.


Write a solution to find the number of times each student attended each exam.
Return the result table ordered by student_id and subject_name.
The result format is in the following example.
*/
