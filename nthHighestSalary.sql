CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
       select salary from
       (select 
            id
            , salary
            , dense_rank() over (order by salary desc) rn
       from Employee
       ) s
       where rn = N
       group by rn
  );
END



/*
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest salary from the Employee table. If there
 is no nth highest salary, return null.

The result format is in the following example.


*/