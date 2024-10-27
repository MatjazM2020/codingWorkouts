with Apples as 
(select 
    sale_date
    , fruit
    , sum(sold_num) sold_num
from Sales
where fruit = 'apples'
group by sale_date)
, Oranges as
(select
    sale_date
    , fruit
    , sum(sold_num) sold_num
from Sales
where fruit = 'oranges'
group by sale_date)
select
    a.sale_date
    , (a.sold_num - o.sold_num) diff
from Apples a 
inner join Oranges o on a.sale_date = o.sale_date
order by a.sale_date


/*
https://leetcode.com/problems/apples-oranges/description/?envType=study-plan-v2&envId=premium-sql-50

Table: Sales

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| sale_date     | date    |
| fruit         | enum    | 
| sold_num      | int     | 
+---------------+---------+
(sale_date, fruit) is the primary key (combination of columns with unique values) of this table.
This table contains the sales of "apples" and "oranges" sold each day.
 

Write a solution to report the difference between the number of apples and oranges sold each day.

Return the result table ordered by sale_date.


*/