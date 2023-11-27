select 
    d.name as Department, 
    e.name as Employee,
    e.salary as Salary 
from
    Employee e 
    join 
    Department d
    on e.departmentId = d.id 

where (e.departmentId,e.salary) in 
    (
        select 
             departmentId, salary
        from 
        (
            select 
            departmentId,
            salary,
            dense_rank() over (partition by departmentId order by salary desc) dr
            from 
            Employee
        ) as t
     where dr < 4
)







/*
problem: https://leetcode.com/problems/department-top-three-salaries/description/
Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference column) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of a department and its name.
 

A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write a solution to find the employees who are high earners in each of the departments.

Return the result table in any order.
*/