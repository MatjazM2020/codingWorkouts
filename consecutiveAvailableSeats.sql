with ids as (select seat_id from
(select 
    seat_id
    , lag(free, 1, 0) over (order by seat_id asc) free_prev
    , free free_this
from Cinema) x
where free_prev = 1 and free_this = 1)
select seat_id - 1 as seat_id
from ids 
union 
select seat_id
from ids
order by seat_id asc


/*
https://leetcode.com/problems/consecutive-available-seats/description/?envType=study-plan-v2&envId=premium-sql-50
Table: Cinema

+-------------+------+
| Column Name | Type |
+-------------+------+
| seat_id     | int  |
| free        | bool |
+-------------+------+
seat_id is an auto-increment column for this table.
Each row of this table indicates whether the ith seat is free or not. 1 means free while 0 means occupied.
 

Find all the consecutive available seats in the cinema.

Return the result table ordered by seat_id in ascending order.

The test cases are generated so that more than two seats are consecutively available.
*/