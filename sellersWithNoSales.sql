select 
    seller_name
from Seller
where seller_id not in  
(select 
    seller_id 
from Orders 
where year(sale_date) = 2020)
order by seller_name asc



/*
https://leetcode.com/problems/sellers-with-no-sales/description/?envType=study-plan-v2&envId=premium-sql-50

Table: Customer

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| customer_name | varchar |
+---------------+---------+
customer_id is the column with unique values for this table.
Each row of this table contains the information of each customer in the WebStore.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| sale_date     | date    |
| order_cost    | int     |
| customer_id   | int     |
| seller_id     | int     |
+---------------+---------+
order_id is the column with unique values for this table.
Each row of this table contains all orders made in the webstore.
sale_date is the date when the transaction was made between the customer (customer_id) and the seller (seller_id).
 

Table: Seller

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| seller_id     | int     |
| seller_name   | varchar |
+---------------+---------+
seller_id is the column with unique values for this table.
Each row of this table contains the information of each seller.
 

Write a solution to report the names of all sellers who did not make any sales in 2020.

Return the result table ordered by seller_name in ascending order.
*/