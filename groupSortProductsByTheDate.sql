select 
sell_date,
count(distinct product) as num_sold, 
group_concat(distinct product order by product asc separator ',') as products
from 
Activities 
group by sell_date



/* 
prob: https://leetcode.com/problems/group-sold-products-by-the-date/?envType=study-plan-v2&envId=top-sql-50
Table Activities:

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each row of this table contains the product name and the date it was sold in a market.
 

Write a solution to find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.
*/ 