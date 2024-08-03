with cte1 as (
    select stock_name, sum(price) minus from Stocks where operation = 'Buy' group by stock_name
),cte2 as (
    select stock_name, sum(price) plus from Stocks where operation = 'Sell' group by stock_name
)
select 
    t1.stock_name
    , (plus - minus) capital_gain_loss
from  
    cte1 t1 inner join cte2 t2 
on 
    t2.stock_name = t1.stock_name





/*
https://leetcode.com/problems/capital-gainloss/

Table: Stocks

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| stock_name    | varchar |
| operation     | enum    |
| operation_day | int     |
| price         | int     |
+---------------+---------+
(stock_name, operation_day) is the primary key (combination of columns with unique values) for this table.
The operation column is an ENUM (category) of type ('Sell', 'Buy')
Each row of this table indicates that the stock which has stock_name had an operation on the day operation_day with the price.
It is guaranteed that each 'Sell' operation for a stock has a corresponding 'Buy' operation in a previous day. It is also guaranteed 
that each 'Buy' operation for a stock has a corresponding 'Sell' operation in an upcoming day.


*/