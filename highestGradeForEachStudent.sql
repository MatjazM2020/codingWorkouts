with cte as (select
    student_id
    , max(grade) max_grade
from Enrollments
group by student_id)
select
    crs.student_id
    , min(course_id) course_id
    , crs.max_grade grade
from Enrollments e
inner join cte crs on crs.student_id = e.student_id and crs.max_grade = e.grade
group by student_id, grade
order by student_id asc




/*
https://leetcode.com/problems/highest-grade-for-each-student/description/?envType=study-plan-v2&envId=premium-sql-50

Table: Enrollments

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| course_id     | int     |
| grade         | int     |
+---------------+---------+
(student_id, course_id) is the primary key (combination of columns with unique values) of this table.
grade is never NULL.
 

Write a solution to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest course_id.

Return the result table ordered by student_id in ascending order.

The result format is in the following example.
*/