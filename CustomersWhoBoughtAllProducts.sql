select 
customer_id
from
(select 
customer_id,
count(distinct product_key) as numb
from 
Customer
group by customer_id) as w
where numb = (select count(*) from Product)




/*
problem: https://leetcode.com/problems/customers-who-bought-all-products/description/?envType=study-plan-v2&envId=top-sql-50

Table: Customer
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
This table may contain duplicates rows. 
customer_id is not NULL.
product_key is a foreign key (reference column) to Product table.

Table: Product
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key is the primary key (column with unique values) for this table.
 
Write a solution to report the customer ids from the Customer table that bought all the products in the Product table.
Return the result table in any order.
*/
