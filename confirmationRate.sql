select 
u.user_id,
coalesce(confirmation_rate,0) as confirmation_rate
from
(select distinct user_id
from 
Signups) as u
left join 
(select 
d.user_id,
case 
  when sm = 0 then 0 
  else round(f.counts/sm,2)
end as confirmation_rate
from
(select
user_id,
sum(counts) as sm
from
(select 
q.user_id, 
q.action, 
coalesce(counted,0) as counts
from
(select distinct Signups.user_id, action
from 
Confirmations
cross join 
Signups) as q
left join 
(select 
user_id, 
action, 
count(action) as counted
from Confirmations
group by 
user_id, 
action) as w
on q.user_id = w.user_id and q.action = w.action) as a
group by user_id) as d

join 

(select 
user_id, 
action, 
counts
from
(select 
q.user_id, 
q.action, 
coalesce(counted,0) as counts
from
(select distinct Signups.user_id, action
from 
Confirmations
cross join 
Signups) as q
left join 
(select 
user_id, 
action, 
count(action) as counted
from Confirmations
group by 
user_id, 
action) as w
on q.user_id = w.user_id and q.action = w.action) as r
where action = 'confirmed') as f
on d.user_id = f.user_id) as n
on u.user_id = n.user_id
order by confirmation_rate

/*
Excercise: https://leetcode.com/problems/confirmation-rate/?envType=study-plan-v2&envId=top-sql-50

table: Signups 
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
user_id is the column of unique values for this table.
Each row contains information about the signup time for the user with ID user_id.

table: Confirmations 
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
| action         | ENUM     |
+----------------+----------+
(user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
user_id is a foreign key (reference column) to the Signups table.
action is an ENUM (category) of the type ('confirmed', 'timeout')
Each row of this table indicates that the user with ID user_id requested a confirmation message at
time_stamp and that confirmation message was either confirmed ('confirmed') or expired without confirming ('timeout').


The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested 
confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0.
 Round the confirmation rate to two decimal places. Write a solution to find the confirmation rate of each user.
Return the result table in any order.
*/

