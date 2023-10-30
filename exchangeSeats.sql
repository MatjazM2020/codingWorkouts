select 
id,
case 
    when (id mod 2) = 0 then lag(student) over (order by id)
    else coalesce(lead(student) over (order by id),student) 
end as student
from 
Seat 
order by id asc 



/* 
problem: https://leetcode.com/problems/exchange-seats/description/?envType=study-plan-v2&envId=top-sql-50

Table: Seat
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
id is a continuous increment.
 

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

*/ 