
with x as(select 
    team_id
    , count(team_id) team_size
from Employee
group by team_id)
select 
    e.employee_id
    , team_size
from Employee e
inner join x on x.team_id = e.team_id

/*
https://leetcode.com/problems/find-the-team-size/description/?envType=study-plan-v2&envId=premium-sql-50
Table: Employee

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| employee_id   | int     |
| team_id       | int     |
+---------------+---------+
employee_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID of each employee and their respective team.
 

Write a solution to find the team size of each of the employees.

Return the result table in any order.
*/