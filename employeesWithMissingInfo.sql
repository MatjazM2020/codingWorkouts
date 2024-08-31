with temp as
(select e.employee_id
from Employees e
left join Salaries s on e.employee_id = s.employee_id
where s.employee_id is null 
union
select s.employee_id
from Employees e
right join Salaries s on e.employee_id = s.employee_id
where e.employee_id is null) 
select employee_id
from temp
order by employee_id asc



/*
https://leetcode.com/problems/employees-with-missing-information/description/

Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
employee_id is the column with unique values for this table.
Each row of this table indicates the name of the employee whose ID is employee_id.
 

Table: Salaries

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| salary      | int     |
+-------------+---------+
employee_id is the column with unique values for this table.
Each row of this table indicates the salary of the employee whose ID is employee_id.
 

Write a solution to report the IDs of all the employees with missing information. The information of an employee is missing if:

The employee's name is missing, or
The employee's salary is missing.
Return the result table ordered by employee_id in ascending order.

The result format is in the following example.

*/
