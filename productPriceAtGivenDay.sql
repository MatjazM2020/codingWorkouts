select 
u.product_id, 
coalesce(price, 10) as price
from 
(select 
q.product_id, 
price
from
(select
product_id, 
max(change_date) as dt
from 
Products
where change_date <= '2019-08-16'
group by product_id ) as p
join
(select 
product_id,
change_date,
new_price as price
from 
Products) as q 
on p.product_id = q.product_id and  dt = q.change_date) as w
right join
(select 
distinct product_id
from 
Products
) as u
on w.product_id = u.product_id



/*
problem: https://leetcode.com/problems/product-price-at-a-given-date/description/?envType=study-plan-v2&envId=top-sql-50

Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.
 

Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

Return the result table in any order.
*/ 