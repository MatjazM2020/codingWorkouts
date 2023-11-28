select 
coalesce(
    (select 
        salary as SecondHighestSalary
    from
    (select
        dense_rank() over (order by salary desc) as rg,
        salary 
    from Employee 
    ) as t
    where rg = 2
    limit 1
    ), null
) as SecondHighestSalary







/* 
prob: https://leetcode.com/problems/second-highest-salary/description/?envType=study-plan-v2&envId=top-sql-50
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
*/ 