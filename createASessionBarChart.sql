with base as (
    select '[0-5>' bin , 0 total
    union
    select '[5-10>' bin , 0 total
    union
    select '[10-15>' bin , 0 total
    union 
    select '15 or more' bin , 0 total
)
select
    base.bin
    , count(x.bin) total
from
    (select
        case
            when duration/60 < 5 then '[0-5>'
            when duration/60 < 10 then '[5-10>'
            when duration/60 < 15 then '[10-15>'
            else '15 or more'
        end bin
    from Sessions) x
right join base on x.bin = base.bin
group by bin



/*
https://leetcode.com/problems/create-a-session-bar-chart/description/


Table: Sessions

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| session_id          | int     |
| duration            | int     |
+---------------------+---------+
session_id is the column of unique values for this table.
duration is the time in seconds that a user has visited the application.
 

You want to know how long a user visits your application. You decided to create bins of "[0-5>", "[5-10>", "[10-15>", and "15 minutes or more" and count the number of sessions on it.

Write a solution to report the (bin, total).

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Sessions table:
+-------------+---------------+
| session_id  | duration      |
+-------------+---------------+
| 1           | 30            |
| 2           | 199           |
| 3           | 299           |
| 4           | 580           |
| 5           | 1000          |
+-------------+---------------+
Output: 
+--------------+--------------+
| bin          | total        |
+--------------+--------------+
| [0-5>        | 3            |
| [5-10>       | 1            |
| [10-15>      | 0            |
| 15 or more   | 1            |
+--------------+--------------+
Explanation: 
For session_id 1, 2, and 3 have a duration greater or equal than 0 minutes and less than 5 minutes.
For session_id 4 has a duration greater or equal than 5 minutes and less than 10 minutes.
There is no session with a duration greater than or equal to 10 minutes and less than 15 minutes.
For session_id 5 has a duration greater than or equal to 15 minutes.
*/