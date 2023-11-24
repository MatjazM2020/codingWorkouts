select
accepter_id as id,
sum(n) as num
from
((select 
accepter_id, 
count(*) as n 
from RequestAccepted
group by accepter_id 
) 
union all
(select 
requester_id, 
count(*) as n2 
from RequestAccepted
group by requester_id 
)) as w
group by accepter_id
order by num desc
limit 1 



/* 
problem: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/?envType=study-plan-v2&envId=top-sql-50
Table: RequestAccepted

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
 

Write a solution to find the people who have the most friends and the most friends number.

The test cases are generated so that only one person has the most friends.

*/ 
