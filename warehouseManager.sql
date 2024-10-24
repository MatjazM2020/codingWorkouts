select
    name warehouse_name
    , sum(units * Width*Length*Height) volume
from Products p
inner join Warehouse w on w.product_id = p.product_id 
group by name


/*
https://leetcode.com/problems/warehouse-manager/description/?envType=study-plan-v2&envId=premium-sql-50
Table: Warehouse

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| name         | varchar |
| product_id   | int     |
| units        | int     |
+--------------+---------+
(name, product_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the information of the products in each warehouse.
 

Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
| Width         | int     |
| Length        | int     |
| Height        | int     |
+---------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row of this table contains information about the product dimensions (Width, Lenght, and Height) in feets of each product.
 

Write a solution to report the number of cubic feet of volume the inventory occupies in each warehouse.

Return the result table in any order.
*/