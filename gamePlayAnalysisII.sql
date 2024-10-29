with x as (select
    player_id
    , min(event_date) event_date
from Activity
group by player_id)
select 
    a.player_id
    , device_id
from Activity a
inner join x on a.player_id = x.player_id and a.event_date = x.event_date





/*
https://leetcode.com/problems/game-play-analysis-ii/description/?envType=study-plan-v2&envId=premium-sql-50


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
 

Write a solution to report the device that is first logged in for each player.

Return the result table in any order.
*/