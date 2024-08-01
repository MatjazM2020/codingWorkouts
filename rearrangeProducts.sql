select product_id, 
    'store1' store,
    store1 price
from Products
where store1 is not null
union 
select product_id, 
    'store2' store,
    store2 price
from Products
where store2 is not null
union 
select product_id, 
    'store3' store,
    store3 price
from Products
where store3 is not null



/*
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.
 
Write a solution to rearrange the Products table so that each row has (product_id, store, price). If a product is not
 available in a store, do not include a row with that product_id and store combination in the result table.
Return the result table in any order.
*/