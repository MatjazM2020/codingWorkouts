(select
u.name as results
from
(select
user_id,
count(user_id) as n
from 
MovieRating
group by user_id) as w
join 
Users as u 
on u.user_id = w.user_id 
order by n desc, name asc
limit 1
)

union all

(select 
title 
from 
(select 
movie_id, 
avg(rating) as r
from MovieRating 
where month(created_at) = 2 and year(created_at) = 2020
group by movie_id
) as q
join 
Movies as m
on m.movie_id = q.movie_id 
order by q.r desc, title asc 
limit 1) 


/* 
problem: https://leetcode.com/problems/movie-rating/description/?envType=study-plan-v2&envId=top-sql-50

Table: Movies

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table.
title is the name of the movie.
 

Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
 

Table: MovieRating

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user's review date. 
 

Write a solution to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.

*/ 