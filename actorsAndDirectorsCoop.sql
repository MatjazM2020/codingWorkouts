with cte as (select
actor_id,
director_id,
count(*) c
from 
ActorDirector
group by actor_id, director_id) 

select actor_id, director_id from cte where c >= 3



/* 
https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/description/


Table: ActorDirector

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
timestamp is the primary key (column with unique values) for this table.
 

Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

Return the result table in any order.

*/ 