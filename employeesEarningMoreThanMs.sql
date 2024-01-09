select 
a.name Employee
from Employee a
join 
Employee e 
on a.managerId = e.id 
where e.salary < a.salary 





/* https://leetcode.com/problems/employees-earning-more-than-their-managers/description/ 

Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

Write a solution to find the employees who earn more than their managers.
*/ 