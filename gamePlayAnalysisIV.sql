select
round((select 
sum(x)
from
(select 
a.player_id,
sum(case when datediff(event_date, first) = 1 then 1
    else 0
    end) as x
from
(select 
player_id,
min(event_date) as first
from 
Activity
group by player_id) as firstDate
join 
Activity as a 
on a.player_id = firstDate.player_id
group by player_id) as w)
/
(
select 
count(distinct player_id)
from Activity
),2)
as fraction


/*
Table: Activity
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.


Write a solution to report the fraction of players that logged in again on the day after the day they 
first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at 
least two consecutive days starting from their first login date, then divide that number by the total number of players.
*/