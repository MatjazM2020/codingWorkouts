select 
    distinct title TITLE
from Content c
inner join TVProgram tvp on tvp.content_id = c.content_id
where Kids_content = 'Y' and month(program_date) = 6 and year(program_date) = 2020
and content_type = 'Movies'


/*
https://leetcode.com/problems/friendly-movies-streamed-last-month/description/?envType=study-plan-v2&envId=premium-sql-50
Table: TVProgram

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| program_date  | date    |
| content_id    | int     |
| channel       | varchar |
+---------------+---------+
(program_date, content_id) is the primary key (combination of columns with unique values) for this table.
This table contains information of the programs on the TV.
content_id is the id of the program in some channel on the TV.
 

Table: Content

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| content_id       | varchar |
| title            | varchar |
| Kids_content     | enum    |
| content_type     | varchar |
+------------------+---------+
content_id is the primary key (column with unique values) for this table.
Kids_content is an ENUM (category) of types ('Y', 'N') where: 
'Y' means is content for kids otherwise 'N' is not content for kids.
content_type is the category of the content as movies, series, etc.
 

Write a solution to report the distinct titles of the kid-friendly movies streamed in June 2020.



*/