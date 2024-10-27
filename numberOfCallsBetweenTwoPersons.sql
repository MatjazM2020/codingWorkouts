select person1, person2, count(person1) call_count, sum(duration) total_duration 
from 
(select 
    case when from_id < to_id then from_id else to_id end person1
    , case when from_id < to_id then to_id else from_id end person2
    , duration 
from Calls) x
group by person1, person2




/*
https://leetcode.com/problems/number-of-calls-between-two-persons/description/?envType=study-plan-v2&envId=premium-sql-50

Table: Calls

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| from_id     | int     |
| to_id       | int     |
| duration    | int     |
+-------------+---------+
This table does not have a primary key (column with unique values), it may contain duplicates.
This table contains the duration of a phone call between from_id and to_id.
from_id != to_id
 

Write a solution to report the number of calls and the total call duration between each pair of distinct persons (person1, person2) where person1 < person2.

Return the result table in any order.

Input: 
Calls table:
+---------+-------+----------+
| from_id | to_id | duration |
+---------+-------+----------+
| 1       | 2     | 59       |
| 2       | 1     | 11       |
| 1       | 3     | 20       |
| 3       | 4     | 100      |
| 3       | 4     | 200      |
| 3       | 4     | 200      |
| 4       | 3     | 499      |
+---------+-------+----------+
Output: 
+---------+---------+------------+----------------+
| person1 | person2 | call_count | total_duration |
+---------+---------+------------+----------------+
| 1       | 2       | 2          | 70             |
| 1       | 3       | 1          | 20             |
| 3       | 4       | 4          | 999            |
+---------+---------+------------+----------------+

*/