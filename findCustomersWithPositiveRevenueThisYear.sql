select 
    customer_id
from Customers
where year = 2021 and revenue > 0


/*
https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/description/?envType=study-plan-v2&envId=premium-sql-50

Table: Customers

+--------------+------+
| Column Name  | Type |
+--------------+------+
| customer_id  | int  |
| year         | int  |
| revenue      | int  |
+--------------+------+
(customer_id, year) is the primary key (combination of columns with unique values) for this table.
This table contains the customer ID and the revenue of customers in different years.
Note that this revenue can be negative.
 

Write a solution to report the customers with postive revenue in the year 2021.

Return the result table in any order.


*/