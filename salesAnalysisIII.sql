select product_id, product_name from Product where product_id not in 
(select p.product_id
from Product p
join Sales s on p.product_id = s.product_id and ((sale_date < '2019-01-01') or (sale_date > '2019-03-31')))
and product_id in (
    select s.product_id
    from Sales s
    where s.sale_date between '2019-01-01' and '2019-03-31'
);



/*
https://leetcode.com/problems/sales-analysis-iii/description/

Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the name and the price of each product.
Table: Sales

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| seller_id   | int     |
| product_id  | int     |
| buyer_id    | int     |
| sale_date   | date    |
| quantity    | int     |
| price       | int     |
+-------------+---------+
This table can have duplicate rows.
product_id is a foreign key (reference column) to the Product table.
Each row of this table contains some information about one sale.
 

Write a solution to report the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

Return the result table in any order.
*/