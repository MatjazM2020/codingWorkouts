with a as (select 
    count(customer_number) c, 
    customer_number 
from Orders 
group by customer_number) 

select customer_number 
from a where 
c = (select max(c) from a)


/* https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
Table: Orders

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.
 
Write a solution to find the customer_number for the customer who has placed the largest number of orders.
The test cases are generated so that exactly one customer will have placed more orders than any other customer.

*/ 