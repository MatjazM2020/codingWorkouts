select 
    customer_id
    ,customer_name
from Customers
where customer_id not in 
(select 
    customer_id
from Orders 
where product_name = 'C')
and customer_id in 
(select 
    customer_id
from Orders
where product_name = 'A')
and customer_id in
(select 
    customer_id
from Orders
where product_name = 'B')
order by customer_id asc


/*
https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/?envType=study-plan-v2&envId=premium-sql-50

Table: Customers

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| customer_id         | int     |
| customer_name       | varchar |
+---------------------+---------+
customer_id is the column with unique values for this table.
customer_name is the name of the customer.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| customer_id   | int     |
| product_name  | varchar |
+---------------+---------+
order_id is the column with unique values for this table.
customer_id is the id of the customer who bought the product "product_name".
 

Write a solution to report the customer_id and customer_name of customers who bought products "A", "B" but did not buy the product 
"C" since we want to recommend them to purchase this product.

Return the result table ordered by customer_id.
*/