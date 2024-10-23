select 
    e.employee_id
    ,coalesce(p.salary, 0) bonus
from Employees e
left join Employees p on e.employee_id = p.employee_id 
and p.employee_id mod 2 = 1
and not(p.name like 'M%')
order by e.employee_id asc


/*
https://leetcode.com/problems/calculate-special-bonus/description/


Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id is the primary key (column with unique values) for this table.
Each row of this table indicates the employee ID, employee name, and salary.
 

Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.
*/