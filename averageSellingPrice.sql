select 
o.product_id,
coalesce(average_price,0) as average_price
from
(select distinct product_id
from 
Prices) as o
left join
(select 
product_id,
round(sum(priceUnits)/sum(units),2) as average_price
from
(select 
w.product_id,
units,
price*units as priceUnits
from
(select 
product_id,
purchase_date,
sum(units) as units 
from 
UnitsSold 
group by 
product_id, 
purchase_date) as w
join 
Prices
on Prices.product_id = w.product_id 
and purchase_date between start_date and end_date) as k
group by 
product_id) as p
on p.product_id = o.product_id

/*
Exercise: 

Table: Prices
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| start_date    | date    |
| end_date      | date    |
| price         | int     |
+---------------+---------+
(product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the price of the product_id in the period from start_date to end_date.
For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods
 for the same product_id.

table: UnitsSold
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| purchase_date | date    |
| units         | int     |
+---------------+---------+
This table may contain duplicate rows.
Each row of this table indicates the date, units, and product_id of each product sold. 


Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places.
Return the result table in any order.
*/