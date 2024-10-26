select
    round((count(im.delivery_id)/count(*))*100, 2) immediate_percentage
from Delivery d
left join Delivery im on d.delivery_id = im.delivery_id 
and im.order_date = im.customer_pref_delivery_date




/*
https://leetcode.com/problems/immediate-food-delivery-i/description/?envType=study-plan-v2&envId=premium-sql-50


Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the primary key (column with unique values) of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
 

If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

Write a solution to find the percentage of immediate orders in the table, rounded to 2 decimal places.
*/