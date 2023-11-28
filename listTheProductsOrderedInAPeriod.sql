SELECT  
    p.product_name, 
    x.unit
FROM 
    Products p
    join 
    (SELECT
        * 
    FROM 
        (SELECT 
        product_id, 
        sum(unit) AS unit
        FROM 
        Orders
        WHERE MONTH(order_date) = 2 AND YEAR(order_date) = 2020 
        GROUP BY product_id) AS t 
        WHERE unit >= 100
    ) AS x 
    ON x.product_id = p.product_id 


/* 
prob: https://leetcode.com/problems/list-the-products-ordered-in-a-period/submissions/1108217178/?envType=study-plan-v2&envId=top-sql-50
Table: Products

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
product_id is the primary key (column with unique values) for this table.
This table contains data about the company's products.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
This table may have duplicate rows.
product_id is a foreign key (reference column) to the Products table.
unit is the number of products ordered in order_date.
 

Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.

*/ 