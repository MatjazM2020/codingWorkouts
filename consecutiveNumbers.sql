with threeConsecutive as (
    select 
    num, 
    lag(num) over (order by id) as prev,
    lead(num) over (order by id) as next
    from 
    Logs
)
select 
distinct num as ConsecutiveNums
from threeConsecutive
where num = prev and num = next




/*

problem: https://leetcode.com/problems/consecutive-numbers/description/?envType=study-plan-v2&envId=top-sql-50

Table: Logs
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column.
 

Find all numbers that appear at least three times consecutively.

Return the result table in any order.
*/ 